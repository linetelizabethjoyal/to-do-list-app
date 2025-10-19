from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_bmi():
    try:
        height_cm = float(request.form.get('height', 0))
        weight = float(request.form.get('weight', 0))
        if height_cm <= 0 or weight <= 0:
            raise ValueError("Height and weight must be positive numbers.")

        height_m = height_cm / 100.0
        bmi = round(weight / (height_m ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        return render_template('index.html', bmi=bmi, category=category)
    except Exception as e:
        # Simple error handling: show message in template
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
