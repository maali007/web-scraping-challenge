# web-scraping-challenge
<h3>Part 1: Jupyter Notebook</h3>
<p>Created a Jupyter Notebook that does the following:</p>
<ul>
  <li>Scrapes <a href="https://redplanetscience.com/">redplanetscience.com</a> and collects the latest News Title and Paragraph Text.</li>
  <li>Uses Splinter to navigate to <a href="https://spaceimages-mars.com/">spaceimages-mars.com </a> and finds the image url for the current Featured Mars Image and assign the url string to a variable</li>
  <li>Visit the Mars Facts webpage, <a href="https://galaxyfacts-mars.com/">galaxyfacts-mars.com</a> and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. Use Pandas to convert the data to a HTML table string.</li>
  <li>Visit the astrogeology site, <a href="https://marshemispheres.com/">marshemispheres.com</a>, to obtain high resolution images for each of Mars's hemispheres and save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Using a Python dictionary, store the data using the keys img_url and title.</li> 

<hr>

<h3>Part 2: MongoDB and Flask Application</h3>
<p>Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.</p>

