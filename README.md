# web-scraping-challenge
<h3>Part 1: Jupyter Notebook</h3>
<p>Created a Jupyter Notebook that does the following:</p>
<ul>
  <li>Scrapes <a href="https://redplanetscience.com/">redplanetscience.com</a> and collects the latest News Title and Paragraph Text.</li>
  <li>Uses Splinter to navigate to <a href="https://spaceimages-mars.com/">spaceimages-mars.com </a> and finds the image url for the current Featured Mars Image and assign the url string to a variable</li>
  <li>Visit the Mars Facts webpage, <a href="https://galaxyfacts-mars.com/">galaxyfacts-mars.com</a> and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. Use Pandas to convert the data to a HTML table string.</li>
  <li>Visit the astrogeology site, <a href="https://marshemispheres.com/">marshemispheres.com</a>, to obtain high resolution images for each of Mars's hemispheres and save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Using a Python dictionary, store the data using the keys img_url and title.</li> 
</ul>  

<hr>

<h3>Part 2: MongoDB and Flask Application</h3>
<p>Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above. Here's a <a href="https://github.com/maali007/web-scraping-challenge/blob/main/Missions_to_Mars/Screenshot.png" target="_blank">screenshot</a> of the result: </p>

<img src="https://github.com/maali007/web-scraping-challenge/blob/main/Missions_to_Mars/Screenshot.png">

<hr>
<h3>ISSUES</h3>
<ul>
  <li>Instructions say Mars facts table for second requirement in Part 1. However, there are two tables in <a href="https://galaxyfacts-mars.com/">galaxyfacts-mars.com</a>. The first one has a comparison between Mars and Earth and is in the screenshot in the assignment guide. The second one is only Mars facts. I switched back and forth between the two then finally settled for the comparison one to conform with the guide image.</li>
</ul>  
