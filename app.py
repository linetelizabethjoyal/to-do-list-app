from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight_kg, height_cm):
    h_m = height_cm / 100.0
    if h_m <= 0:
        return None
    bmi = weight_kg / (h_m * h_m)
    return bmi

def bmi_category(bmi):
    if bmi is None:
        return ("Invalid", "")
    if bmi < 18.5:
        return ("Underweight", "underweight")
    elif bmi <= 24.9:
        return ("Normal", "normal")
    elif bmi <= 29.9:
        return ("Overweight", "overweight")
    else:
        return ("Obese", "obese")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        weight = float(request.form.get("weight", 0))
        height = float(request.form.get("height", 0))
    except ValueError:
        weight, height = 0, 0

    bmi = calculate_bmi(weight, height)
    if bmi is None or bmi <= 0:
        result = {"bmi": None, "category": "Invalid input", "class": "invalid"}
    else:
        cat, cls = bmi_category(bmi)
        result = {"bmi": round(bmi, 1), "category": cat, "class": cls}

    return render_template("index.html", result=result, height=height, weight=weight)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
