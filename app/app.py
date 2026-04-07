from flask import Flask, request

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send():
    message = request.form['message']    
    return f"Message sent to flask application: {message}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
