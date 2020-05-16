# disneyland scraping for thedisneybot

import requests
from bs4 import BeautifulSoup as bs
import os

#website with Disneyland images
url = 'https://www.gettyimages.com/photos/disneyland?family=editorial&phrase=disneyland&sort=mostpopular'

# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')

# create directory for disneyland images
if not os.path.exists('disneyland'):
    os.makedirs('disneyland')

# move to new directory
os.chdir('disneyland')

# image file name variable
x = 0

# writing images
for image in image_tags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('disneyland-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass

