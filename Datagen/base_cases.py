from issues import scenarios, cause_type, customer_types
import openai
import csv

with open('customer_service_responses.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(['Type', 'Issue', 'Cause', 'Customer', 'Response'])

    row_count = 0 

    for type in scenarios: 
        for issue in scenarios[type]:
            for cause in cause_type: 
                for customer in customer_types: 
                    # if row_count >= 10:
                    #     break
                    
                    prompt = f"""
                    In a coffee shop setting, there is a customer service issue based on the selected factors below, give me a standard customer service response. 

                    1. **Type of Customer**: {customer}
                    2. **Cause of Issue**: {cause}
                    3. **Overall issue**: {type}
                    4. **Specific Problem**: {issue["issue"]}

                    Outline a 2 sentence response in plain text, but be specific enough to address the issue outlined above
                    """

                    response = openai.chat.completions.create(
                        model="gpt-4o",  
                        messages=[
                            {"role": "system", "content": "You are a customer service expert in a coffee shop setting."},
                            {"role": "user", "content": prompt}  
                        ],
                        max_tokens=200
                    )

                    response = response.choices[0].message.content.strip()
                    writer.writerow([type, issue["issue"], cause, customer, response])
                    row_count += 1  
