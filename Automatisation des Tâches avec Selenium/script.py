from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def automate_browser(url):
    options = Options()
    options.headless = True  # Exécuter le navigateur en mode headless
    service = Service('path/to/chromedriver')  # Remplacez par le chemin de votre ChromeDriver

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    # Exemple : récupérer le titre de la page
    title = driver.title
    print(f'Title: {title}')

    # Fermer le navigateur
    driver.quit()

if __name__ == "__main__":
    automate_browser('https://www.example.com')
