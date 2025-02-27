from flask import Flask, jsonify, request
app = Flask(__name__)
import http.client
import json
import os

#--------------------------------------------------------------------------
# read environment variables

if 'SERVER' not in os.environ:
    print("Environment variable $SERVER needs to be defined!")
    exit()
else:
    server = os.environ.get('SERVER')
    print("Environment variable SERVER: ", server)

if 'TOKEN' not in os.environ:
    print("Environment variable $TOKEN needs to be defined!")
    exit()
else:
    token = os.environ.get('TOKEN')
    print("Environment variable TOKEN: ", token)

#--------------------------------------------------------------------------
# define HTTP request header and request endpoint

token = "ZenApiKey" + " " + token
header = {
    'Authorization': token,
    "content-type": "application/json",
    'accept': "application/json"
    }

endpoint= "/openpages-openpagesinstance-cr-opgrc/api/v2/contents"

#--------------------------------------------------------------------------


@app.route('/', methods=['GET'])
def hello_world():
    print("***********Hello, World!***********")
    return 'Hello, World!'

@app.route('/Submit_For_Review', methods=['GET'])
def Submit_For_Review():
    print("\nREST call received: Submit_For_Review")
    object_id = request.args.get('id')
    if object_id != None:
        print( "Object ID= " + object_id)
    else:
        return "Object ID= Undefined"
    # Retrieve the objects's field values via the 
    # REST API of the Governance Console
    endpoint = "/openpages-openpagesinstance-cr-opgrc/api/v2/contents/"+object_id
    conn = http.client.HTTPSConnection(server)
    conn.request("GET", endpoint, headers=header)
    response = conn.getresponse()
    print("Status: {}\nReason: {}\n".format(response.status, response.reason))
    if response.status == 200:
        data = response.read().decode("utf-8")
        my_dict = json.loads(data)
        result = "Success! object ID found ===> " + my_dict["name"]
        # print the object's field values in JSON format
        print( json.dumps(json.loads(data), indent=4))
    elif response.status == 404:
        result = "Object ID not found "+object_id
    else:
        result = "Error!"
    return result


@app.route('/Return_For_Update', methods=['GET'])
def Return_For_Update():
    print("\nREST call received: Return_For_Update")
    str = request.args.get('id')
    if str != None:
        str = "Object ID= "+str
    else:
        str = "Object ID= Undefined"
    print(str)
    return str

@app.route('/Approve', methods=['GET'])
def Approve():
    print("\nREST call received: Approve")
    str = request.args.get('id')
    if str != None:
        str = "Object ID= "+str
    else:
        str = "Object ID= Undefined"
    print(str)
    return str


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
#    app.run(host='0.0.0.0')

