from flask import Flask, render_template, request, jsonify, Response, redirect
from dijkstar import Graph, find_path
import json
from data import *


keys = list(roomNameDict.keys())
keys = sorted(keys)
errStr = [{'err':''}]
keysVals = []
for key, value in roomNameDict.items():
	kv = value+". "+key
	keysVals.append(kv)


app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
	return render_template("index.html", error=errStr, roomList=keysVals)
		

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
	return json.dumps(keys)

@app.route("/directions", methods=['POST'])
def directions():
	global errStr
	srcName = request.form.get('source')
	destName = request.form.get('destination')
	#verification of failing test cases
	source,destination = verify_fails(srcName, destName)
	if not source:
		return redirect('/')
	#all fails are passed and we find the path
	errStr = [{'err':''}]
	path,cost = getPath(source,destination)
	dirsList = []
	for i in range(len(path)-1):#generates a list of directions for the nodes belongin to the path
		keyDirDict = path[i]+','+path[i+1]
		try:
			roomDirDict[keyDirDict]
		except:
			roomDirDict[keyDirDict] = "Continue Straight"
		dirsList.append({'room': path[i], 'dir' : roomDirDict[keyDirDict], 'count': i+1, 'name': get_key(roomNameDict,path[i])})
	return render_template('directions.html', directions=dirsList, srcDest=[{'src':srcName, 'dest':destName, 'cost': cost}])



def getPath(str1,str2):
	cost_func = lambda u, v, e, prev_e: e['cost']
	dijk = find_path(graph, str1, str2, cost_func=cost_func)
	path = dijk[0]
	return path, dijk[3]

def get_key(my_dict, val): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key 

def verify_fails(srcName, destName):
	global errStr
	if srcName == '' and destName == '':
		errStr = [{'err':'Please enter a value for Source and Destination.'}]
		return False, False
	elif srcName == '':
		errStr = [{'err':'Please enter a value for Source.'}]
		return False, False
	elif destName == '':
		errStr = [{'err':'Please enter a value for Destination.'}]
		return False, False
	try:
		source = roomNameDict[srcName]
		destination = roomNameDict[destName]
		return source,destination
	except:
		errStr = [{'err':'Please enter a value for Source and Destination from the drop down.'}]
		return False, False

if __name__ == "__main__":
    app.run(debug=True)