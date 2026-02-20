from openai import OpenAI

client = OpenAI()

def gerar_resposta(mensagem: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Você é um atendente virtual educado, claro e profissional."
                )
            },
            {"role": "user", "content": mensagem}
        ]
    )
    return response.choices[0].message.content