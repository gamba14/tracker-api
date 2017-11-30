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
        output.append({'id': p['_id'],'adress': p['adress']})
    return jsonify({'parcels': output})

@app.route('/v1.0/parcels/<int:parcelId>',methods=['GET'])
def getParcel(parcelId):
    parcels = mongo.db.mytable
    p = parcels.find_one({'_id':parcelId})
    if p:
        output = {'id':p['id'],'adress':p['adress'],'city':p['city'],
                    'county':p['county']}
    else:
        output = 'Not found'
    return  jsonify({'Result':output})

@app.route('/v1.0/parcels',methods=['POST'])
def newParcel():
    parcels = mongo.db.mytable
    if not request.json or not 'id' in request.json:
        abort(400)
    idParcel = str(db.seqs.find_and_modify(
        query={ 'collection' : 'admin_collection' },
        update={'$inc': {'id': 1}},
        fields={'id': 1, '_id': 0},
        new=True
    ).get('id'))
    parcel ={
                '_id':idParcel,
                'adress':request.json['adress'],
                'city':request.json['city'],
                'county':request.json['county']
    }
    status = parcels.insert(parcel)
    return jsonify({'parcel':'Ok'}),201

@app.route('/v1.0/parcels/<int:parcelId>', methods=['DELETE'])
def deleteParcel(parcelId):
    parcels = mongo.db.mytable
    p = parcels.find_one_and_delete({'_id':parcelId})
    if p:
        output = {'id':p['_id'],'adress':p['adress'],'city':p['city'],
                    'county':p['county']}
    else:
        output = 'Not found'
    return  jsonify({'Result':output})


if __name__ == '__main__':
    app.run(debug=True)
