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
    mns_url = 'https://redplanetscience.com'
    browser.visit(mns_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_info["nt"] = soup.find('section', class_='image_and_description_container').find('div', class_='content_title').text

    mars_info["pt"] = soup.find('section', class_='image_and_description_container').find('div', class_='article_teaser_body').text
        
    return mars_info

def scrape_fmi():

    browser = init_browser()

    # Use splinter module to go to visit JPL Mars Space images site
    fsi_url = 'https://spaceimages-mars.com'
    browser.visit(fsi_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    fmi_url = soup.find('img', class_='headerimage')['src']
    main_url = 'https://www.jpl.nasa.gov'
    
    fmi_url = fsi_url + fmi_url
    mars_info["fmi_url"] = fmiurl 
        
    return mars_info

def scrape_mf():
    # Go to the Mars Facts webpage and scrape the table with mars facts only (not earth-mars comparison) using Pandas
    mf_url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(facts_url)
    mf_df = tables[1]
    # Rename the columns
    mf_df.columns = ['Attribute','Value']
    html_table = mf_df.to_html()
    mars_info["mf"] = html_table

    return mars_info




