from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_command():
    command = request.form['command']
    print("Received command:", command)
    # 執行指令並返回結果
    # ...

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1234)  # 設定伺服器的IP和端口號