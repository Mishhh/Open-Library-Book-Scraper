# 📚 Open Library Subject & Book Scraper

A Python web scraping project built with **Scrapy** that extracts book data from [Open Library](https://openlibrary.org/) by navigating through subjects → categories → books, and storing the results in JSON format.

---

## 🚀 Features
- Scrapes **all subjects** from the Open Library subjects page.
- Navigates to each **category** under a subject.
- Fetches book details via the **Open Library Subjects API**.
- Extracted fields include:
  - Subject name
  - Category name
  - Book title
  - Authors
  - First publish year
  - Subjects (tags)
  - Availability info
- Saves data to `output.json`.

---

## 🛠 Tech Stack
- **Python 3.9+**
- **Scrapy** – for crawling and scraping
- **JSON** – for structured output


---

## 📊 Example Output
```json
{
    "subject": "Art",
    "category": "Architecture",
    "title": "Architecture: Form, Space, & Order",
    "authors": ["Francis D. K. Ching"],
    "first_publish_year": 1979,
    "subjects": ["Architecture", "Design"],
    "availability": {
        "status": "borrow_available",
        "available_to_browse": true
    }
}


