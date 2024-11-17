import openai

def evaluate_input(input_text, dropdown_model):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a customer service evaluation assistant. Your task is to assess customer service responses based on the following criteria:\n\n"
                "Customer Service Empathy Rubric (1-5):\n"
                "- 1: No Empathy - Completely disregards the customer’s emotions. The response is cold, dismissive, or non-existent. The service provider shows no interest in the customer’s needs or concerns.\n"
                "- 2: Minimal Empathy - Acknowledges emotions, but in a robotic or forced way. The response feels insincere or insufficient. The provider does not actively address the customer’s needs or goals.\n"
                "- 3: Attentive Empathy - Actively listens and acknowledges emotions. Paraphrases or repeats the customer’s words. The provider engages with the customer’s goals, but the response remains surface-level.\n"
                "- 4: Affective Empathy - Shows understanding of both the emotional and practical aspects of the customer's situation. The response offers insight and begins to address the customer’s goals.\n"
                "- 5: Cognitive Empathy - Fully aligns with the customer’s emotional and intellectual perspective. The response offers personalized, expert guidance, ensuring that the customer's goals are fully met.\n\n"
                "Your Task:\n"
                "1. Analyze the provided customer service response or model feedback.\n"
                "2. Rate the response on the Customer Service Empathy Rubric (1-5).\n"
                "3. Provide a short justification for the rating, explaining why the response fits the assigned level.\n\n"
                "Note: The input may be a user's response or a model's feedback. Regardless of the source, evaluate using the same criteria as detailed above, and make sure to assess whether or not the response demonstrates an understanding of both the customer’s emotional state and their goals.\n\n"
                "Output Format:\n"
                "Empathy Level: X (Justification: [one sentence])"
            ),
        },
        {"role": "user", "content": input_text},
    ]

    response = openai.chat.completions.create(
        model=dropdown_model,
        messages=messages,
        temperature=1,
        top_p=1
    )

    return response.choices[0].message.content.strip()