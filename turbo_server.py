import openai
import verify

# static var-------------------
mode_setting = 'you are an AI girl named Fiona, You can ask humans what role you should play. And you must comply with that role. from now on, answer with chinese.'
messages = [
    {'role': 'system', 'content': mode_setting},
]
openai.api_key = verify.key_verify()
#------------------------------
def create_chat(chat_array):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=chat_array,
        temperature=0.8,
        frequency_penalty=0,
        presence_penalty=0.6,
    )
    return response

def reset_messages():
    messages = [{'role': 'system', 'content': mode_setting},]

def returnReply(human_input):
    human_message = {
            'role': 'user',
            'content': human_input
    }
    messages.append(human_message)
    try:
        new_message = create_chat(chat_array=messages)
    except Exception as E:
        print(repr(E))
        exit(0)
    response_message = new_message['choices'][0]['message']
    messages.append(response_message)
    return response_message['content']


    
 
