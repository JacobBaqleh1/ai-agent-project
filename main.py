import os   
from dotenv import load_dotenv
from openai import OpenAI 

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise RuntimeError("OPENROUTER_API_KEY environment variable not found")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

response = client.chat.completions.create(
    model='openrouter/free',
    messages=[
        {
"role": "user",
"content": "Why is the sky blue"
        }
    ],
)
if response.usage is None:
    raise RuntimeError("API request failed: usage metadata missing")
print(f"Prompt tokens:{response.usage.prompt_tokens}")    
print(f"Response tokens: {response.usage.completion_tokens}")
print(response.choices[0].message.content)