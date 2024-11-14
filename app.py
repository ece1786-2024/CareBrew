from flask import Flask, render_template, request
import openai
import pandas as pd

# Import functions from the modules
from models.training_mode_prompt import call_to_API as generate_scenario
from models.training_mode_response import call_to_API as process_training_response
from models.assistant_mode_response import call_to_API as generate_assistant_response

app = Flask(__name__)

# Route for the main selection page
@app.route('/')
def base():
    return render_template('base.html')

# Route for Training Mode
@app.route('/training', methods=['GET', 'POST'])
def training_mode():
    # Generate a scenario using the function from training_mode_prompt.py
    generated_scenario = generate_scenario()
    scenario = generated_scenario

    # Check if the shuffle button was clicked
    if request.method == 'POST' and 'shuffle' in request.form:
        scenario = generate_scenario()
    # Process the form for user response in Training Mode
    elif request.method == 'POST' and 'user_response' in request.form:
        user_response = request.form['user_response']
        processed_response = process_training_response(generated_scenario, user_response)

    return render_template('training_mode.html', scenario=scenario)

# Route for Assistant Mode
@app.route('/assistant', methods=['GET', 'POST'])
def assistant_mode():
    generated_response = None

    # Process the form for user input in Assistant Mode
    if request.method == 'POST' and 'user_scenario' in request.form:
        user_scenario = request.form['user_scenario']
        generated_response = generate_assistant_response(user_scenario)

    return render_template('assistant_mode.html', generated_response=generated_response)

if __name__ == '__main__':
    app.run(debug=True)
