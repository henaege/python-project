from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print"This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    deaths = [
        "You died. You kinda suck at this.",
        "My grandma beat this game with her eyes closed and one hand tied behind her back, but you just died.",
        "You died, loser.",
        "This is about what I expected from the likes of you. Enjoy death." 
    ]

    def enter(self):
        print Death.deaths[randint(0, len(self.deaths)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "\n"
        print "While sleeping in and missing the beginning of your"
        print "shift, enemy spies released nerve gas into the"
        print "ventilation system of your ship. Being a big weenie"
        print "you sleep with the covers over your head. Luckily the"
        print "covers filtered out the nerve gas and you are the sole"
        print "survivor of your ship's crew."
        print "\n"
        print "Your last mission is to retrieve the self-destruct"
        print "bomb from the armory and plant it on the bridge to"
        print "blow up the ship after getting into an escape pod."
        print "You're running down the central corridor toward the"
        print "armory when suddenly an enemy spy jumps out, blocking"
        print "the entrance to the armory. He's reaching for his"
        print "weapon..."
        print "\n"
        print "What action do you take? (shoot, dodge, tell a joke)"

        action = raw_input("> ")

        if action == "shoot":
            print "\n"
            print "Despite your lingering grogginess, you are quick"
            print "on the draw, firing your blaster at the spy."
            print "Because of your lingering grogginess your aim"
            print "sucks and you miss completely. The spy, on the"
            print "other hand, is well trained. He makes a lewd"
            print "comment about your sister in a language you don't" 
            print "understand just before he shoots your face"
            print "repeatedly."
            return 'death'

        elif action == "dodge":
            print "\n"
            print "Somehow you summon the presence of mind to dodge"
            print "aside, bobbing and weaving, juking and jiving like"
            print "a pro boxer after the title belt. The spy squeezes"
            print "off a shot that narrowly misses your head."
            print "\n"
            print "Just as you glide past the spy, you slip on the"
            print "peel of the banana he just finished and bonk your"
            print "head on the metal door of the armory. The last"
            print "thing you see before slipping into unconciousness"
            print "is the spy's boot on an imminent collision course"
            print "with your head."
            return 'death'

        elif action == "tell a joke":
            print "\n"
            print "Luckily, you're well-known as the ship's funniest"
            print "crew member. You tell the best joke you know."
            print "The spy tries not to laugh, but becomes"
            print "overwhelmed by mirth. He laughs so hard he has an"
            print "aneurysm and keels over on the spot. You leap over"
            print "his corpse and into the armory."
            return 'armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print "\n"
        print "You execute a sweet diving roll through the armory"
        print "door, landing in a crouch in the middle of the room."
        print "You don't see any more spies as you scan the room."
        print "You stand up and run to the far side of the room,"
        print "finding the safe containing the self-destruct bomb."
        print "You'll need to enter the safe's code on the keypad"
        print "to unlock it and retrieve the bomb."
        print "\n"
        print "If you get the code wrong 10 times the lock destroys"
        print "itself and you won't be able to get the bomb."
        print "The code is 3 digits. Good luck."
        code = [[randint(1,9)], [randint(1,9)], [randint(1,9)]]
        print code
        user_input = raw_input("[keypad]> ")
        guess_string = list(user_input)
        guess = [map(int, x) for x in guess_string]


        # guess = [int(raw_input("[keypad]> ")), int(raw_input("[keypad]> ")), int(raw_input("[keypad]> "))]

        guesses = 0

        while guess != code and guesses < 9:
            
            print "BZZZZTT!"
            guesses += 1
            user_input = raw_input("[keypad]> ")
            guess_string = list(user_input)
            guess = [map(int, x) for x in guess_string]
            if guesses == 3:
                print "[Hint: the first digit is %r" % code[0]
            elif guesses == 7:
                print "Hint: the second digit is %r" % code[1]
            

        if guess == code:
            print "\n"
            print "The safe clicks open and the seal breaks."
            print "Super-cooled air rushes out in a dense fog."
            print "As the fog clears, you see the bomb nestled in"
            print "its insulated shell. Once the bomb reaches room"
            print "temperature it will explode. Plant it in the"
            print "correct spot on the bridge and make your way to"
            print "an escape pod before then!"
            return 'bridge'

        else:
            print "\n"
            print "The lock buzzes one last time and you feel sick"
            print "as you hear the lock mechanism fuse itself shut."
            print "You sit there contemplating your failure until the"
            print "spies blow the ship up remotely and you die."
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print "\n"
        print "After grabbing the self-destruct bomb you rush to the"
        print "bridge. As you burst into to the room, 5 spies who"
        print "were trying to take control of the ship turn around"
        print "in surprise at your sudden interruption. They haven't"
        print "pulled their weapons yet, as they see the bomb tucked"
        print "under your arm and they don't want to set it off."
        print "\n"
        print "What action do you take? (throw the bomb, place the bomb)"
        print "\n"
        action = raw_input("> ")

        if action == "throw the bomb":
            print "\n"
            print "In a panic you throw the bomb at the nearest spy"
            print "and leap for the door. Mid-leap, one of the other"
            print "spies shoots you in the back. As you die you see"
            print "one of the spies frantically try to disarm the"
            print "bomb. You die knowing that at least it will"
            print "probably blow them up when it goes off."
            return 'death'

        elif action == "place the bomb":
            print "\n"
            print "You point the blaster at the bomb under your arm"
            print "and the spies put their hands up as they start to"
            print "sweat. You inch backward to the door, open it,"
            print "then carefully place the bomb on the floor,"
            print "pointing your blaster at it the entire time."
            print "Then, you jump through the door, punch the close"
            print "button, and blast the lock so the spies can't get"
            print "out. Now that you have placed the bomb you can"
            print "find an escape pod and blow this popsicle stand."
            return 'escape_pod'

        else:
            print "DOES NOT COMPUTE!"
            return 'bridge'

class EscapePod(Scene):

    def enter(self):
        print "\n"
        print "You rush through the ship desperately trying to make"
        print "it to an escape pod before the ship explodes."
        print "It seems like hardly any spies are on the ship, so"
        print "your run is clear of interference. You get to the"
        print "chamber with the escape pods and now you need to pick"
        print "one to take. Some of them could be damaged but you"
        print "don't have time to look. There are 5 pods to choose"
        print "from. Which one do you take?"

        good_pod = randint(1,5)
        print good_pod
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "\n"
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into space jam."
            return 'death'

        else:
            print "\n"
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily glides out into space, then rockets"
            print "propel you toward the planet below. As you fly to"
            print "the planet, you look back at the ship through the"
            print "viewport and see the ship explode like a bright"
            print "star, taking out the spy ship at the same time."

            return 'finished'

class Finished(Scene):

    def enter(self):
        print "You won! Good job."
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'armory': LaserWeaponArmory(),
        'bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

