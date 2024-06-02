from flask import Flask,jsonify, render_template, request, url_for
import joblib as job
import numpy as np
app =Flask(__name__, template_folder='templete')

model =job.load('floods.joblib')


@app.route('/', methods=['GET'])
def home():
    return render_template('/floods.html')

@app.route('/', methods=['POST'])
def predict():
    if request.method == "POST":
        features = [float(x) for x in request.form.values()]
        array_features = [np.array(features)]
        prediction= model.predict(array_features)

        return render_template('/floods.html', prediction=prediction)
    return render_template ('/floods.html')
    #
if __name__ == '__main__':
    app.run(debug=True)
