from flask_restful import Api

from app import appFlask

from .GetText import GetText
from .GetImages import GetImages

restapp=Api(appFlask)


restapp.add_resource(GetText, "/text")
restapp.add_resource(GetImages, "/images")
