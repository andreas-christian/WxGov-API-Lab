from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    print("***********Hello, World!***********")
    return 'Hello, World!'

@app.route('/Submit_For_Review', methods=['GET'])
def Submit_For_Review():
    print("\nREST call received: Submit_For_Review")
    str = request.args.get('id')
    if str != None:
        str = "Object ID= "+str
    else:
        str = "Object ID= Undefined"
    print(str)
    return str

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

