from flask import Flask, request



appFlask = Flask(__name__)



if __name__=='__main__':
    from api import *
    appFlask.run(debug=True, port=8080)

