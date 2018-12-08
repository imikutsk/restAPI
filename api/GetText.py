from flask_restful import Resource
import logging as logger
import urllib.request
from bs4 import BeautifulSoup
import requests
import os

class GetText(Resource):

    def get(self):
        logger.debug("Inside get method")

        # create new folder for text
        text_path = 'txt'
        if not os.path.exists(text_path):
            os.mkdir(text_path)

        url = open('url.txt').read().split('\n')[0]
        #url='http://pixabay.com'
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page.read(), "html.parser")

        for script in soup(["script", "style"]):
            script.extract()

        text = soup.get_text()

        # save text in folder as new file
        f = open(text_path + '/' + url[8:12], 'w')
        f.write(text)
        f.close()


        return 'Save '+ url[8:12]+' file in folder '+text_path



