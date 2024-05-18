# A very simple Flask Hello World app for you to get started with...


from flask import Flask, render_template, request,jsonify
from model import diagnosis
from chatbot import chatbot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = chatbot.respond(user_input)
    return jsonify({'response': response})

@app.route('/ner', methods=['POST'])
def ner():
    # Get user input from the request
    user_input = request.form['text']
    print(user_input)
    # Call the diagnosis function from model.py
    ner_results = diagnosis(user_input)


    # Return the NER results as JSON
    return jsonify({'ner_results': ner_results})
