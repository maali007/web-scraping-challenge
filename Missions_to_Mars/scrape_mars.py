# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd


def scrape_info():
    # Path to chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

mars_info = {}

def scrape_mns():

    browser = scrape_info()

    # Use splinter module to go to visit Nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_info["nt"] = soup.find('section', class_='image_and_description_container').find('div', class_='content_title').text

    mars_info["pt"] = soup.find('section', class_='image_and_description_container').find('div', class_='article_teaser_body').text
        
    return mars_info



