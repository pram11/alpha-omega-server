from flask import Flask, jsonify,request
import json
app = Flask(__name__)

with open('./status.json','w',encoding='utf-8') as json_file:
	json_data = json.loads(json_file)
@app.route('/status',methods=["POST","GET"])
def status():
	if request.method=="POST":
		print("test")
		print(request.get_json())
		json_request = request.get_json()
		print(json_request['status'])
		return jsonify(json_data)
	elif request.method=="GET":
		return jsonify(json_data) 

	
@app.route('/token',methods=['POST'])
def getToken():
	if request.method=="POST":
		print("getToken")
		print(request.get_json())
		return jsonify(json_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8995,debug=True)
