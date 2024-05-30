import requests

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} is up and running.")
        else:
            print(f"{url} returned status code {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"Error checking {url}: {e}")

if __name__ == "__main__":
    check_website('https://www.example.com')
