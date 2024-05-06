import os.path
import openai
import configparser
import time

MAX_ERRORS = 5

def exceptionHandler(error):
    print('Exception occurred: ')
    print(error)
    time.sleep(2)


def getGPT4Response(prompt, config_dict):
    openai.api_key = config_dict['openai_api_key']
    try_count = 0
    while 1:
        if try_count < MAX_ERRORS:
            try:
                response = openai.Completion.create(
                    model = config_dict['gpt_model'],
                    prompt=prompt,
                    max_tokens=int(config_dict['max_tokens']),
                    temperature=0,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                time.sleep(1)
                break
            except openai.error.ServiceUnavailableError as e:
                try_count += 1
                exceptionHandler(e)
            except openai.error.RateLimitError as e:
                try_count += 1
                exceptionHandler(e)
            except openai.error.APIError as e:
                try_count += 1
                exceptionHandler(e)
        else:
            raise Exception('Max errors reached. Exiting...')
    try:
        # serialization to save the response
        return response.to_dict_recursive()
    except:
        return {}