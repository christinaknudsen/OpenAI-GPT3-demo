# -*- coding: utf-8 -*-
import openai
from dotenv import load_dotenv
import os
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

prompt = '''Action: write a Python code that prints "hello" everytime there is an even number in a loop over every number
code:
i = 0
while (True):
    if i %2:
        print ('hello')
    i+=1

Action: write a python function that takes a variable as an input, and multiplies this variable with 3
code:
def multiplication(var):
    return var*3

Action: write a python code that prints a long decimal number with only two decimals.
code:
def long_decimal(num):
    return str(num).rjust(2, '0')


Action: write a python code that takes a variable as an input, and prints the variable in a binary format
code:
def binary_format(var):
    return '%b' % var

Action: write a python code that takes a variable as an input, and prints the variable in a octal format
code:
def octal_format(var):
    return '%o' % var

Action: write a python code that opens and reads a text file
code:
def read_file(filename):
    with open(filename, 'r') as f:
    for line in f:
    print(line)

Action: write a python code that opens and writes a text file
code:
def write_file(filename, data):
    with open(filename, 'w') as f:
    f.write(data)

Action:'''



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
    print (response)
    return answer, new_prompt

def write_code(prompt):
    while True:
        prompt += input('Action: ')
        answer, prompt = gpt3(prompt,
                              temperature=0.5,
                              frequency_penalty=0.0,
                              presence_penalty=0.0,
                              start_text='\nCode:',
                              restart_text='\nAction: ',
                              response_length=100,
                              stop_seq=['\n'])
        print('Code:' + answer)
write_code(prompt)
