# utils/config.py

# Base URL for the API
BASE_URL = "https://admin-api.nfttrace.com"  # Replace with the actual base URL of your API

# Default headers for API requests
DEFAULT_HEADERS = {
    "Content-Type": "application/json"
}

# Timeout setting for API requests (in seconds)
REQUEST_TIMEOUT = 10  # Adjust this value as needed

# Login credentials for testing (used in login tests)
LOGIN_CREDENTIALS = {
    "email": "superadmin@gmail.com",
    "password": "Admin@123",
    "rememberMe": True
}
