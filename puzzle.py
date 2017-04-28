# Caeser
# cipher_key = 13
# text_message = "lbh zhfg hayrnea jung lbh unir yrnearq"
# text_message_list = text_message.split(" ")
# de_message = ""
# for word in text_message_list:
#     de_word = ""
#     for i in word:
#         i = chr((ord(i) - 97 + cipher_key) % 26 + 97)
#         de_word += i
#     de_message += " " + de_word
# print (de_message)

from math import random
def cipher(user_input1, user_input2, scene_number):
    key = 3
    Note_list = ["Zkdw jrhv edfn dqg iruwk frqvwdqwob, exw qhyhu lq d vwudljkw olqh?",
                "Zkdw orvhv lwv khdg lq wkh pruqlqj dqg jhwv lw edfn dw qljkw?"]
    answer_list = ["What goes back and forth constantly, but never in a straight line?",
                    "What loses its head in the morning and gets it back at night?"]
    try:
        user_input1 = int(user_input1)
    except ValueError:
        #display text next to the input box to tell the user to enter a valid input
    else:
        if user_input == key:
            # display answer
