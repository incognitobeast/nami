import pickle
from flask import Flask, render_template, request, redirect, url_for, jsonify
import numpy as np
app = Flask(__name__)
ml = pickle.load(open('ml.pkl','rb'))
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        featuresnew = [np.array(features)]
        prediction = ml.predict(featuresnew)
        output = round(prediction[0],2)
        return render_template('index.html', prediction_text=f'Approximate Price of the Property is {output}/')
    except:
        return render_template('index.html', prediction_text=f'Check your Input Values!!')
if __name__=='__main__':
    app.run(debug=True)
