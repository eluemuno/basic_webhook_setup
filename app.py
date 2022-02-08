from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Simple Webhooks Test'

@app.route('/testHooks', methods=['POST'])
def testHook():
    data = request.json
    return data

if __name__ == '__main__':
    app.run(debug=True, port=1980)
