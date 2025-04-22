from openai import OpenAI

def factory_message(chave_api, usar_gpt, usar_gemini, prompt_usuario="") -> str:
    client = OpenAI(
        api_key=chave_api,
        base_url="https://api.x.ai/v1",
    )

    modelo = (
        "gemini-2.0-flash" if usar_gpt and usar_gemini else
        "gpt-3.5-turbo" if usar_gpt and not usar_gemini else
        "gemini-2.0-flash" if usar_gemini and not usar_gpt else
        "gemini-2.0-flash"
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
