from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def process_webhook():
    data = request.get_json()
    
    print(data)
    
    return 'OK'

if __name__ == '__main__':
    app.run()