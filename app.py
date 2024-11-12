from flask import Flask, render_template, request
import openai
import pandas as pd
import random

app = Flask(__name__)

# Configure OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

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

# Single route to render both modes
@app.route('/', methods=['GET', 'POST'])
def base():
    scenario = random.choice(scenarios)  # Randomly select a scenario for training
    evaluation = None
    generated_response = None

    # Check if the shuffle button was clicked
    if request.method == 'POST' and 'shuffle' in request.form:
        scenario = random.choice(scenarios)
    # Process the form for Training Mode
    elif request.method == 'POST' and 'user_response' in request.form:
        user_response = request.form['user_response']
        prompt = f"Scenario: {scenario}\nUser Response: {user_response}\nEvaluate this response."
        evaluation = generate_response(prompt, mode="evaluation")

    # Process the form for Assistant Mode
    elif request.method == 'POST' and 'user_scenario' in request.form:
        user_scenario = request.form['user_scenario']
        prompt = f"Provide a suitable response to this scenario: {user_scenario}"
        generated_response = generate_response(prompt, mode="response")

    return render_template('base.html', scenario=scenario, evaluation=evaluation, generated_response=generated_response)

if __name__ == '__main__':
    app.run(debug=True)
