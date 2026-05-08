import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load model
model = joblib.load(r"C:\Users\morea\Downloads\Desktop.plk")

df = pd.DataFrame()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    global df

    # Get input values
    input_features = [int(x) for x in request.form.values()]
    features_value = np.array(input_features)

    # Validate hours
    if input_features[0] < 0 or input_features[0] > 24:
        return render_template(
            'index.html',
            prediction_text='Please enter valid hours between 1 to 24'
        )

    # Prediction
    output = round(model.predict([features_value])[0][0], 2)

    # Save data
    new_data = pd.DataFrame({
        'Study Hours': [input_features[0]],
        'Predicted Output': [output]
    })

    df = pd.concat([df, new_data], ignore_index=True)

    print(df)

    df.to_csv('smp_data_from_app.csv', index=False)

    return render_template(
        'index.html',
        prediction_text=f'You will get [{output}%] marks when you study [{features_value[0]}] hours per day'
    )


if __name__ == "__main__":
    app.run(debug=True)