from flask_restful import Resource
import logging as logger
import urllib.request
from bs4 import BeautifulSoup
import requests
import os

class GetImages(Resource):

    def get(self):

        url = open('url.txt').read().split('\n')[0]
        #url = 'http://pixabay.com'
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page.read(), "html.parser")

        # create new folder for images
        images_path = 'img_' + url[8:12]
        if not os.path.exists(images_path):
            os.mkdir(images_path)

        sum=0
        images = []
        for img in soup.findAll('img'):

            if (img.get('src').startswith('http')):
                images.append(img)

        for image in images:
            im = image.get('src')

            # save images in folder img as new files
            file_name = im.split('/')[-1]
            f = open(images_path + '/' + file_name[0:15], 'wb')
            sum = sum + 1
            r = requests.get(im)
            f.write(r.content)
            f.close()

        #return 'Save '+str(sum)+' images in folder '+images_path
        return sum


