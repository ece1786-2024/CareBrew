import openai

def call_to_API(user_response, dropdown_model):
    messages = [
        {"role": "user", "content": user_response},
        {
            "role": "system",
            "content": "Given the user's scenario above, suggest what the user can do to mitigate the situation."
            "Address the user as 'you' in your response. That is, use language such as 'Your response shows' or something of that nature."
            "Your answer should not include any bold or italicized text."
            f"At the beginning of the answer, say: {dropdown_model} is being used to generate the below response - ."
            "Please use bullet points and tables to organize the response for better readability."
        }
    ]
    
    response = openai.chat.completions.create(
        model=dropdown_model,
        messages=messages,
        temperature=1,
        top_p=1
    )
    
    return response.choices[0].message.content.strip()