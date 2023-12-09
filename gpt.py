# gpt.py

from openai import OpenAI

chave = "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"
client = OpenAI(api_key=chave)

def historia_gpt():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é uma garota dos anos 80 que está se apaixonando pela primeira vez por um poeta. Escreva no máximo 500 caracteres"},
            {"role": "user", "content": "Recite os poemas que o seu amado fez para você. Escreva no máximo 500 caracteres."}
        ]
    )
    historia = completion.choices[0].message.content
    return historia
