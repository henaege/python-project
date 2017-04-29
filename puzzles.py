class Puzzle(object):
    def __init__(self):
        pass

class Bedroom_Puzzles(Puzzle):
    def __init__(self):
        pass

    def puzzle1(self):
        correct = False
        print """Find a 10-digit number where the first digit is how many
        zeros there arein the number, the second digit is how
        many 1s there are in the number etc. until the tenth
        digit which is how many 9s there are in the number.\n """

        user_input = raw_input("What is the solution? ")

        correct_answer = "6210001000"
        if user_input == correct_answer:
            correct = True

    def puzzle2(self):
        correct = False
        print """Tom asked his Granny how old she was.
        Rather than giving him a straight answer, she replied:\n """
        print '''""I have 6 children, and there are 4 years between each one
        and the next. I had my first child (your Uncle Peter) when I was 19.
        Now the youngest one (Your Auntie Jane) is 19 herself. That's all I'm telling you!"\n'''

        user_input = raw_input("How old is Tom's Granny?\n ")

        correct_answer = "58"
        if user_input == correct_answer:
            correct = True