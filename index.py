"""
FreeNewsAPI Python SDK

A Python wrapper for the Free News API.
"""

import datetime
import json
import typing
from urllib.parse import urlencode
import requests
import ssl
import certifi
import base64

ssl_context = ssl.create_default_context(cafile=certifi.where())

class NewsAPIError(Exception):
    """Exception raised for Free News API errors."""

    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"NewsAPI Error ({status_code}): {message}")


class NewsAPI:
    """Client for the Free News API."""

    def __init__(self, api_key: str, base_url: str = "https://api.freenewsapi.com", timeout: int = 60):
        """
        Initialize the NewsAPI client.

        Args:
            api_key: Your Free News API key
            base_url: The base URL for the API (default: https://api.freenewsapi.com)
            timeout: Request timeout in seconds (default: 60)
        
        Raises:
            ValueError: If API key is not provided
        """
        if not api_key:
            raise ValueError("API key is required")

        self.api_key = api_key
        self.base_url = base_url
        self.search_endpoint = f"{base_url}/v1/search"
        self.timeout = timeout

    def _build_url(self, params: dict) -> str:
        """
        Build the URL with query parameters for the API request.
        
        Args:
            params: Query parameters for the search
            
        Returns:
            The complete URL for the API request
        """
        # Add API key
        params["apikey"] = self.api_key
        
        # Process parameters
        for key, value in list(params.items()):
            # Skip None values
            if value is None:
                del params[key]
                continue
                
            # Convert lists/tuples to comma-separated strings
            if isinstance(value, (list, tuple)):
                params[key] = ','.join(str(item) for item in value)
                
            # Convert datetime objects to ISO format
            elif isinstance(value, datetime.datetime):
                params[key] = value.isoformat()
                
            # Convert date objects to ISO format
            elif isinstance(value, datetime.date):
                params[key] = value.isoformat()
                
            # Convert booleans to strings
            elif isinstance(value, bool):
                params[key] = str(value).lower()
        
        # Build query string
        query_string = urlencode(params)
        
        return f"{self.search_endpoint}?{query_string}"

    def _get_error_message(self, status_code: int) -> str:
        """
        Get an error message based on status code.
        
        Args:
            status_code: HTTP status code
            
        Returns:
            Error message
        """
        error_messages = {
            400: "Bad Request - Your request is invalid",
            401: "Unauthorized - Invalid API Key or Account status is inactive",
            403: "Forbidden - Your account is not authorized to make that request",
            429: "Too Many Requests - You have reached your daily request limit. The next reset is at 00:00 UTC",
            500: "Internal Server Error - We had a problem with our server. Please try again later",
            503: "Service Unavailable - We're temporarily offline for maintenance. Please try again later"
        }
        
        return error_messages.get(status_code, f"Unknown error with status code: {status_code}")

    def _make_request(self, params: dict) -> typing.Union[dict, bytes]:
        """
        Make a request to the API.
        
        Args:
            params: Query parameters for the request
            
        Returns:
            The API response (JSON dict or bytes for non-JSON formats)
            
        Raises:
            NewsAPIError: If the API request fails
        """
        url = self._build_url(params)
        
        try:
            response = requests.get(url, timeout=self.timeout)
            
            # Handle HTTP errors
            if not response.ok:
                error_message = self._get_error_message(response.status_code)
                
                # Try to get more detailed error from response
                try:
                    error_data = response.json()
                    if "message" in error_data:
                        error_message = error_data["message"]
                    if "detail" in error_data:
                        error_message = error_data["detail"]["message"]
                except (ValueError, json.JSONDecodeError):
                    pass
                    
                raise NewsAPIError(response.status_code, error_message)
            
            # Handle different formats
            response_format = params.get("format", "json")
            
            if response_format == "json":
                return response.json()
            else:
                # For CSV, XLSX, etc. return raw bytes
                return response.content
                
        except requests.RequestException as e:
            raise NewsAPIError(500, f"Request failed: {str(e)}")

    def search(self, **kwargs) -> typing.Union[dict, bytes]:
        """
        Search for news articles.
        
        Args:
            **kwargs: Query parameters for the search
            q (str): Keywords to search for
            startDate (str, datetime): Start date
            endDate (str, datetime): End date
            content (bool): Whether to include full content
            lang (str, list): Language(s) to filter by
            country (str, list): Country/countries to filter by
            region (str, list): Region(s) to filter by
            category (str, list): Category/categories to filter by
            max (int): Maximum number of results
            attributes (str, list): Attributes to search in (title, description, content)
            page (int): Page number for pagination
            sortby (str): Sort by 'publishedAt' or 'relevance'
            publisher (str, list): Publisher(s) to filter by
            format (str): Response format (json, csv, xlsx)
                
        Returns:
            Search results (dict for JSON, bytes for other formats)
            
        Raises:
            NewsAPIError: If the API request fails
        """
        return self._make_request(kwargs)
