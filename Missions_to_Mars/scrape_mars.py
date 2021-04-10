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

    # Use splinter module to go to Nasa news site
    mns_url = 'https://redplanetscience.com'
    browser.visit(mns_url)

    # HTML Object
    html = browser.html

    # Use BeautifulSoup to parse HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Collect the latest News Title (nt) and Paragraph Text (pt)
    mars_info["nt"] = soup.find('section', class_='image_and_description_container').find('div', class_='content_title').text
    mars_info["pt"] = soup.find('section', class_='image_and_description_container').find('div', class_='article_teaser_body').text
        
    return mars_info

def scrape_fmi():

    browser = scrape_info()

    # Use splinter module to go to JPL Mars Space images site
    fsi_url = 'https://spaceimages-mars.com'
    browser.visit(fsi_url)

    # HTML Object
    html = browser.html

    # Use BeautifulSoup to parse HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Get current featured mars image url
    fmi_url = soup.find('img', class_='headerimage')['src']
    main_url = 'https://www.jpl.nasa.gov' 
    fmi_url = fsi_url + fmi_url
    mars_info["fmi_url"] = fmi_url 
        
    return mars_info

def scrape_mf():
    # Go to the Mars Facts webpage
    mf_url = 'https://galaxyfacts-mars.com/'

    # Use pandas's read_html to read HTML tables into a list of DataFrame objects
    tables = pd.read_html(mf_url)

    # Scrape only the table with mars facts (not earth-mars comparison)  
    mf_df = tables[1]

    # Rename the columns
    mf_df.columns = ['Attribute','Value']
    html_table = mf_df.to_html()
    mars_info["mf"] = html_table

    return mars_info

def scrape_mars_hemispheres():

    browser = scrape_info()

    # Use splinter module to go to Astrogeology site
    hemispheres_url = 'https://marshemispheres.com'
    browser.visit(hemispheres_url)

    # HTML Object
    html = browser.html

    # Use BeautifulSoup to parse HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Find all elements with the class item [where the 4 hemisphere info is organized]
    items = soup.find_all('div', class_='item')    
    items = soup.find_all('div', class_='item')

    # Create a python list for the dictionaries to store hemisphere title and full-resolution image url
    hemisphere_img_urls = []

    # Loop through hemisphere results i.e. items
    for item in items:
        # Store title
        title = item.find('h3').text

        # Find and store link for full-resolution image
        hemisphere_url = 'https://marshemispheres.com/' + item.find('a', class_='itemLink product-item')['href']

        # Visit the full-resolution image links above
        browser.visit(hemisphere_url)

        # HTML Object of each link visited
        html = browser.html

        # Use BeautifulSoup to parse the HTML of  each page visited 
        soup = BeautifulSoup(html, 'html.parser')

        # Get the full-resolution image source
        hemisphere_img_url = 'https://marshemispheres.com/' + soup.find('img', class_='wide-image')['src']

        # Append to list of dictionaries
        hemisphere_img_urls.append({'title': title, 'img_url': hemisphere_img_url})

    mars_info["hemisphere_img_urls"] = hemisphere_img_urls
    
    return mars_info




