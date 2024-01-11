# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import pickle
import joblib
import numpy as np
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)
model = DecisionTreeClassifier()

joblib.dump(model, 'rain.pkl', protocol=4)
loaded_model = joblib.load('rain.pkl')
model = pickle.load(open('rain.pkl', 'rb'))
joblib.dump(model, 'rain.pkl')


@app.route('/')
def start():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    try:
        # Check if 'rd' is present in the form data
        a = request.form.get("min_temp")
        b = request.form.get("humidity_9am")
        c = request.form.get("wind_speed")
        d = request.form.get("pressure_9am")
        e = request.form.get("wind_gust_speed")
        f = request.form.get("humidity_3pm")
        g = request.form.get("pressure_3pm")
        h = request.form.get("wind_speed_9am")
        i = request.form.get("temp_3pm")
        j = request.form.get("wind_dir_3pm")
        k = request.form.get("max_temp")
        l = request.form.get("rainfall")
        m = request.form.get("wind_dir_9am")
        n = request.form.get("year")
        o = request.form.get("month")


# Check if any of the required fields are missing
        if any(field is None for field in [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o]):
            return "Error: One or more required fields are missing in the form data", 400
        if s is None:
            return "Error: 's' field is missing in the form data", 400

# Convert 's' to numeric value based on your logic
        if s == "cal":
            s = 0
        elif s == "flo":
            s = 1
        else:
            s = 2
# Convert s to numeric value based on your logic
        if s == "cal":
            s = 0
        elif s == "flo":
            s = 1
        else:
            s = 2

        t = [[float(p), float(q), float(r), float(s)]]
        output = model.predict(t)

        return render_template("index.html", y="The predicted profit is " + str(np.round(output[0])))

    except KeyError as e:
        return f"Error: {str(e)}", 400


if __name__ == '__main__':
    app.run(debug=True)
