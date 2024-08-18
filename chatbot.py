import os
import openai

# Replace 'your-api-key-here' with your actual API key
api_key = "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"

client = openai.OpenAI(api_key=api_key)

while True:
    question = input('What is your question (type "quit" to exit): ')

    if question.lower() == 'quit':
        break

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a chatbot"},
                {"role": "user", "content": f"{question}"},
            ]
        )

    result = ''
    for choice in response.choices:
        result += choice.message.content

    print(f"We asked ChatGPT: {question} - Here is their answer:")
    print("-----------------------------------------------------------------")
    print(result)
