#### Web-Scraping-Challenge
# Mission to Mars 

This mission is to scrape the  most recent news from the NASA website. Scrap the martian hemispheres and the Mars Facts table. It also scrapes the latest Martian news story image and displays it at the top of the page. Store them in MongoDB, retreive them from Mongo and render them as a webpage. 

# Header 
On inital page landing, the most recent scrape data is displayed. 

![PageHeaderInitialRender](https://user-images.githubusercontent.com/98897041/173713351-041964d0-28bc-4937-afd2-27eba34863f0.PNG)

### After requested scrape latest news is rendered. 

![HeaderAfterScrapButton](https://user-images.githubusercontent.com/98897041/173713602-54633b3b-bf0d-40ef-b87e-4942c2317a11.PNG)

# Center of Page
Renders scraped Featured Image and Mars Facts table.

![FeatureFacts](https://user-images.githubusercontent.com/98897041/173713692-a17e65f8-78dd-4d2b-9819-d79c58b831d1.PNG)

# Bottom of Page 
Renders Martian hemiphere images

![HemisperesRendered](https://user-images.githubusercontent.com/98897041/173713761-ae23e196-13b5-49e2-8510-0d8dfbaec58a.PNG)



#### Source Websites:  
Mars News Site
https://redplanetscience.com/  
JPL Mars Space Images:   
https://spaceimages-mars.com/
Mars Facts webpage:  
https://galaxyfacts-mars.com/  
astrogeology site:  
https://marshemispheres.com/

#### Dependencies:  
Flask, render_template  | Pymongo  | B4, BeautifulSoup |splinter, Browser | pandas | datetime | ssl | Bootstrap | chromedriver.exe
