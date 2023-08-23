#importing libraries
import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

#creating instance of the class
app=Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    # print(ValuePredictor([3, 2, 1, 0.2]))
    return flask.render_template('index.html')
    #return "Hello World"


#prediction function
def ValuePredictor(pred_vals):
    to_predict = np.array(pred_vals)
    with open('SVM.pickle', 'rb') as f:
        model = pickle.load(f)
    return model.predict(to_predict)



@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()

        prediction = "Batata"

        s_width = float(to_predict_list['s_width'])
        s_length = float(to_predict_list['s_length'])
        p_width = float(to_predict_list['p_width'])
        p_length = float(to_predict_list['p_length'])

        prediction = ValuePredictor([[s_width, s_length, p_width, p_length]])

        return render_template("result.html",prediction=prediction)

if __name__=="__main__":
    app.run(debug = True)

