import googleapiclient
from googleapiclient import discovery
import os
import logging
from flask import Flask
from google.cloud import translate

credential_path = "JameProject2019-460487621c01.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = crendential_path


compute = googleapiclient.discovery.build('compute', 'v1')
#
# app = Flask(__name__)
# @app.route('/')
# # web server expose
# def hello():
#     return "Hello Python"
#
# # main trigger
# if  __name__ == '__main__':
#     app.run(host='127.0.0.1', port=8080, debug=True)