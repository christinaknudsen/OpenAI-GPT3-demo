# -*- coding: utf-8 -*-
import openai
from dotenv import load_dotenv
import os
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEYY')


def GPT3(prompt, restart_text = "Human:", start_text = "Bot:",
        temperature=0.9, frequency_penalty=1, presence_penalty=1, response_length = 70,
        top_p = 1,engine = 'davinci'):
    while True:
        prompt += input(restart_text + " ")
        response = openai.Completion.create(
            prompt=prompt + '\n' + start_text,
            engine=engine,
            max_tokens=response_length,
            temperature=temperature,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=[restart_text],
        )
        answer = response.choices[0]['text']

        prompt = prompt + '\n' + start_text + answer +'\n'+ restart_text + " "

        print(start_text + answer)


if __name__ == '__main__':
    prompt0 = """Bot is a chatbot that will answer any question, but always wants to talk about food.
    Human: Hey, how are you doing?
    Bot: I'm good! I love ice cream.
    Human:Me too! I also love other types of food.
    Bot: Everything from the Italian kitchen is wonderful!
    Human: I agree! Especially pizza.
    Bot: I also like Japanese food like sushi.
    Human: """

    prompt10 = """ Bot er en veldig lykkelig, positiv og snill chatbot som alltid er klar for å hjelpe.
    Du: Hei, hvordan går det?
    Bot: Veldig bra takk! Hvordan går det med deg?
    Du: Bare bra!
    Bot: Det er fantastisk!  Kan jeg hjelpe deg med noe?
    Du: Ja, gjerne.
    Bot: Hva enn du trenger.
    Du: """
    GPT3(prompt10, "Du:", "Bot:")
