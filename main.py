from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    content = request.data
    print(content)
    return 'Received'

if __name__ == '__main__':
    app.run(debug=True)
