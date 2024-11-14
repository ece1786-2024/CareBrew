import openai

generation_prompt = {
    "role": "system",
    "content": "Provide feedback on how well the response addresses the given scenario."
}

def call_to_API(training_mode_prompt, user_response):
    messages = [
        {"role": "user", "content": training_mode_prompt},
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
