import openai

generation_prompt = (
    "something"
)

def call_to_API(user_response):
    messages = [
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

user_response = "I was having trouble at work today..."

response = call_to_API( user_response)