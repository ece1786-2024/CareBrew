import random
import openai

data = {
    "Trust and Reactivity": {
        "value": 10.873,
        "variables": {
            "Faithfully treating service customer demanded": 0.732,
            "Responding immediately to customer's question": 0.726,
            "Providing rapid service in order of visiting customer": 0.708,
            "Keeping promise made by customers": 0.706,
            "Workers responding immediately to customer's demands": 0.648,
            "Attitude to help customers willingly": 0.644,
            "Treating customer's demand accurately": 0.628,
            "Trust towards raw materials and cooking procedures": 0.567
        }
    },
    "Assurance and Sympathy": {
        "value": 1.931,
        "variables": {
            "Deep interest towards individual customers": 0.81,
            "Accomplishing faithfully to customer's demand": 0.756,
            "Carrying out service with sympathy": 0.702,
            "Being friendly and thoughtful": 0.642,
            "Understanding customer's needs and emotion": 0.642,
            "Being safe from all situation such as fire": 0.626,
            "Trust towards hygiene and safety": 0.6,
            "Skill to make coffee and beverage well": 0.472
        }
    },
    "Taste": {
        "value": 1.483,
        "variables": {
            "Taste of beverages": 0.831,
            "Taste of foods excluding coffee and beverages": 0.807,
            "Tasty product overall": 0.803,
            "Taste of coffee": 0.766
        }
    },
    "Materiality": {
        "value": 1.267,
        "variables": {
            "Facilities and equipment": 0.824,
            "Store atmosphere including interior": 0.73,
            "Physical Environment": 0.671,
            "Attire and appearance of workers": 0.626
        }
    }
}



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

prompt = f"""
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

Give me a less than 2 sentences description of the scenario that includes all the information above. 
"""

response = openai.chat.completions.create(
    model="gpt-4",  
    messages=[
        {"role": "system", "content": "You are a customer service expert in a coffee shop setting."},
        {"role": "user", "content": prompt}  
    ],
    max_tokens=200
)

print(response.choices[0].message.content.strip())
