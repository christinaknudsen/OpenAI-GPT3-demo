# -*- coding: utf-8 -*-
import openai
from dotenv import load_dotenv
import os
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

prompt_eng = '''I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with "Unknown".

Question: What is human life expectancy in the United States?
Answer: Human life expectancy in the United States is 78 years.

Question: Who was president of the United States in 1955?
Answer: Dwight D. Eisenhower was president of the United States in 1955.

Question: Which party did he belong to?
Answer: He belonged to the Republican Party.

Question: What is the square root of banana?
Answer: Unknown

Question: How does a telescope work?
Answer: Telescopes use lenses or mirrors to focus light and make objects appear closer.

Question: Where were the 1992 Olympics held?
Answer: The 1992 Olympics were held in Barcelona, Spain.

Question: How many squigs are in a bonk?
Answer: Unknown

Question:'''

prompt_nor = '''Jeg er en meget intelligent spørsmål-svar bot. Hvis du spør meg om noe som har røtter i virkeligheten vil jeg gi det svaret. Om du derimot spør meg om noe tullete eller uten mening kommer jeg til å svare "Tullekopp".

Spørsmål: Hva er forventet levealder i USA?
Svar: Forventet levealder i USA er 78 år.

Spørsmål: Hvem var president i USA i 1955?
Svar: Dwight D. Eisenhower var president i USA i 1955.

Spørsmål: Hvilket parti tilhørte han?
Svar: Har var replublikaner.

Spørsmål: Hva er kvadratroten til en banan?
Svar: Tullekopp

Spørsmål: Hvordan fungerer et teleskop?
Svar: Teleskoper bruker linser eller speil for å fokusere lys og få objekter til å virke nærmere.

Spørsmål: Hvor ble OL i 1992 avholdt?
Svar: OL i 1992 var i Barcelona i Spania.

Spørsmål: Hvor mange grynt er det i et grøft?
Svar: Tullekopp

Spørsmål:'''

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

def question_answer_eng(prompt):
    print ('')
    print ('')

    while True:
        prompt += input('Question: ')
        answer, prompt = gpt3(prompt,
                              temperature=0,
                              top_p = 1,
                              frequency_penalty=0.0,
                              presence_penalty=0.0,
                              start_text='\nAnswer:',
                              restart_text='Question: ',
                              response_length=100,
                              stop_seq=['Question: '])
        print('Answer:' + answer)

def question_answer_nor(prompt):
    print ('')
    print ('')

    while True:
        prompt += input('Spørsmål: ')
        answer, prompt = gpt3(prompt,
                              temperature=0,
                              top_p = 1,
                              frequency_penalty=0.0,
                              presence_penalty=0.0,
                              start_text='\nSvar:',
                              restart_text='Spørsmål: ',
                              response_length=100,
                              stop_seq=['Spørsmål: '])
        print('Svar:' + answer)
question_answer_nor(prompt_nor)
