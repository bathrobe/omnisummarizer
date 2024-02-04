from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    print('Received')
    content = request.data
    print(content)
    return 'Received'

@app.route('/hello', methods=['GET'])
def hello_world():
    print('Hello World')
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)
