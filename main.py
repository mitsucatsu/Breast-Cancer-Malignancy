import numpy as np
import joblib
import inquirer
from src.inputs import get_user_input

# Load the model
model = joblib.load('models/svm.pkl')

# Define initial question
initial = [
    inquirer.List(
        'action',
        message='What would you like?',
        choices=['Predict', 'Exit']
    )
]

# Prompt
initial_answer = inquirer.prompt(initial)

# Action
if initial_answer['action'] == 'Predict':
    # Get user input
    new_data = get_user_input()

    # Make a Prediction
    prediction = model.predict(new_data)[0]

    # Map numerical prediction
    label_map = {
        2: 'Benigh',
        4: 'Malignant'
    }
    prediction_label = label_map.get(prediction , 'Unknown')

    print(f"Prediction: {prediction_label}")

else:
    print('Exit, bye.')
