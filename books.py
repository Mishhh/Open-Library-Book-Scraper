import scrapy
import json


class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = ["https://openlibrary.org/subjects"]

    def parse(self, response):
        for subject_heading in response.css("#subjectsPage h3"):
            subject_name = subject_heading.css("::text").get().strip()

            category_list_items = subject_heading.xpath("following-sibling::ul[1]/li")

            for category_item in category_list_items:
                category_name = category_item.css("a::text").get().strip()
                category_link = category_item.css("a::attr(href)").get()

                category_slug = category_link.split("/")[-1]

                api_url = f"https://openlibrary.org/subjects/{category_slug}.json?details=true&limit=5"

                yield scrapy.Request(
                    url=api_url,
                    callback=self.parse_category_books,
                    meta={
                        "subject_name": subject_name,
                        "category_name": category_name
                    }
                )

    def parse_category_books(self, response):
        subject_name = response.meta["subject_name"]
        category_name = response.meta["category_name"]

        category_data = json.loads(response.text)

        for book in category_data.get("works", []):
            yield {
                "subject": subject_name,
                "category": category_name,
                "title": book.get("title"),
                "authors": [author.get("name") for author in book.get("authors", [])],
                "first_publish_year": book.get("first_publish_year"),
                "subjects": book.get("subject", []),
                "availability": book.get("availability", {})
            }