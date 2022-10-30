from flask import Flask, jsonify, request, render_template
from flask_restful import Api, Resource
import json

server = Flask(__name__)
api = Api()

class Keys(Resource):
    def get(self):
        with open('./static/storage.data', 'r', encoding = 'UTF-8') as f:           
            raw_data = json.loads(f.read())
            if raw_data:
                return raw_data
        return {}

class Key(Resource):
    def get(self,key):
        with open('./static/storage.data', 'r', encoding = 'UTF-8') as f:           
            raw_data = json.loads(f.read())
            if str(key) in raw_data:
                return raw_data.get(key)
            else:   
                return "key not found"
        
class Post(Resource):
    def post(self):
        with open('./static/storage.data', 'r', encoding = 'UTF-8') as f: 
            raw_data = json.loads(f.read())
            req_data = request.get_json(force=False, silent=False, cache=True)
            key = list(req_data.keys())[0]
            value = list(req_data.values())[0]
            if key in raw_data and [value]:
                raw_data[key] = raw_data[key] + [value]
            else:
                raw_data.update({key: [value]})

        with open('./static/storage.data', 'w+',encoding = 'UTF-8') as f:
            f.write(json.dumps(raw_data, indent=4))
            f.close()    
        return "Success"

@server.route('/')
def hello():
    return render_template('index.html')


api.add_resource(Keys, "/api/v1/storage/json/all")
api.add_resource(Key, "/api/v1/storage/json/key=<string:key>")
api.add_resource(Post,"/api/v1/storage/json/write")
api.init_app(server)




