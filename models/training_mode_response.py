import openai

generation_prompt = {
    "role": "system",
    "content": "Given the scenario and the user's response, the goal is to analyze the user's response."
    "Begin by acknowledge what the user did well. Then suggest on what they can improve on." 
    "Address the user as 'you' in your response. That is, use language such as 'Your response shows' or something of that nature."
    "Your answer should not include any bold or italicized text."
}

def call_to_API(training_mode_prompt, user_response):
    messages = [
        {"role": "assistant", "content": "Scenario: " + training_mode_prompt},
        {"role": "user", "content": "User response: " + user_response},
        generation_prompt
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages,
        temperature=1,
        top_p=1
    )
    
    return response.choices[0].message['content'].strip()
