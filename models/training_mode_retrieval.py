import pandas as pd
import openai

pd.set_option('display.max_colwidth', None)

def get_baseline(scenario):
    # Read the CSV file with the specified encoding
    df = pd.read_csv('models/customer_service_responses.csv', encoding='ISO-8859-1')

    prompt = f"""
    The scenario is: {scenario}

    Given the scenario, return the correct response for the scenario in each category.

    1. **Customer Type**: Regular customer, New customer, Walk-in customer, Online order customer, Returning customer
    2. **Cause Type**: Customer induced issue, Communication induced error, Employee induced error, IT induced error, Accidental issue
    3. **Issue Type**:
    Delayed Service Response
    Customer Uncertainty About Service Timing
    Slow or Inaccurate Order Fulfillment
    Unfriendly or Unhelpful Staff
    Staff Ignoring or Not Listening to Customer Requests
    Lack of Personalization in Service
    Inconsistent Quality of Food or Beverage
    Unpleasant Taste of Beverages or Food
    Temperature Issues with Coffee or Food
    Dirty or Unappealing Store Environment
    Unprofessional or Unkempt Appearance of Staff
    Inadequate Allergy or Dietary Information
    Substandard Hygiene or Safety Practices
    Confusing Loyalty Program or Promotions
    Misleading or Unclear Pricing
    Unclear Communication of Menu Choices
    Unclear or Unfriendly Return/Refund Process

    Output Format:
    Customer Type: X
    Cause Type: X
    Issue Type: X
    """

    response = openai.chat.completions.create(
        model="gpt-4",  
        messages=[
            {"role": "system", "content": "You are a customer service expert in a coffee shop setting."},
            {"role": "user", "content": prompt}  
        ],
    )

    response_text = response.choices[0].message.content.strip()
    
    #Debug message
    #print(response_text)
    #print(prompt)
    
    customer_type = None
    cause_type = None
    issue_type = None

    for line in response_text.split("\n"):
        if line.startswith("Customer Type:"):
            customer_type = line.split(":")[1].strip()
        elif line.startswith("Cause Type:"):
            cause_type = line.split(":")[1].strip()
        elif line.startswith("Issue Type:"):
            issue_type = line.split(":")[1].strip()


    try:
        # Attempt to find the matching row based on the conditions
        matching_row = df[
            (df['Customer'].str.lower() == customer_type.lower()) &
            (df['Cause'].str.lower() == cause_type.lower()) &
            (df['Issue'].str.lower() == issue_type.lower())
        ]
        
        # Extract the 'Response' column as a single string without index
        full_response = matching_row['Response'].to_string(index=False)

        # Debug messages (can be uncommented for troubleshooting)
        # print(full_response)
        # print(matching_row)

        # Return the response after cleaning
        return full_response.replace("\n", " ").strip()

    except Exception as e:
        # Return a fallback message if anything fails
        # Optionally, log the exception for debugging purposes
        # print(f"Error: {e}")
        return "no standard response"
