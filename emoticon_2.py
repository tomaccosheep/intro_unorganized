#emoticon_2.py
import random

eye_list = [':', ';']
nose_list = ['>', '-']
mouth_list = [')', '(']

def emo_gen(in_num):
    out_string = ''
    print("generating...")
    for i in range(0, in_num):
        out_string = out_string + random.choice(eye_list) + random.choice(nose_list) + random.choice(mouth_list) + ' '
    return out_string

print(emo_gen(4))
