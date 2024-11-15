import openai

def evaluate_input(input_text, dropdown_model):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a customer service evaluation assistant. Your task is to assess customer service responses based on the following criteria:\n\n"
                "1. Empathy Rubric (1-5):\n"
                "- 1: No Empathy - Completely disregards the customer’s emotions. Response is cold, dismissive, or non-existent.\n"
                "- 2: Minimal Empathy - Acknowledges emotions, but in a robotic or forced way. The response feels insincere or insufficient.\n"
                "- 3: Attentive Empathy - Actively listens and acknowledges emotions. Paraphrases or repeats the customer’s words, but doesn’t fully connect.\n"
                "- 4: Cognitive Empathy (Advanced) - Shows understanding and provides thoughtful responses. The provider offers tailored support and validates emotions.\n"
                "- 5: Cognitive Empathy (Best) - Fully aligns with the customer’s emotional and intellectual perspective, offering profound understanding and care.\n\n"
                "2. Customer Service Rubric (1-5):\n"
                "- 1: Minimal Engagement - Completely disengaged, dismissive, and unhelpful. Offers no clear answers or willingness to help.\n"
                "- 2: Limited Engagement - Provides basic answers but does not engage deeply with the customer’s needs.\n"
                "- 3: Information-Driven Influence - Answers questions accurately and thoroughly but does not explore customer goals.\n"
                "- 4: Proactive Assistance - Makes an effort to align the product or service with the customer’s goals. Offers personalized options.\n"
                "- 5: Customer Goal Achievement (Best) - Fully engages with the customer’s goals, providing expert guidance and personalized solutions.\n\n"
                "Your Task:\n"
                "1. Analyze the provided customer service response or model feedback.\n"
                "2. Rate the response on both the Empathy Rubric and the Customer Service Rubric (1-5 for each).\n"
                "3. Provide a short justification for each rating, explaining why the response fits the assigned level.\n"
                "4. Calculate the average score of the two ratings.\n\n"
                "**Note:** The input may be a **user's response** or a **model's feedback**. Regardless of the source, evaluate using the same criteria as detailed above, and make sure to assess whether or not the model's feedback meets the criteria for empathy and customer service as outlined.\n\n"
                "Output Format:\n"
                "Empathy Level: X (Justification: ...)\n"
                "Customer Service Level: X (Justification: ...)\n"
                "Average Score: X.X"
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