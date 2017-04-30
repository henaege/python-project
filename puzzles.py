from math import random

class Puzzle(object):
    def __init__(self):
        pass

class Bedroom_Puzzles(Puzzle):
    def __init__(self):
        pass

    def puzzle1(self):
        correct = False
        print """Find a 10-digit number where the first digit is how many
        zeros there are in the number, the second digit is how
        many 1s there are in the number etc. until the tenth
        digit which is how many 9s there are in the number.\n """

        user_input = raw_input("What is the solution? ")

        correct_answer = "6210001000"
        if user_input == correct_answer:
            correct = True
        return correct

    def puzzle2(self):
        correct = False
        print """Tom asked his Granny how old she was.
        Rather than giving him a straight answer, she replied:\n """
        print '''"I have 6 children, and there are 4 years between each one
        and the next. I had my first child (your Uncle Peter) when I was 19.
        Now the youngest one (Your Auntie Jane) is 19 herself. That's all I'm telling you!"\n'''

        user_input = raw_input("How old is Tom's Granny?\n ")

        correct_answer = "58"
        if user_input == correct_answer:
            correct = True
        return correct

class Library_puzzle(user_input1, user_input2, scene_number):
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
