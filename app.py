from flask import Flask, render_template, request
import openai
import pandas as pd
import random

app = Flask(__name__)

# Load scenarios from CSV
scenarios = pd.read_csv('scenarios.csv')['scenario'].tolist()

# Function to generate evaluation or response using OpenAI API
def generate_response(prompt, mode="evaluation"):
    model = "gpt-4" if mode == "evaluation" else "gpt-4"
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=100,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Route for the main selection page
@app.route('/')
def base():
    return render_template('base.html')

# Route for Training Mode
@app.route('/training', methods=['GET', 'POST'])
def training_mode():
    scenario = random.choice(scenarios)  # Randomly select a scenario for training
    evaluation = None

    # Check if the shuffle button was clicked
    if request.method == 'POST' and 'shuffle' in request.form:
        scenario = random.choice(scenarios)
    # Process the form for user response in Training Mode
    elif request.method == 'POST' and 'user_response' in request.form:
        user_response = request.form['user_response']
        prompt = f"Scenario: {scenario}\nUser Response: {user_response}\nEvaluate this response."
        evaluation = generate_response(prompt, mode="evaluation")

    return render_template('training_mode.html', scenario=scenario, evaluation=evaluation)

# Route for Assistant Mode
@app.route('/assistant', methods=['GET', 'POST'])
def assistant_mode():
    generated_response = None

    # Process the form for user input in Assistant Mode
    if request.method == 'POST' and 'user_scenario' in request.form:
        user_scenario = request.form['user_scenario']
        prompt = f"Provide a suitable response to this scenario: {user_scenario}"
        generated_response = generate_response(prompt, mode="response")

    return render_template('assistant_mode.html', generated_response=generated_response)

if __name__ == '__main__':
    app.run(debug=True)
