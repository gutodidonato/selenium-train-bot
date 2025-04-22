from openai import OpenAI

def factory_message(chave_api, usar_gpt, usar_grok, prompt_usuario="") -> str:
    client = OpenAI(
        api_key=chave_api,
        base_url="https://api.x.ai/v1",
    )

    modelo = (
        "grok-3-beta" if usar_gpt and usar_grok else
        "gpt-3.5-turbo" if usar_gpt and not usar_grok else
        "grok-3-beta" if usar_grok and not usar_gpt else
        "grok-3-beta"
    )

    completion = client.chat.completions.create(
        model=modelo,
        messages=[
            {
                "role": "system",
                "content": "Você é um sistema de avaliação e melhoramento de outros chatbots."
            },
            {"role": "user", "content": prompt_usuario}  # aqui tem que ser uma string
        ]
    )

    return completion.choices[0].message.content
