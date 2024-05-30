import requests

def check_security_headers(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        security_headers = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "X-XSS-Protection",
            "Referrer-Policy",
            "Permissions-Policy"
        ]

        results = {header: response.headers.get(header, 'Missing') for header in security_headers}
        return results
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    url = "https://www.exemple.com"
    headers_status = check_security_headers(url)
    for header, status in headers_status.items():
        print(f"{header}: {status}")
