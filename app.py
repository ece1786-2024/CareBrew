from flask import Flask, render_template, request, session
import pandas as pd

# Import functions from the modules
from models.training_mode_prompt import call_to_API as generate_scenario
from models.training_mode_retrieval import get_baseline as retrieve_baseline
from models.training_mode_response import call_to_API as process_training_response

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
        baseline_response = retrieve_baseline(generated_scenario)
        session['base_line_response'] = baseline_response
    else:
        # Generate a scenario using the function from training_mode_prompt.py
        session.clear()
        generated_scenario = generate_scenario()
        session['generated_scenario'] = generated_scenario
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
        baseline_response = retrieve_baseline(generated_scenario)
        session['base_line_response'] = baseline_response

    # Process user response in Training Mode
    elif request.method == 'POST' and 'user_response' in request.form:
        user_response = request.form['user_response']
        number_response = int(request.form['number_response'])
        model_response, chat_session = process_training_response(chat_session, generated_scenario, user_response, number_response)
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
            chat_session_text=chat_session_text,
            model_response=model_response,
            number_response=number_response
        )

    elif request.method == 'POST' and 'user_input' in request.form:
        user_input = request.form['user_input']
        number_response = int(request.form['number_response'])
        selected_model_response = int(request.form['selected_model_response'])
        print(selected_model_response)
        model_response = model_response[selected_model_response-1]
        model_response, chat_session = process_training_response(chat_session, model_response, user_input, number_response)
        chat_session_text = process_chat_session(chat_session)
        session['chat_session'] = chat_session
        session['chat_session_text'] = chat_session_text
        session['model_response'] = model_response

        return render_template(
            'training_mode_response.html',
            scenario=generated_scenario,
            chat_session_text=chat_session_text,
            model_response=model_response,
            number_response=number_response
        )

    return render_template('training_mode_base.html', scenario=generated_scenario)


def process_chat_session(chat_session: list) -> str:
    """
    Process the chat session and return a formatted HTML string.
    """
    conversation = ""
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
            conversation += f"<br><strong>CareBrew</strong>: {text}<br>\n"
        else:
            conversation += f"<br><strong>User</strong>: {text}<br>\n"
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
