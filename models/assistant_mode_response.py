import openai

generation_prompt = {
    "role": "system",
    "content": "Given the user's scenario above, suggest what the user can do to mitigate the situation."
    "Address the user as 'you' in your response. That is, use language such as 'Your response shows' or something of that nature."
    "Your answer should not include any bold or italicized text."
}

def call_to_API(user_response):
    messages = [
        {"role": "user", "content": user_response},
        generation_prompt
    ]
    
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=1,
        top_p=1
    )
    
    return response.choices[0].message.content.strip()