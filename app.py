from flask import Flask, render_template, request, session
import openai
import pandas as pd
import json

# Import functions from the modules
from models.training_mode_prompt import call_to_API as generate_scenario
from models.training_mode_prompt_user_question import call_to_API as generate_user_question
from models.training_mode_retrieval import get_baseline as retrieve_baseline
from models.training_mode_response import call_to_API as process_training_response
from models.training_mode_suggestions import call_to_API as generate_suggestions

app = Flask(__name__)
app.secret_key = '1A2B3C4D5E'

# Route for the main selection page (Base Page)
@app.route('/')
def base():
    # Clear the session data when visiting the base page
    session.clear()  # Clears the entire session when the base page is accessed
    return render_template('base.html')


@app.route('/training', methods=['GET', 'POST'])
def training_mode():
    if request.method == 'POST' and 'generated_scenario' in session:
        generated_scenario = session['generated_scenario']
        user_question = ['user_question']
        baseline_response = retrieve_baseline(generated_scenario)
        session['base_line_response'] = baseline_response

    else:
        # Generate a scenario using the function from training_mode_prompt.py
        session.clear()
        generated_scenario = generate_scenario()
        session['generated_scenario'] = generated_scenario
        user_question = generate_user_question(generated_scenario)
        session['user_question'] = user_question
        baseline_response = retrieve_baseline(generated_scenario)
        session['base_line_response'] = baseline_response

    # Initialize chat session variables
    chat_session = session.get('chat_session', [])
    chat_session_text = session.get('chat_session_text', '')
    model_response = session.get('model_response', '')

    # Check if the shuffle button was clicked
    if request.method == 'POST' and 'shuffle' in request.form:
        session.clear()  # Clears the entire session when shuffle button is clicked
        generated_scenario = generate_scenario()
        session['generated_scenario'] = generated_scenario
        user_question = generate_user_question(generated_scenario)
        session['user_question'] = user_question
        baseline_response = retrieve_baseline(generated_scenario)
        session['base_line_response'] = baseline_response

    # Process user response in Training Mode
    elif request.method == 'POST' and 'user_response' in request.form:
        user_response = request.form['user_response']
        num_suggestions = int(request.form['number_response'])
        model_response, chat_session = process_training_response(chat_session, generated_scenario, user_response)
        suggestions = generate_suggestions(generated_scenario, user_response, baseline_response, num_suggestions)
        chat_session_text = process_chat_session(chat_session)
        session['chat_session'] = chat_session
        session['chat_session_text'] = chat_session_text
        session['model_response'] = model_response

        # Save data to CSV if requested
        if 'save_data' in request.form:
            save_training_data(generated_scenario, user_response, model_response)

        return render_template(
            'training_mode_response.html',
            scenario=generated_scenario,
            question=user_question,
            chat_session_text=chat_session_text,
            model_response=json_to_df_html(model_response),
            model_suggestion=suggestions
        )

    elif request.method == 'POST' and 'user_input' in request.form:
        user_input = request.form['user_input']
        num_suggestions = int(request.form['number_response'])
        model_response, chat_session = process_training_response(chat_session, model_response, user_input)
        suggestions = generate_suggestions(generated_scenario, user_response, baseline_response, num_suggestions)
        chat_session_text = process_chat_session(chat_session)
        session['chat_session'] = chat_session
        session['chat_session_text'] = chat_session_text
        session['model_response'] = model_response

        return render_template(
            'training_mode_response.html',
            scenario=generated_scenario, 
            question=user_question,
            chat_session_text=chat_session_text,
            model_response=json_to_df_html(model_response),
            model_suggestion=suggestions
        )

    return render_template('training_mode_base.html', scenario=generated_scenario, question=user_question)

def json_to_df_html(json_str: str) -> str:
    try:
        structured_data = json.loads(json_str)
        df = pd.DataFrame(structured_data)
        df_html = df.to_html(classes='table table-striped', index=False) 
        return df_html
    except json.JSONDecodeError as e:
            print("Failed to parse response:", e)

def process_chat_session(chat_session: list) -> str:
    """
    Process the chat session and return a formatted HTML string.
    """
    conversation = ""
    first_carebrew_response = True  

    for entry in chat_session:
        # Access content dynamically based on type
        if isinstance(entry["content"], str):
            text = entry["content"]
        elif isinstance(entry["content"], list) and "text" in entry["content"][0]:
            text = entry["content"][0]["text"]
        else:
            text = "Invalid content format"

        # Format conversation based on role
        if entry['role'] == 'assistant':
            if first_carebrew_response:
                conversation += f"<br><strong>Scenario</strong>: {text}<br>\n"
                first_carebrew_response = False
            else:
                conversation += f"<br><strong>Past Grading</strong>: <br>\n"
                conversation += json_to_df_html(text)
        else:
            conversation += f"<br><strong>User response</strong>: {text}<br>\n"

    return conversation


def save_training_data(scenario, user_response, model_response):
    """
    Save training data to a CSV file.
    """
    try:
        # Load existing data if the file exists
        try:
            df = pd.read_csv('training_responses.csv')
        except FileNotFoundError:
            df = pd.DataFrame(columns=['generated_scenario', 'user_response', 'processed_response'])

        # Append new record
        new_record = {
            'generated_scenario': scenario,
            'user_response': user_response,
            'processed_response': model_response
        }
        df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)

        # Save to CSV
        df.to_csv('training_responses.csv', index=False)
    except Exception as e:
        print(f"Error saving data: {e}")


if __name__ == '__main__':
    app.run(debug=True)
