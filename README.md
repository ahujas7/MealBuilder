# Meal Builder

Using Python and the Selenium Webdriver API, a webscraping tool was created which gathers nutrition data for a variety of foods on a supermarket's website.

After the driver has been set up, an initial search query is entered, for example a product or company name. The driver is able to find product links for every product in the results, even the one's hidden under the 'View More' section. This is achieved by carrying out JavaScript events such as clicking a button and scrolling the window. As the product links are acquired, they are appended to a text file which contains the name of the product along with the corresponding link.

Once all product links have been found, each product page is visited by the driver, one by one, and all of the nutrition data is scraped. For each product, a seperate text file is created to store the scraped data.

Finally, a basic food class was created to extract the major macronutrient data (carbs, protein, and fat) from the text files. This class can also be used to normalize the data to 1 gram servings and sum macros to create entire meals.  
