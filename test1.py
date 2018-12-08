from api import GetText
from api import GetImages
import os


url = open('url.txt').read().split('\n')[0]
text_file = "txt/"+ url[8:12]
images_path = 'img_' + url[8:12]


def test_getText():
    GetText.get(1)
    if os.path.exists(text_file):
        if os.path.getsize(text_file) > 0:
            print("Test getText is OK")
    else:
        print("Test getText is Fail")


def test_getImages():
    GetImages.get(1)
    if os.path.exists(images_path):
        if len([name for name in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, name))]) >0:
            print("Test getImages is OK")
    else:
        print("Test getImages is Fail")



test_getText()
test_getImages()

