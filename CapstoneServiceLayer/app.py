from flask import Flask, render_template, Response
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)

# MongoDB initialization values
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'capstoneproject'
COLLECTION_NAME = 'zipData'
FIELDS = {"_id": False, 'Zip': True, 'Longitude': True, 'Latitude': True,
          "MedianSalesPrice": True, "QualifyingIncome": True, "HousingAffordabilityIndex": True}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/getData')
def getData():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    zipData = collection.find(projection=FIELDS)
    json_zipData = []
    for zip in zipData:
        json_zipData.append(zip)
    json_zipData = json.dumps(json_zipData, default=json_util.default)
    connection.close()
    return json_zipData


@app.route('/getZipInfo/<string:zip>')
def getZipInfo(zip):
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    zipInfo = collection.find({'Zip': zip}, projection={
                              '_id': False, 'MedianSalesPrice': True, 'QualifyingIncome': True, 'HousingAffordabilityIndex': True})
    json_zipInfo = []
    for zip in zipInfo:
        json_zipInfo.append(zip)
    if json_zipInfo == []:
        json_zipInfo.append({"MedianSalesPrice": "No Data",
                             "QualifyingIncome": "No Data", "HousingAffordabilityIndex": "No Data"})
    print(json_zipInfo)
    json_zipInfo = json.dumps(json_zipInfo, default=json_util.default)
    connection.close()
    return json_zipInfo


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
