# Poses a meaningful question to the user after the scenario is generated
# Separate API call so as not to interfere with data retrieval
import openai

generation_prompt = {
    "role": "system",
    "content": "The goal is to generate a question that prompts the user to respond as if they were the employee in this situation."
    "Here is an example: "
    
    "Example scenario: A regular online order customer places their usual coffee order through the app, expecting pickup shortly. Due to a staff member’s oversight,"
    "the order is prepared incorrectly and a different drink is served instead. Upon realizing the error, the customer, who relies on quick service while en route to work," 
    "contacts the coffee shop. The customer's trust in the shop is shaken,"
    "and they are seeking prompt and willing assistance to rectify the mistake, testing the staff's attitude and reactivity in resolving an employee-induced error."
    
    "Example response: As the employee handling this situation, how would you address the customer's concerns about their incorrect order while ensuring they feel heard and valued?" 
    "Provide details on how you would communicate with the customer and the steps you would take to resolve the issue promptly"

    "Now given the scenario below, generate a question that prompts the user to respond as if they were the employee in this situation."
}

def call_to_API(model_prompt):
    messages = [
        generation_prompt,
        {"role": "user", "content": model_prompt}
    ]
    
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=1,
        top_p=1
    )
    
    return response.choices[0].message.content.strip()