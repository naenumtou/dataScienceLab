
import pickle
import numpy as np
import os

from flask import Flask, render_template, request

app = Flask(__name__)
model = pickle.load(open('model.pk', 'rb'))

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def getPredict():
    x1 = request.form['x1']
    x2 = request.form['x2']
    x3 = request.form['x3']
    XTest = np.array([[x1, x2, x3]], dtype = np.float64)
    
    predicted = model.predict(XTest)[0]
    predicted = 1 / (1 + np.exp(-predicted))
    return render_template('index.html',
    prediction_text = f'Predicted: {predicted * 100:.2f}%')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port, debug = True)