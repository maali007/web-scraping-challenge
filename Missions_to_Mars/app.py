# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars
import pymongo

# Flask app instance
app = Flask(__name__)

# Set mongo connection in line
mongo = PyMongo(app, uri="mongodb://localhost:27017/mymars_app")


 