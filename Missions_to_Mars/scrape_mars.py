# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd

def init_browser():
    # Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

mars_info = {}



