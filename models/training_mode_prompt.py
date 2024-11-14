import openai

generation_prompt = (

    "something"
)


def call_to_API():
    messages = [
        generation_prompt
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages,
        temperature=1,
        top_p=1
    )
    
    return response.choices[0].message['content'].strip()

response = call_to_API