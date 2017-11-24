#!flask/bin/python
from flask import Flask,jsonify,abort,make_response,request,url_for
from flask_pymongo import PyMongo,MongoClient

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

mongo = PyMongo(app)

@app.route('/v1.0/parcels',methods=['GET'])
def getParcels():
    parcels = mongo.db.mytable
    output = []
    for p in parcels.find():
        output.append({'id': p['id'],'adress': p['adress']})
    return jsonify({'parcels': output})
if __name__ == '__main__':
    app.run(debug=True)
