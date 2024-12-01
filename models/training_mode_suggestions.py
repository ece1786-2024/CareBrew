# Currently, when the user reads the scenario it is unclear what they are responding to
# This API call is to pose a meaningful question to the user
# It is done in a seperate API call to not ruin the flow of data retrival 


import openai

def call_to_API(generated_scenario, user_response, baseline_response, num_suggestions):
    
    generation_prompt = f"""
    
    This is a customer service scenario the user is presented with: {generated_scenario}
    This is their answer on how they would react in the situation: {user_response}
    Given that this is the baseline response for the situation: {baseline_response}
    Provide {num_suggestions} on how the user can improve their response
    """

    messages = [
        {"role": "user", "content": generation_prompt}
    ]
    
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=1,
        top_p=1
    )
    
    return response.choices[0].message.content.strip()