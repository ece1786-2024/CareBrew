import openai

generation_prompt = {
    "role": "user",
    "content": "Generate a coffee shop customer service scenario. The scenario should be no more than 1 to 3 sentences long."
    "After generating the scenario, add 'How would you react to this situation?'"
}

def call_to_API():
    messages = [generation_prompt]
    
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages,
        temperature=1,
        top_p=1
    )
    
    return response.choices[0].message['content'].strip()
