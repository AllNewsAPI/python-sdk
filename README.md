# FreeNewsAPI Python SDK

[![pypi version](https://img.shields.io/pypi/v/freenewsapi.svg?style=flat-square)](https://pypi.org/project/freenewsapi/)
[![pypi downloads](https://img.shields.io/pypi/dm/freenewsapi.svg?style=flat-square)](https://pypi.org/project/freenewsapi/)
[![license](https://img.shields.io/pypi/l/freenewsapi.svg?style=flat-square)](LICENSE)
[![build](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square)](https://github.com/FreeNews-API/python-sdk)

The official **FreeNewsAPI SDK** for the Python programming language.

Easily access real-time and historical news articles and headlines from multiple sources around the world.

---

## Installation

```bash
pip install freenewsapi
```

---

## Usage
> FreeNewsAPI uses API keys for authentication. To get started, <a href="https://freenewsapi.com/signup" target="_blank">sign up for free</a> to get an API key.

Next, import and initialize the SDK with your API key.

```python
from freenewsapi import NewsAPI, NewsAPIException

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
```

---

## API Reference

### `NewsAPI(api_key)`

Creates a new instance of the NewsAPI client.

- `api_key` (string, required): Your FreeNewsAPI API key.

---

### `news_api.search(**options)`

Search for news articles based on various filters and options.  
🔗 [See Full API Documentation](https://freenewsapi.com/documentation#search-endpoint)

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

### Notes:
- `start_date` and `end_date` accept either a **string** or a **datetime.datetime** object.
- When `content=True`, full article content will be included in results.
- If `format` is set to `'csv'` or `'xlsx'`, the SDK will return raw binary data — you'll need to handle file saving.

---

## Links

- 📚 [API Documentation](https://freenewsapi.com/documentation)
- 🐛 [Report Issues](https://github.com/FreeNews-API/python-sdk/issues)
- 🌟 [Star the Project](https://github.com/FreeNews-API/python-sdk)

## License

[MIT](LICENSE)
 