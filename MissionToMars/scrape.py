#----------------------------------------
# Conversion of JN to function
#----------------------------------------

# Dependencies and Setup
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import datetime as dt

#----------------------------------------
# Certificate Handlling 
#----------------------------------------
 
# To accept bad certificate from target site 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#----------------------------------------
# Initialize Browser
#----------------------------------------
 
# Windows
executable_path = {"executable_path": "./chromedriver.exe"}
browser = Browser("chrome", **executable_path)

# Mac
# executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
# browser = Browser("chrome", **executable_path, headless=False)

#----------------------------------------
# Golbal Variable to hold Goodies
#----------------------------------------
goodies = {}

#----------------------------------------
# Mars News
#----------------------------------------

def mars_news(browser):

    # Goto Red Planet Science
    url = "https://redplanetscience.com"
    browser.visit(url)
    # Parse Results HTML with BeautifulSoup
    html = browser.html
    news_soup = BeautifulSoup(html, "html.parser")
    try:
        # Get Headlines/Image/News Paragraph 
        headline = news_soup.find("div", class_="content_title").get_text()
        mi = news_soup.select("div.list_image")
        mi_url = mi[0].find("img").get('src')
        news_paragraph = news_soup.find("div", class_="article_teaser_body").get_text()

        # Save our found treasures
        goodies["Headline"] = headline
        goodies["Nasa_img"] = mi_url
        goodies["News_paragraph"] = news_paragraph

    except AttributeError:
        return None, None
    return goodies

#----------------------------------------
# JPL Mars Space Images—Featured Image
#----------------------------------------

def jpl_mars(browser):
    # Visit the NASA JPL (Jet Propulsion Laboratory) Site
    url = "https://spaceimages-mars.com"
    browser.visit(url)

    # Find the full image button and click it using splinter
    Buttons = browser.find_by_tag("button")
    FullimageButton = Buttons[1]
    FullimageButton.click()

    # Parse Results HTML with BeautifulSoup
    html = browser.html
    image_soup = BeautifulSoup(html, "html.parser")
    try:
        # Retrieve Feature Image url
        img_url = image_soup.select_one("img.fancybox-image").get("src")

        # Create full url and save
        img_url = f"https://spaceimages-mars.com/{img_url}"
        goodies["SpaceMarsImg"] = img_url

    except AttributeError:
        return None, None
    return goodies

#----------------------------------------
# Mars Facts
#----------------------------------------

def mars_facts():

    try:
         # Visit the Mars Facts Site Using Pandas to Read
         mars_df = pd.read_html("https://galaxyfacts-mars.com/")[0]
        #  marst = mars_df.reset_index(drop=True)
         table_data = mars_df.to_html(classes="table table-striped table-light", header=False, index=False)

         # Add to goodies dictionary
         goodies["MarsFacts"] = table_data

    except AttributeError:
        return None, None
    return goodies

#----------------------------------------
# Mars Hemispheres
#----------------------------------------

def mars_hemispheres(browser):
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    try:
        # Get a List of All the Hemispheres
        links = browser.find_by_css("a.product-item h3")
        for i in range(len(links)):
    
            # Find an entry with header
            browser.find_by_css("a.product-item h3")[i].click()
    
            # Find Image Anchor Tag and get url from href
            element = browser.find_link_by_text("Sample").first    
    
            # Find url and title and add to dict
            goodies[f'SpaceMarsImg{i}'] = element["href"]
            goodies[f'SpaceMarsImgTitle{i}'] = browser.find_by_css("h2.title").text

            # Return to prior page 
            browser.back()
    except AttributeError:
        return None, None
    return goodies

#----------------------------------------
# Controller Function for All Scrapes
#----------------------------------------

def scrape_all():
    # executable_path = {"executable_path": "./chromedriver.exe"}
    # browser = Browser("chrome", **executable_path, headless=False)

    # Run each scrape function  
    mars_news(browser)
    jpl_mars(browser)
    mars_facts()
    mars_hemispheres(browser)
    goodies["scrapedate"] = dt.datetime.now()

    browser.quit()
    return goodies

if __name__ == "__main__":
    print(scrape_all())