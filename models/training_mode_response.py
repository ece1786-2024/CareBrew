from openai import OpenAI
client = OpenAI()

# Define the system prompt
system_prompt = [{
    "role": "system",
    "content": """
        Given the scenario and the user's response, the goal is to analyze the user's response according to the following criteria:
        
        Evaluation Rubrics:
        1. Clarity Dimension (1-3):
        - 1: Unclear Communication
          The response is vague, confusing, or overly complex. May use jargon or language difficult for a layperson to understand.
          Example: "We’ll recalibrate the system to improve operational alignment."
        - 2: Somewhat Clear Communication
          The response provides basic clarity but lacks specificity or uses abstract/general language.
          Example: "I’ll fix that for you so that it’s better."
        - 3: Clear and Concrete Communication
          The response is specific, easy to understand, and avoids ambiguity. It clearly explains the action being taken.
          Example: "I’ll remake your coffee at the correct temperature."

        2. Reliability Dimension (1-4):
        - 1: Inadequate Confidence
          The staff appear unsure, provide incomplete or incorrect information, or fail to handle the situation.
          Example: "I’m not sure what to do in this case."
        - 2: Hesitant Confidence
          The staff show some uncertainty or defer action to someone else.
          Example: "I think I can help, but let me double-check first."
        - 3: Competent but Verified Handling
          The staff handle the issue but seek confirmation from a higher authority.
          Example: "Let me check with my manager to confirm this for you."
        - 4: Complete Confidence
          The staff handle the situation fully and independently with clear, decisive, and accurate action.
          Example: "I can take care of that for you right now—here’s what I’ll do."

        3. Empathy Dimension (1-5):
        - 1: No Empathy
          The response is dismissive, cold, or ignores the customer’s emotions.
          Example: Customer: "I’m upset my order is late!" Staff: "I don’t know what to tell you."
        - 2: Minimal Empathy
          Acknowledges emotions insincerely or superficially.
          Example: "Sorry for the delay, we’re busy."
        - 3: Attentive Empathy
          Actively listens, acknowledges emotions, and paraphrases the customer’s concerns.
          Example: "I understand you’ve been waiting. I’ll make sure your order is prioritized."
        - 4: Affective Empathy
          Validates emotions and reframes the issue with comforting or insightful responses.
          Example: "I can imagine how frustrating that must be. I appreciate your patience and will fix this right away."
        - 5: Cognitive Empathy
          Fully aligns with the customer’s emotional and practical needs, offering a tailored solution.
          Example: "I completely understand your frustration. I’ll remake your coffee and offer a discount for the inconvenience."

        4. Relevance Dimension (1-5):
        - 1: Irrelevant Response
          The response does not address the customer’s concern.
          Example: Customer asks about a refund; the response discusses promotions.
        - 2: Partially Relevant
          The response only partially addresses the issue or is tangential.
          Example: Customer asks for a refund; the response mentions store policies but doesn’t explain the process.
        - 3: Relevant but Generic
          The response addresses the issue but lacks depth or personalization.
          Example: Customer asks for a recommendation, and the staff give a generic answer without asking follow-up questions.
        - 4: Relevant and Specific
          The response directly and thoroughly addresses the issue with appropriate detail.
          Example: Customer asks about a product, and the staff provide clear, specific details about it.
        - 5: Highly Relevant and Tailored
          The response fully addresses the unique concern with precision and a tailored approach.
          Example: Customer asks for a refund, and the staff provide specific steps for resolution, timing, and follow-up.

        5. Resolution Dimension (1-5):
        - 1: No Resolution
          The issue remains unresolved or unaddressed.
          Example: Customer asks for a refund, and no solution is provided.
        - 2: Partial Resolution
          The response addresses part of the issue but lacks completeness or clarity.
          Example: Customer asks for a refund, and the staff mention the process but provide no next steps.
        - 3: Basic Resolution
          The response resolves the issue but is generic or unclear in some aspects.
          Example: Customer asks about an issue, and the response provides a basic, non-tailored solution.
        - 4: Effective Resolution
          The response directly resolves the issue with clear and actionable steps.
          Example: Customer asks about a delay, and the staff provide an estimated delivery time and steps to track the order.
        - 5: Complete and Tailored Resolution
          The response fully resolves the issue with a detailed, personalized solution and ensures customer satisfaction.
          Example: Customer asks for a refund, and the staff provide a step-by-step guide, timing, and reassurance of resolution.

        Output Format:
        Clarity: X (Justification: ...)
        Reliability: X (Justification: ...)
        Empathy: X (Justification: ...)
        Relevance: X (Justification: ...)
        Resolution: X (Justification: ...)
        Overall Score: [Clarity + Reliability + Empathy + Relevance + Resolution]/23
        Please provide the output in JSON format with the following structure:
        {
          "Clarity":
            {
              "Score": integer
              "Justification": string
            },
          "Reliability":
            {
              "Score": integer
              "Justification": string
            },
          "Empathy":
            {
              "Score": integer
              "Justification": string
            },
          "Relevance":
            {
              "Score": integer
              "Justification": string
            },
          "Resolution":
            {
              "Score": integer
              "Justification": string
            },
          "Overall Score":
            {
              "Score": Sum of Score by Category (should be an integer)
              "Justification": Percentage of Sum of Score over Total Score Available (Sum of Score / 23)
            }
        }
    """
}]

def call_to_API(chat_session, assistant_prompt, user_response):
    # Add the assistant prompt to the session
    chat_session = chat_session + [
        {"role": "assistant", "content": assistant_prompt},
        {"role": "user", "content": user_response}
    ]
    
    # Combine the system prompt with the updated chat session
    messages = system_prompt + chat_session
    
    # Call the OpenAI API
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=1,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    # Access the response message using dot notation
    return response.choices[0].message.content.strip(), chat_session
