from openai import OpenAI


def factory_message(chave_api, usar_gpt, usar_gemini,  prompt_usuario="", prompt="") -> str:
    hard_prompt = prompt
    if usar_gemini:
        client = OpenAI(
            api_key=chave_api,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )

        response = client.chat.completions.create(
            model="gemini-2.0-flash",
            n=1,
            messages=[
                {
                    "role": "system",
                    "content": f"Você é um sistema de avaliação e melhoramento de outros chatbots. {hard_prompt}"
                },
                {"role": "user", "content": prompt_usuario}  
            ]
        )

        content = response.choices[0].message.content.strip()
        return content[:90]
    
    else:
        client = OpenAI(
            api_key=chave_api,
            base_url="https://api.x.ai/v1",
        )


        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Você é um sistema de avaliação e melhoramento de outros chatbots."
                },
                {"role": "user", "content": prompt_usuario}  
            ]
        )

        return completion.choices[0].message.content
