from flask import Flask, request, render_template_string
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

np.random.seed(42)
num_houses = 80
bedrooms = []
area = []
price = []
for i in range(60):
    beds = np.random.choice([1, 2, 3, 4, 5, 6], p=[0.15, 0.25, 0.3, 0.15, 0.1, 0.05])
    bedrooms.append(beds)
    area_val = beds * 400 + np.random.randint(200, 800)
    area.append(area_val)
    price_val = 500000 + area_val * 1500 + beds * 250000 + np.random.randint(-300000, 300000)
    price.append(price_val)

for i in range(20):
    beds = np.random.randint(7, 21)
    bedrooms.append(beds)
    area_val = beds * 500 + np.random.randint(1000, 3000)
    area.append(area_val)
    price_val = 1000000 + area_val * 1200 + beds * 300000 + np.random.randint(-500000, 500000)
    price.append(price_val)

X = np.column_stack([bedrooms, area])
y = np.array(price)
model = LinearRegression()
model.fit(X, y)
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    input_bedrooms = ''
    input_area = ''
    
    if request.method == 'POST':
        try:
            input_bedrooms = request.form['bedrooms']
            input_area = request.form['area']
            bedrooms = int(input_bedrooms)
            area = int(input_area)
            
            if bedrooms > 0 and area > 0:
                predicted_price = model.predict([[bedrooms, area]])[0]
                prediction = f"ETB {predicted_price:,.0f}"
            else:
                prediction = "Please enter positive numbers"
                
        except ValueError:
            prediction = "Please enter valid numbers"

    return render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <title>House Price Estimator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 500px;
            margin: 100px auto;
            padding: 20px;
            background-color: #f0f0f0;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
            color: #34495e;
        }
        input {
            width: 100%;
            padding: 12px;
            border: 2px solid #bdc3c7;
            border-radius: 6px;
            font-size: 16px;
        }
        input:focus {
            border-color: #3498db;
            outline: none;
        }
        button {
            width: 100%;
            padding: 15px;
            background-color: #27ae60;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 18px;
            cursor: pointer;
            margin-top: 10px;
        }
        button:hover {
            background-color: #219a52;
        }
        .result {
            margin-top: 25px;
            padding: 20px;
            background-color: #d5f4e6;
            border-radius: 6px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: #27ae60;
            border: 2px solid #27ae60;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>House Price Estimator</h1>
        
        <form method="POST">
            <div class="form-group">
                <label for="bedrooms">Number of Bedrooms:</label>
                <input type="number" id="bedrooms" name="bedrooms" value="{{ input_bedrooms }}" 
                       min="1" max="100" required placeholder="Enter 1-100 bedrooms">
            </div>
            
            <div class="form-group">
                <label for="area">Total Area (sq ft):</label>
                <input type="number" id="area" name="area" value="{{ input_area }}" 
                       min="500" max="50000" required placeholder="Enter area in square feet">
            </div>
            
            <button type="submit">Calculate Estimated Price</button>
        </form>

        {% if prediction %}
        <div class="result">
            Estimated Price: {{ prediction }}
        </div>
        {% endif %}
    </div>
</body>
</html>
''', prediction=prediction, input_bedrooms=input_bedrooms, input_area=input_area)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
