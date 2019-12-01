from flask import Flask, jsonify,request
import json
app = Flask(__name__)


@app.route('/status',methods=["POST","GET"])
def status():
	with open('./status.json', encoding='utf-8') as json_file:
		json_data = json.load(json_file)
	if request.method=="POST":
		print(request.get_json(force=True))
		json_request = request.get_json()
		with open('./status.json','w',encoding='utf-8')as js_w:
			json.dump(json_data,js_w)

		print(json_request)
		return jsonify(status=json_data['status'])
	elif request.method=="GET":
		return jsonify(json_data) 

	
@app.route('/token',methods=['POST'])
def getToken():
	with open('./status.json', encoding='utf-8') as json_file:
		json_data = json.load(json_file)
	if request.method=="POST":
		json_request = request.get_json()
		print(json_request)
		with open('./status.json','w',encoding='utf-8')as js_w:
			json.dump(json_data,js_w)
		print("getToken")
		print(request.get_json())
		with open('./status.json',encoding='utf-8')as jf:
			json_d=json.load(jf)
		return jsonify(json_d['token'])

@app.route('/initialize',methods=['POST'])
def Initialize():
	with open('./status.json',encoding='utf-8') as json_file:
		json_data = json.load(json_file)
	if request.method=='POST':
		json_data['status']='normal'
		json_data['token']=json_data['token']
		json_data['is_escaped']=False
		json_data['pushed']=False
		with open('./status.json','w',encoding='utf-8') as js_w:
			json.dump(json_data,js_w)
		print("server initialized")
		return jsonify(message="server initialized!")


@app.route('/escaped',methods=['POST'])
def Escaped():
	with open('./status.json',encoding='utf-8') as json_file:
		json_data = json.load(json_file)
	if request.method=="POST":
		json_data['is_escaped']=True
		with open('./status.json','w',encoding='utf-8') as js_w:
			json.dump(json_data,js_w)
		print("escape complete")
		return jsonify(message="escaped!")


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=80,debug=False)
