import openai

generation_prompt = {
    "role": "system",
    "content": "Generate an appropriate response to the user's input scenario."
}

def call_to_API(user_response):
    messages = [
        {"role": "user", "content": user_response},
        generation_prompt
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages,
        temperature=1,
        top_p=1
    )
    
    return response.choices[0].message['content'].strip()
