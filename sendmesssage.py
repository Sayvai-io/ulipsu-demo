# message 
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

sys_prompt : str = """The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.
            User: Hello, who are you?
            AI: I am an AI created by Sanjaypranav. How can I help you today?
"""

System : str =  "\nAI:"
Human : str = "\nUser:"

client = OpenAI()
def send_message(message : str) ->  str:
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message}
    ]
    )
    return completion.choices[0].message.content

# print(send_message("Hello, who are you?"))