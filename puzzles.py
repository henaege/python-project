import math



class Puzzle(object):
    def __init__(self, user_input=None, puzzle_solved=False):
        self.user_input = user_input
        self.puzzle_solved = puzzle_solved



class Bedroom_Puzzles(Puzzle):
    def __init__(self):
        super(Bedroom_Puzzles, self).__init()


    def puzzle1(self, user_input):
        correct = False
        print """Find a 10-digit number where the first digit is how many
        zeros there are in the number, the second digit is how
        many 1s there are in the number etc. until the tenth
        digit which is how many 9s there are in the number.\n """

        # print "What is the solution? "

        correct_answer = "6210001000"
        if self.user_input == correct_answer:
            correct = True
        return correct

    def puzzle2(self, user_input):
        correct = False
        print """Tom asked his Granny how old she was.
        Rather than giving him a straight answer, she replied:\n """
        print '''"I have 6 children, and there are 4 years between each one
        and the next. I had my first child (your Uncle Peter) when I was 19.
        Now the youngest one (Your Auntie Jane) is 19 herself. That's all I'm telling you!"\n'''

        # print "How old is Tom's Granny?
        self.update_user_input(user_input)
        correct_answer = "58"
        if self.user_input == correct_answer:
            correct = True
        return correct


class Library_puzzle(Puzzle):

    def __init__(self):
        super(Library_puzzle, self).__init__()

    def check_answer(self, user_input, answer):
        if user_input is not None:
            if user_input == answer:
                # display answer
                self.puzzle_solved = True
            else:
                print ("We need your answer.")

    def puzzle1(self, string_list):
        text_generator(screen, "Zkdw jrhv edfn dqg iruwk frqvwdqwob, exw qhyhu lq d vwudljkw olqh?", (200, 300))
        library_puzzle.check_answer(entry.get_user_input(), "3")
