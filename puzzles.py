import math


class Puzzle(object):
    def __init__(self, user_input=None, puzzle_solved=False):
        self.user_input = user_input
        self.puzzle_solved = puzzle_solved



class Bedroom_Puzzle(Puzzle):
    def __init__(self):
        super(Bedroom_Puzzle, self).__init__()

    def puzzle1(self, user_input):
        correct = False
        print """Find a 10-digit number where the first digit is how many
        zeros there are in the number, the second digit is how
        many 1s there are in the number etc. until the tenth
        digit which is how many 9s there are in the number.\n """
        correct_answer = "6210001000"
        if user_input == correct_answer:
            return True


    def puzzle2(self, user_input):
        correct = False
        print """Tom asked his Granny how old she was.
        Rather than giving him a straight answer, she replied:\n """
        print '''"I have 6 children, and there are 4 years between each one
        and the next. I had my first child (your Uncle Peter) when I was 19.
        Now the youngest one (Your Auntie Jane) is 19 herself. That's all I'm telling you!"\n'''

        correct_answer = "58"
        if user_input == correct_answer:
            return True


class Library_puzzle(Puzzle):

    def __init__(self):
        super(Library_puzzle, self).__init__()

    def puzzle1(self, user_input):
        # print questions
        if self.check_answer(user_input, '3'):
            # print answer
            # print question
            if self.check_answer(user_input, 'pendulum'):
                return True
            else:
                # print you need to think harder?

    def puzzle2(self, user_input):
        # print questions I don't know what the answer is? But you pass in into the check_answer method
        if self.check_answer(user_input, ''):
            # print answer
            # print question
            if self.check_answer(user_input, 'pendulum'):
                return True
            else:
                # print you need to think harder?

    def check_answer(self, user_input, answer):
        if user_input is not None:
            if user_input == answer:
                self.puzzle_solved = True
                return True
            else:
                print ("We need your answer.")


class Kitchen_Puzzle(Puzzle):
    def __init__(self):
        super(Kitchen_Puzzle, self).__init__()

    def puzzle1(self):
        pass

    def puzzle2(self):
        pass
