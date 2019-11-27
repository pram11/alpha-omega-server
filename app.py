from flask import Flask, jsonify,request
import json
app = Flask(__name__)

with open('./status.json',encoding='utf-8') as json_file:
	json_data = json.load(json_file)
@app.route('/status',methods=["POST","GET"])
def status():
	if request.method=="POST":
		print(request.get_json(force=True))
		json_request = request.get_json()
		json_data['status'] = json_request['status']
		with open('./status.json','w',encoding='utf-8')as js_w:
			json.dump(json_data,js_w)

		print(json_request)
		return jsonify(sataus=json_data['status'])
	elif request.method=="GET":
		return jsonify(json_data) 

	
@app.route('/token',methods=['POST'])
def getToken():
	if request.method=="POST":
		json_request = request.get_json()
		json_data['token']=json_request['token']
		with open('./status.json','w',encoding='utf-8')as js_w:
			json.dump(json_data,js_w)
		print("getToken")
		print(request.get_json())
		json_request = request.get_json()
		print(json_request['status'])
		return jsonify(json_data['status'])

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8995,debug=True)
