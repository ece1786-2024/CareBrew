import openai

#This part is copy pasted from training_mode_response, but altered for the purposes of suggestions
def rate_baseline_response(generated_scenario, user_response):
    generation_prompt = f"""
    
    This is the scenario: {generated_scenario}
    This is the user's response: {user_response}
        
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
    
    # Access the response message using dot notation
    return response.choices[0].message.content.strip()


def call_to_API(generated_scenario, user_response, baseline_response, num_suggestions):
    
    baseline_grading = rate_baseline_response(generated_scenario, baseline_response)
    generation_prompt = f"""
    
    This is a customer service scenario the user is presented with: {generated_scenario}
    This is their answer on how they would react in the situation: {user_response}
    
    Given that this is the baseline response for the situation: {baseline_response}
    And this is the baseline response grading: {baseline_grading}
    
    Provide suggestions for each of the 5 categories so the user can improve their response to try and attain the highest score in each category:
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

    Please provide the output in the following structure:
    Clarity: Suggestion (Clarity rating/3)
    Reliability: Suggestion (Reliability rating/4)
    Empathy: Suggestion (Empathy rating/5)
    Relevance: Suggestion (Relevance rating/5)
    Resolution: Suggestion (Resolution rating/5)

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