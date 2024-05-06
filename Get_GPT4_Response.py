import os.path
import openai
import configparser
import time
import json
import re

MAX_ERRORS = 5

def exceptionHandler(error):
    print('Exception occurred: ')
    print(error)
    time.sleep(2)


def getGPT4Response(prompt, prompt_prefix, config_dict):
    client = openai.OpenAI(api_key=config_dict['openai_api_key'])
    try_count = 0
    while 1:
        if try_count < MAX_ERRORS:
            try:
                response = client.chat.completions.create(
                        model = config_dict['gpt_model'],
                        messages = [
                            {'role': 'system','content': prompt_prefix},
                            {'role': 'user','content': prompt},
                                    ],
                        temperature = 0,
                        max_tokens= int(config_dict['max_tokens']),
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
                time.sleep(1)
                break
            except openai.RateLimitError as e:
                try_count += 1
                exceptionHandler(e)
            except openai.APIError as e:
                try_count += 1
                exceptionHandler(e)
        else:
            raise Exception('Max errors reached. Exiting...')
    try:
        return json.loads('{'+re.findall(r'\{(.*?)\}',response.choices[0].message.content.replace('\n',''))[0]+'}')
    except:
        return {}