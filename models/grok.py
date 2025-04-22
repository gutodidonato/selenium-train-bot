from openai import OpenAI
from main import CHAVE_API, grok

model: str = "grok-3-beta" if grok else "gpt-3.5"



def factory_message(model = "grok-3-beta", content= "") -> str:
    client = OpenAI(
    api_key=CHAVE_API,
    base_url="https://api.x.ai/v1",
    )

    completion = client.chat.completions.create(
    model="grok-3-beta",
    messages=[
        {
            "role": "system",
            "content": "Você é um sistema de avaliação e melhoramento de outros chatbots."
        },
        {"role": "user", "content": content}
    ]
    )
    message = completion.choices[0].message.content
    return message
    
    

    
    