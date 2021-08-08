import os
import sys
import requests
import re
from bs4 import BeautifulSoup

#switching to current running python files directory
#os.chdir("\\".join(__file__.split("/")[:-1]))


#function to get the HTML of the page

def getPageFromMedium(page):
    global url
    url = page
    
    if not re.match(r'https?://medium.com/',url):
        print("Please enter a valid URL from Medium")
        sys.exit()


if __name__== "__main__":

    getPageFromMedium("https://betterprogramming.pub/a-standing-desk-saved-my-career-18fd54e95737")
