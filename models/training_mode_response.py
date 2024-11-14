import openai

generation_prompt = (
    "something"
)

def call_to_API(training_mode_prompt, user_response):
    messages = [
        training_mode_prompt, 
        user_response,
        generation_prompt
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages,
        temperature=1,
        top_p=1
    )
    
    return response.choices[0].message['content'].strip()

training_mode_prompt = "I was sad because my coffe was cold"
user_response = "Let me make you a new one"

response = call_to_API(training_mode_prompt, user_response)