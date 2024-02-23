from flask import Flask
from flask import jsonify
from flask import request, render_template

app = Flask(__name__)

@app.route("/chatbot", methods=["GET"])
def chatbot():
    import chatbot

    message = request.json['message']
    res = chatbot.get_message(message)
    
    return jsonify({'res': res})

@app.route('/')
def chatbot_ui():
    return render_template('index.html')