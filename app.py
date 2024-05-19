# A very simple Flask Hello World app for you to get started with...


from flask import Flask, render_template, request,jsonify
from model import diagnosis
from chatbot import chatbot
import joblib

# import requests
# API_URL = "https://api-inference.huggingface.co/models/Riftkey/diabetes-prediction"
# API_TOKEN ="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"
# headers = {"Authorization": f"Bearer {API_TOKEN}"}
# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()


model = joblib.load('diabetes_model.pkl')


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



@app.route('/predict_diabetes', methods=['POST'])
def predict_diabetes():
    data = request.get_json()
    # Ensure all features are extracted based on the input names and types
    features = [
        float(data.get('pregnancies', 0)),
        float(data.get('glucose', 0)),
        float(data.get('bloodPressure', 0)),
        float(data.get('skinthickness', 0)),
        float(data.get('insulin', 0)),
        float(data.get('bmi', 0)),
        float(data.get('DiabetesPedigreeFunction', 0)),
        float(data.get('age', 0))
    ]
    # Predict using the model
    # Ensure your model expects a 2D array
    print(model)
    prediction = model.predict([features])[0]
    # prediction = query([features])
    print(prediction)

    # Determine the risk level based on the prediction
    risk = 'High' if prediction == 1 else 'Low'
    return jsonify({'prediction': risk})





#Comment Out Kalo mau di up ke pythonanywhere
if __name__ == '__main__':
    app.run(debug=True)
#^^^^^^^^^^^^di delete/dicomment aja kalo mau di upload kepythonanywhere
