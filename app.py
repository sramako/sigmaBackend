import os
from flask import Flask
from flask import request
import json
from flask_cors import CORS, cross_origin
import pymongo
# import math
import sys

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://ako:sigma123@ds149365.mlab.com:49365/sigma")
mydb = myclient['sigma']

@app.route('/')
def hello():
    return 'Ako: All endponts are live.'

@app.route('/courses')
def courses():
    mycol = mydb["courses"]
    data = dict()
    count = 0
    for course in mycol.find({},{'_id':0}):
        data[count] = course
        count+=1
    return json.dumps(data)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	CORS(app, resources=r'/*')
    # app.config['CORS_HEADERS'] = 'Content-Type'
	app.run(host='0.0.0.0', port=port,debug=True)
	# app.run()
