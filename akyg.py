from flask import Flask,request
from flask_restful import Api, Resource
import random

app = Flask(__name__)
api=Api(app)

class rastgele(Resource):
	def get(self):
		randomnumber=random.randint(0,9)
		return {'Sayi': randomnumber}, 200

class kupAl(Resource):
	def get(self,number):
		kupu=number**3
		return {'KUPU' : kupu},200

class Name(Resource):
	def get(self,name):
		return {'UYARI': 'endpoint yok'},404


api.add_resource(rastgele, '/rastgeleSayi')
api.add_resource(kupAl, '/kupAl/<int:number>')
api.add_resource(Name, '/<string:name>')

#
if __name__=='__main__':
	app.run(host="0.0.0.0",port=5000)
	app.run()
