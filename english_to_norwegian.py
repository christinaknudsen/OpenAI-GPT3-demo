# -*- coding: utf-8 -*-
import openai
from dotenv import load_dotenv
import os
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


prompt= '''English: I do not speak Norwegian.
Norsk: Jeg snakker ikke norsk.

English: See you later!
Norsk: Snakkes!

English: Where is a good restaurant?
Norsk: Hvor kan jeg finne en god restaurant?

English: What rooms do you have available?
Norsk: Hvilke rom er ledige?

English: What is the time?
Norsk: Hva er klokken?

English: '''

def gpt3(prompt, engine='davinci', response_length=64,
         temperature=0.7, top_p=1, frequency_penalty=0, presence_penalty=0,
         start_text='', restart_text='', stop_seq=[]):
    response = openai.Completion.create(
        prompt=prompt + start_text,
        engine=engine,
        max_tokens=response_length,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop_seq,
    )
    answer = response.choices[0]['text']
    new_prompt = prompt + start_text + answer + restart_text
    return answer, new_prompt


def translate(prompt):
    print ('')
    print ('Write a text in English that you want translated into Norwegian')
    print ('')

    while True:
        prompt += input('English: ')
        answer, prompt = gpt3(prompt,
                              temperature=0.5,
                              frequency_penalty=0,
                              presence_penalty=0,
                              start_text='\nNorsk:',
                              restart_text='English: ',
                              #response_length=100,
                              stop_seq=['English: ', '\n'])
        print('Norsk: ' + answer)
translate(prompt)
