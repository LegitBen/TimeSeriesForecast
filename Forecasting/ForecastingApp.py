import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from cfg import models as model_list

models=model_list

app= Flask('__name__')
app.config["debug"]=True


@app.route("/")
def home():
    return render_template("index.html", models=list(models.keys()))

@app.route("/predict", methods=["POST"])
def predict_xom():
    try:
        model_name=request.form.get("model_name")
        date_given=request.form.get("date")
        model=models[model_name]()
        pred=model.predict(date_given)

    except KeyError: #get value from curl header
        model_name = request.headers.get("model_name")
        date_given = request.headers.get("date")
        model = models[model_name]()
        pred = model.predict(date_given)
    return render_template("prediction.html", pdate=model.get_next_date(date_given), ppred=str(pred)[1:-1]

)


if __name__=='__main__':
    app.run(debug=True)




