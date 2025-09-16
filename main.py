import os
from openai import OpenAI


def main():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a English leaning helper."},
            {"role": "user", "content": (
                "Please make a TOEIC like question using word 'aggravate'."
                "Including 4 answer options."
            )},
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
