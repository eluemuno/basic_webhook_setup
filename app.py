from flask import Flask, request, json

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Sherpa webhooks test'

# Sherpa webhookID--635c5ee0-51f8-11ec-b2d3-3bfc26f017e4
@app.route('/sherpaHooks', methods=['POST'])
def sherpaHook():
    data = request.json
    return data

@app.route('/testhook', methods=['POST'])
def testWebHooks():
    return "Webhooks test confirmed, Nnaemeka"

if __name__ == '__main__':
    app.run(debug=True, port=1980)
