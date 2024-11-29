from flask import Flask, render_template, request, session
import openai
import pandas as pd

# Import functions from the modules
from models.training_mode_prompt import call_to_API as generate_scenario
from models.training_mode_response import call_to_API as process_training_response

app = Flask(__name__)
app.secret_key = '1A2B3C4D5E'

# Route for the main selection page
@app.route('/')
def base():
    return render_template('base.html')

# Route for Training Mode
@app.route('/training', methods=['GET', 'POST'])
def training_mode():
    if request.method == 'POST' and 'generated_scenario' in session:
        generated_scenario = session['generated_scenario']
    else:
        # Generate a scenario using the function from training_mode_prompt.py
        generated_scenario = generate_scenario()
        session['generated_scenario'] = generated_scenario
        # processed_response = None  # Initialize processed_response to avoid UnboundLocalError

    # Check if the shuffle button was clicked
    if request.method == 'GET' and 'shuffle' in request.form:
        generated_scenario = generate_scenario()
        session['generated_scenario'] = generated_scenario

    # Process the form for user response in Training Mode
    elif request.method == 'POST' and 'user_response' in request.form:
        user_response = request.form['user_response']
        processed_response = process_training_response(generated_scenario, user_response)
        if 'save_data' in request.form:
            df = pd.read_csv('training_responses.csv')
            new_record = {'generated_scenario': generated_scenario, 'user_response': user_response, 'processed_response': processed_response}
            df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
            df.to_csv('training_responses.csv', index=False)
        return render_template('training_mode_response.html', scenario=generated_scenario, user_response=user_response, processed_response=processed_response)

    return render_template('training_mode_base.html', scenario=generated_scenario)


if __name__ == '__main__':
    app.run(debug=True)
