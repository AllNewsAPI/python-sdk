# AllNewsAPI Python SDK

[![pypi version](https://img.shields.io/pypi/v/allnewsapi.svg?style=flat-square)](https://pypi.org/project/allnewsapi/)
[![pypi downloads](https://img.shields.io/pypi/dm/allnewsapi.svg?style=flat-square)](https://pypi.org/project/allnewsapi/)
[![license](https://img.shields.io/pypi/l/allnewsapi.svg?style=flat-square)](LICENSE)
[![build](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square)](https://github.com/AllNewsAPI/python-sdk)

The official **AllNewsAPI SDK** for the Python programming language.

Easily access real-time and historical news articles and headlines from multiple sources around the world.

---

## Installation

```bash
pip install allnewsapi
```

---

## Usage
> AllNewsAPI uses API keys for authentication. To get started, <a href="https://allnewsapi.com/signup" target="_blank">sign up for free</a> to get an API key.

Next, import and initialize the SDK with your API key.

```python
from allnewsapi import NewsAPI, NewsAPIException

# Initialize the SDK
news_api = NewsAPI('your-api-key')

# Basic search
try:
    results = news_api.search(q='bitcoin')
    print(results)
except NewsAPIException as e:
    print(f"Error: {e}")

# Advanced search
try:
    results = news_api.search(
        q='elon musk',
        lang=['en', 'fr'],
        category='technology',
        max=10,
        sortby='relevance'
    )
    print(results)
except NewsAPIException as e:
    print(f"Error: {e}")

# Get headlines
try:
    headlines = news_api.headlines(
        country='us',
        category='business',
        max=5
    )
    print(headlines)
except NewsAPIException as e:
    print(f"Error: {e}")
```

---

## API Reference

### `NewsAPI(api_key)`

Creates a new instance of the NewsAPI client.

- `api_key` (string, required): Your AllNewsAPI API key.

---

### `news_api.search(**options)`

Search for news articles based on various filters and options.  
🔗 [See Full API Documentation](https://allnewsapi.com/docs#search-endpoint)

#### Parameters:

- `q` (str): Keywords to search for.
- `start_date` (str | datetime): Start date for search (`YYYY-MM-DD`, `YYYY-MM-DD HH:MM:SS`, or `datetime` object).
- `end_date` (str | datetime): End date for search.
- `content` (bool): Whether to include full article content.
- `lang` (str | list[str]): Language(s) to filter by.
- `country` (str | list[str]): Country/countries to filter by.
- `region` (str | list[str]): Region(s) to filter by.
- `category` (str | list[str]): Category/categories to filter by.
- `max` (int): Maximum number of results to return (1–100).
- `attributes` (str | list[str]): Specific attributes to search in (`title`, `description`, `content`).
- `page` (int): Page number for pagination.
- `sortby` (str): Sort results by `'publishedAt'` or `'relevance'`.
- `publisher` (str | list[str]): Filter by publisher(s).
- `format` (str): Response format (`'json'`, `'csv'`, `'xlsx'`).

#### Returns:

- `dict`: A dictionary containing the search results.

---

### `news_api.headlines(**options)`

Get the latest news headlines based on various filters and options.
🔗 [See Full API Documentation](https://allnewsapi.com/docs#headlines-endpoint)

#### Parameters:

- `q` (str): Keywords to search for.
- `start_date` (str | datetime): Start date for search (`YYYY-MM-DD`, `YYYY-MM-DD HH:MM:SS`, or `datetime` object).
- `end_date` (str | datetime): End date for search.
- `content` (bool): Whether to include full article content.
- `lang` (str | list[str]): Language(s) to filter by.
- `country` (str | list[str]): Country/countries to filter by.
- `region` (str | list[str]): Region(s) to filter by.
- `category` (str | list[str]): Category/categories to filter by.
- `max` (int): Maximum number of results to return (1–100).
- `attributes` (str | list[str]): Specific attributes to search in (`title`, `description`, `content`).
- `page` (int): Page number for pagination.
- `sortby` (str): Sort results by `'publishedAt'` or `'relevance'`.
- `publisher` (str | list[str]): Filter by publisher(s).
- `format` (str): Response format (`'json'`, `'csv'`, `'xlsx'`).

#### Returns:

- `dict`: A dictionary containing the headlines results.

---

### Notes:
- `start_date` and `end_date` accept either a **string** or a **datetime.datetime** object.
- When `content=True`, full article content will be included in results.
- If `format` is set to `'csv'` or `'xlsx'`, the SDK will return raw binary data — you'll need to handle file saving.

---

## Links

- 📚 [API Documentation](https://allnewsapi.com/docs)
- 🐛 [Report Issues](https://github.com/AllNewsAPI/python-sdk/issues)
- 🌟 [Star the Project](https://github.com/AllNewsAPI/python-sdk)

## License

[MIT](LICENSE)
 