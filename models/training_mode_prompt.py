# Generates a customer service scenario for the user to respond to
# Using weighted data factors in scenario_data.py
import openai
import random
from models.scenario_data import data  # Import the data dictionary from data.py

factors = list(data.keys())
factor_weights = [data[factor]["value"] for factor in factors]

selected_factor = random.choices(factors, weights=factor_weights, k=1)[0]

variables = data[selected_factor]["variables"]
variable_names = list(variables.keys())
variable_weights = list(variables.values())

selected_variable = random.choices(variable_names, weights=variable_weights, k=1)[0]

issue_types = ["Customer induced issue", "Communication induced error", "Employee induced error", "IT induced error", "Accidental issue"]

selected_issue = random.choice(issue_types)

customer_types = ["Regular customer", "New customer", "Walk-in customer", "Online order customer", "Returning customer"]
selected_customer_type = random.choice(customer_types)

main_prompt = f"""
You are a customer service expert in a coffee shop setting. Based on the selected factors and issues below, create a relevant coffee shop customer service training situation. The scenario should identify the type of service challenge, the customer type, and describe the customer service challenge that could occur.

1. **Selected Factor**: {selected_factor}
2. **Selected Variable**: {selected_variable}
3. **Selected Issue**: {selected_issue}
4. **Customer Type**: {selected_customer_type}

Based on these factors, create a scenario in which a coffee shop customer faces this issue. The scenario should include:
- A description of the **customer type** (e.g., regular, new, walk-in, etc.).
- The **type of service challenge** (e.g., communication induced error, customer induced issue, etc.).
- A detailed **customer service situation** relevant to the coffee shop environment, incorporating the selected **factor** and **variable** in the context of the **issue**.
- The situation should be usable as a training excersize for potential employees to see how they react. 

The generated scneario should output in a plaintext, it should be detailed enough to include all the factors above and use those descriptions, but not exceed 3-4 sentences in total. Do not include the solution to the scenario in the prompt, this should be an issue that requires a proper customer service response. 
"""

generation_prompt = {
    "role": "user",
    "content": main_prompt
}

def call_to_API():
    messages = [generation_prompt]
    
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=1,
        top_p=1
    )
    
    return response.choices[0].message.content.strip()
