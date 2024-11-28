from openai import OpenAI
client = OpenAI()

system_prompt = [{
    "role": "system",
    "content": [
            {
                "type": "text",
                "text": """
                Given the scenario and the user's response, the goal is to analyze the user's response.
                Begin by acknowledge what the user did well. Then suggest on what they can improve on.
                Address the user as 'you' in your response. That is, use language such as 'Your response shows' or something of that nature.
                Your answer should not include any bold or italicized text.
                """
            }
    ]
}]


def call_to_API(chat_session, assistant_prompt, user_response, temperature=1, top_p=1, frequency_penalty=0, presence_penalty=0):
    chat_session = chat_session + [
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": assistant_prompt
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": user_response
                }
            ]
        },
    ]
    messages = system_prompt + chat_session
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )

    return response.choices[0].message.content.strip(), chat_session
