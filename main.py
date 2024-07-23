import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv 

# load the .env file
_ = load_dotenv(find_dotenv())
client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)

def generate_prompt(reciever, topic):
    prompt = f"""
    As a professional email writer write an email to '{reciever}' in a poetic but in professional manner
    where subject will be related'{topic}' 
    """
    return prompt 


model = "gpt-4o-mini"
temperature = 1.0
max_token = 500
topic = ""
reciever = ""

system_message = """
    You are the professtional email write, who is specialize to write the email in poetic cum professtional manner
    your today's task is to help others to write a email with the help of given dataset.
"""
prompt = generate_prompt(reciever, topic)


messages = [
    {"role":"system", "content":"You are the helpfull doctor to suggest medicaation related deceases."},
    {"role":"user", "content": "As a daibetic patient i am really concerned about my health and want your assistance on getting my medication from you"}
]

def gen_email():
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_token
    )
    return completion.choices[0].message

print(gen_email())