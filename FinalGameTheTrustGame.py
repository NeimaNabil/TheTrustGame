# -------------------------------------------
""" Hey there. This is the programmer of the game.
Before proceeding, I'd like to inform
that this was the longest program I've ever coded so far.
I learnt so many lessons and now have clearer
vision of what I should be focusing on
to develop my programming skills.
I tried as best as I can to use best
practises for the first time. Things like:
- Indentation, tried to keep text as
short as possible and use methods like the
backslash to continue in the next line
, imported each module on a new line and also used
"" only in my entire code without any ''.
This program is neither perfect not useless.
I intend to make it better on a personal scale.
BEFORE READING THE CODE!: I really really recommend
you look at the game with an eye of a gamer or a player before a programmer.
Try to have fun playing it and maybe even reach the secret ending.
Thank you.
"""
# -------------------------------------------


# Importing modules that will be used late on.
import random
import time

# IMPORTANT NOTES ABOUT THE GAME:
# 0. Because there variables WILL NOT be modified or
# changed anywhere in the game, as they play a role of containers,
# I decided to use them as global variables instead of
# passing them each time when they will not be even changed ever.
# 1. However, there are other variables such as
# inventory that can be changed in the middle of the game,
# so in order not to use them as global variables
# I decided to pass them to functions that need
# them as "arguments" and return them whenever they are changed
# So it's more of delivering process
# I considered the main func a base for all
# variables so they are delivered
# and at the end they come back to get stored and
# be used for later functions located inside main
# 2. At last, I didn't use the lower_case thing.
# Instead, I used the camelCase to name funcs and variables.

# This is used to show a differnet message each time the player loses:
endings = ["You've lost your way. Without awareness, you're stuck in a loop."
           " Think about your choices, and try again with a clear mind.",
           "Fatigue overcame you. With low awareness, you fell asleep. Your "
           "journey stops here. Wake up refreshed and start again.",
           "Distractions trapped you. With low awareness, you lost sight "
           "of your goal. Focus your mind and begin your adventure again."]

# This is used to show a differnet message each time the player
# has full awareness Level:
fullyAware = ["Superb! You're fully aware of every detail",
              "Impressive; your attention to your surroundings is complete",
              "Your awareness is commendable; you are alert to every detail"]

# This is used to show a differnet message each time the player
# chooses a wrong decision:
wrongChoicesNavigatin = ["You suddenly feel dazy and lose sense of your "
                         "surroundings for a while..",
                         "Everything becomes foggy at once, "
                         "you feel a werid sense of movement around you..",
                         "With a blink of an eye, everything turns black, "
                         "to an unknown time..."]

# This one is used to check for input validation later:
choicesAvaliable = ["1", "2", "3"]

# This is used to show a different message each time
# the player enters a meaningless input:
invalidInput = ["What? ", "I don't quite get what you wanna say",
                "Hint: Type 1, 2, or 3"]

# A function that sets a line to organize the screen for the player


def organizing():
    print("-"*100)


# A function that both prints string and waits a couple of
# seconds to make the game more user-friendly
def printPause(text):
    print(text)
    time.sleep(3)


# The func that the game starts with. It describes the vibes. Also,
# asks for the player fav num to create a nickname.
def beginning():
    printPause("You find yourself in a room that's pure white,")
    printPause("Its glass walls revealing a view of the sky as if you're "
               "standing atop a cloud.")
    printPause("The surreal beauty of your surroundings is both "
               "calming and unsettling.")
    printPause("As you take in the scene, you notice a mirror. "
               "You see your own reflection, but something feels off.")
    printPause("Your mind is a void, a blank slate. Memories "
               "elude you, even the simplest truth of your own name.")
    printPause("Lost in thought and beginning to explore the "
               "room, your attention is suddenly drawn to the door.")
    printPause("A letter slides under it, capturing your curiosity.")
    printPause("You pick it up, and as you unfold the paper, "
               "a strange sensation washes over you.")
    printPause("A voice begins to speak, not from the room, "
               "but inside your head. ")
    printPause("It's the voice of a girl, clear and calm, "
               "reading the letter aloud.")
    printPause("\"What is your favourite number?\" the voice asks.")
    playerfavnumber = input("My favourite number is: ").lower().strip()
    playerName = f"\"Traveler {playerfavnumber}\""
    printPause("Puzzled, you take a moment before writing "
               "down your favorite number.")
    printPause("As soon as you do, the ink fades, and before "
               "your eyes, new words appear, written by an unseen hand.")
    printPause("The letter now reads, \"From now on, "
               f"consider your name to be {playerName}.\"")
    printPause("At the bottom, a final, enigmatic command "
               "emerges: \"Follow your gut...\"")
    printPause("\"You are ok as long as you take care of "
               "your awareness level\"")
    printPause("\"you have 3 awareness points, if "
               "they reach zero or below, you lose.\"")
    printPause("The voice fades, leaving you in a state of bewilderment.")
    printPause(f"The journey has begun, {playerName}.")
    printPause("The path is uncertain, but the message is clear: "
               "trust nothing, question everything.")

    organizing()

    # look at note number 1 in IMPORTANT NOTES above.
    return playerName

# -------------------------------------------

# My program contains 4 stages that are so similar in
# both handling the if statements and describing the surroundings
# So I created a single function to handle if statements (ifchoices function)
# And created a single function that describes the surroundings
#  (describing function "you will find it after the ifchoices func")
# I did this so I only write the code once for each and
# then call both functions inside of the stage func
# while providing the necessary argumetns depending on each scenario


def ifchoices(question, correctdecision, correctphrase, minus1decision,
              minus1phrase, minus2decision, minus2phrase, awarenessLevel,
              inventory: list, invalidInput=invalidInput,
              choicesAvaliable=choicesAvaliable,
              wrongChoicesNavigatin=wrongChoicesNavigatin):

    # A loop that keeps asking for input in case the user
    # enteres somethings meaningless
    while True:

        # Cleaning the user choice and asking for it:
        playerchoice = input(question).lower().strip().replace(" ", "")

        # Checking whether the user entered something meaningfull and expected
        # as they are choosing which action to take
        if playerchoice in choicesAvaliable:

            if playerchoice == correctdecision:
                printPause(correctphrase)
            else:
                if playerchoice == minus1decision:
                    printPause(minus1phrase)
                    # Decreaase the awareness Level of the player if
                    # he picks the wrong choice
                    awarenessLevel -= 1
                elif playerchoice == minus2decision:
                    printPause(minus2phrase)
                    awarenessLevel -= 2

                # Start picking a phrase to make a smooth navigation to
                # the next stage by choosing it randomly
                printPause(random.choice(wrongChoicesNavigatin))

        # Checking whether the user used bluepotion (It gives them the
        # chance to skip
        # the Level, can also be used for the secret ending)
        elif playerchoice == "bluepotion":
            # Check if it's already in the inventory
            if playerchoice in inventory:
                printPause("A hidden power navigates you to the next "
                           "stage through glass...!")
                printPause(f"You were lucky to skip this difficult round. "
                           "Sometimes, it is good to relax your brain (:")
                # Remove it so it can't be used again
                inventory.remove("bluepotion")
            else:
                printPause("You search your inventory, but you can't seem to "
                           "find it. Maybe it's time to make a decision...")
                continue

        # Checking whether the user used redpotion (It gives them the
        # chance to revive, can also be used for the secret ending)
        elif playerchoice == "redpotion":
            printPause("You went to use the redpotion. However, "
                       "you thought saving it would be better, "
                       "so you put it back")
            continue

        # Checking whether the user wants to quit
        elif playerchoice == "quit":
            # Offer the user to double check if they really want to quit
            if input("Are you sure you want to quit? (y/n): ") == "y":
                quit()
            else:
                continue

        # Checking whether the user entered something meaningless
        else:
            print("\n", "#"*10, random.choice(invalidInput), "#"*10, "\n")
            continue

        # look at note number 1 in IMPORTANT NOTES above.
        return inventory, awarenessLevel


def describing(sentence1, sentence2):

    # Simply, it takes the 2 describing sentences for the stage
    # and prints a phrase to get the player ready to choose their action
    printPause(sentence1)
    printPause(sentence2)
    printPause("Choose your desicion below (1, 2, or 3)...".center(99, "#"))

# -------------------------------------------

# Creating each single stage on its own.


def stage_shareSecret(awarenessLevel, inventory):

    # Calling the needed functions and passing them unique
    # arguments designed especially for the stage
    describing("You step into a dimly lit room, its atmosphere "
               "heavy with mystery. Before you, on a "
               "pedestal, rests a locked box.",
               "A note attached reads, 'To unlock me, "
               "share a secret. Trust that I will keep it safe.")
    # Note 1 in IMPORTANT NOTES
    return ifchoices("1. Whisper a personal secret to the box.\n2. Shout a "
                     "random word.\n3. Attempt to pick the lock.\n>>> ",
                     "3", "With careful precision, you manipulate the lock. "
                     "Click. The box opens, revealing the next clue inside. "
                     "No secrets were needed this time.",
                     "2", "Your shout reverberates through the "
                     "room, but the box remains unmoved.",
                     "1", "As you whisper, the box tightens "
                     "its hold. A mocking voice "
                     "echoes, 'Your secret is safe... with me.' "
                     "It remains closed.",
                     awarenessLevel, inventory)


def stage_talkingStatues(awarenessLevel, inventory):

    # Calling the needed functions and passing them unique
    # arguments designed especially for the stage
    describing("As you move forward, you encounter two talking statues.",
               "One speaks with a solemn tone, 'Trust us, we will guide "
               "you. One of us tells the truth, and the other lies.")
    # Note 1 in IMPORTANT NOTES
    return ifchoices("1. Ask, 'If I were to ask the other statue which way "
                     "to go, "
                     "what would they say?'\n2. Ask, 'Which way should I "
                     "go?'\n3. "
                     "Ignore the statues and search the room.\n>>> ",
                     "3", "You decide not to trust the statues. As you search "
                     "the room, you find a hidden door behind a tapestry.",
                     "1", "The statues give different answers, and you feel "
                     "confused. However, you find that time is over...",
                     "2", "Both statues point in different directions. "
                     "However, the time is already over...",
                     awarenessLevel, inventory)


def stage_villageElder(awarenessLevel, inventory):

    # Calling the needed functions and passing them unique
    # arguments designed especially for the stage
    describing("You meet a village elder who offers advice: ",
               "'In life, the shortest path isn't always the best. "
               "Choose your path wisely.'")
    # Note 1 in IMPORTANT NOTES
    return ifchoices("1. Ignore the advice and take the shortest path.\n2. "
                     "Ask the elder for more details.'\n3. Take the elder's "
                     "advice and choose the longer path.\n>>> ",
                     "2", "The elder gives you a map with hidden paths and "
                     "shortcuts. This helps you a lot on your journey.",
                     "3", "You start walking through, you make it. However, "
                     "now you are so tired.",
                     "1", "You face many obstacles and hard puzzles, making "
                     "your journey hard and tiring.",
                     awarenessLevel, inventory)


def stage_shakyBridge(awarenessLevel, inventory):

    # Calling the needed functions and passing them unique arguments
    # designed especially for the stage
    describing("You arrive at a deep gap with a narrow, shaky bridge and "
               "wild animals. A sign says: ",
               "'Only those who trust their balance will make it across. "
               "Don't look down.'")
    # Note 1 in IMPORTANT NOTES
    return ifchoices("1. Cross the bridge quickly without looking down.\n2. "
                     "Crawl across the bridge slowly.\n3. Look for another "
                     "way around.\n>>> ",
                     "3", "You find a stable path hidden behind some rocks, "
                     "avoiding the dangerous bridge.",
                     "2", "The bridge still breaks, you "
                     "fall into a net below.",
                     "1", "The bridge breaks, and you fall into a net below.",
                     awarenessLevel, inventory)


def stage_weirdBoxes(awarenessLevel, inventory: list,
                     choicesAvaliable=choicesAvaliable,
                     invalidInput: list = invalidInput):
    # Explaining the stage
    describing("You enter a normal-looking room with two unmarked "
               "boxes and an unlocked door.",
               "Everything looks ok. However, you are not sure "
               "whether to open either of the boxes or not.")

    # I couldn't use ifchoice func becaues this stage is unique and has
    # different if statements and is more intricate.
    # However I used mainly the same technique
    while True:
        # Offering Choices
        playerchoice = input("1. Open Box 1.\n2. Open Box 2.\n3. Walk "
                             "through the door.\n>>> ")
        # Activating an action based on the user choice.
        if playerchoice.strip() in choicesAvaliable:

            if playerchoice == "1":
                printPause("A gentle glow surrounds you, and you find a "
                           "red potion that grants you extra strength.")
                printPause("Your bravery is rewarded.")
                # The player gets the redpotion if they choose the first option
                inventory.append("redpotion")

            elif playerchoice == "2":
                print("A puff of smoke fills the room, and you feel a "
                      "slight sting.")
                # The player gets there awareness level reduced if it's
                # the second option
                awarenessLevel -= 1
            elif playerchoice == "3":
                printPause("You choose to walk through the unlocked door, "
                           "moving on to the next round.")
                printPause("However, you miss out on the potential "
                           "reward hidden in the boxes.")

        # hecking whether the player uses item from inventory and make sure
        #  the item is available
        elif playerchoice == "bluepotion":
            if playerchoice in inventory:
                printPause("A hidden power navigates you to the next stage "
                           "through glass...!")
                printPause(f"You were lucky to skip this difficult "
                           "round. Sometimes, "
                           "it is good to relax your brain (:")
                # Removing the item for inventory so it can't be used again
                inventory.remove("bluepotion")
            else:

                printPause("You search your inventory, but you can't "
                           "seem to find it. "
                           "Maybe it's time to make a decision...")
                continue

        elif playerchoice == "redpotion":
            printPause("You went to use the redpotion. However, "
                       "you thought saving it would be better, "
                       "so you put it back")
            continue

        # Checking if the player wants to quit
        elif playerchoice == "quit":
            if input("Are you sure you want to quit? (y/n): ") == "y":
                quit()
            else:
                continue

        # Checking for invalid input
        else:
            print("\n", "#"*10, random.choice(invalidInput), "#"*10, "\n")
            continue

        # NOTE 1 IN IMPORTANT NOTES:
        return inventory, awarenessLevel


# The same goes for this stage, it contains unique if statements,
# so I created its flow inside of it.
def stage_silentMan(awarenessLevel, inventory: list,
                    choicesAvaliable=choicesAvaliable,
                    invalidInput: list = invalidInput):

    # Explaining the stage
    describing("You enter a room that looks like a temple. Inside, you see "
               "a man reading a book.",
               "A sentence above his head says, 'Talk to me if you want'.")

    while True:
        # Offering Choices
        playerchoice = input("1. Ignore the man and walk through the door.\n2."
                             " Talk to the man.\n>>> ").lower().strip()
        # Activating an action based on the user choice.
        if playerchoice in choicesAvaliable:

            if playerchoice == "1":
                print("You feel a bit guilty for not taking the risk, "
                      "but you move on to the next puzzle...")
            elif playerchoice == "2":
                print("The man silently gives you a BluePotion. It's up to "
                      "you to decide what to do with it.")
                # Compensate the player with a bluepotion if they
                # were brave enough
                inventory \
                    .append("bluepotion")
                while True:
                    askPotion = input("Would you like to ask about the "
                                      "potion? (y/n): ").lower().strip()
                    if askPotion == "y":
                        printPause("The man finally looks at you and hands you"
                                   " a piece of paper with a puzzle on it. ")
                        printPause("The puzzle says:"
                                   "'I am not alive, but I can grow; I don't "
                                   "have lungs, but I need air; I don't have"
                                   " a mouth, but water kills me.")
                        printPause("What am I?\n1. Fire\n2. Plant\n3. Ice: ")
                        # Give the player opportunity to know what
                        # the potion does
                        if input("You are: ") == "1":
                            printPause("The man speaks and explains "
                                       "the potion is not "
                                       "dangerous and is used to skip a level")
                            printPause("He continues: 'To use it, "
                                       "enter the word \"BluePotion\"'")
                        else:
                            printPause("The man looks disappointed and refuses"
                                       " to talk. You must continue without "
                                       "knowing if the potion is dangerous.")
                        break
                    elif askPotion == "n":
                        printPause("The man is confused. Re-enter your choice")
            # Note 1 In IMPORTANT NOTES:
            return inventory, awarenessLevel
        elif playerchoice == "redpotion":
            printPause("You went to use the redpotion. However, "
                       "you thought saving it would be better, "
                       "so you put it back")

        elif playerchoice == "quit":
            if input("Are you sure you want to quit? (y/n): ") == "y":
                quit()

        else:
            print("\n", "#"*10, random.choice(invalidInput), "#"*10, "\n")


# The end stage, it also contains the secret ending!
def ending(inventory, playerName):

    # Describing the scene
    printPause("You enter a grand hall. The room is big, with high "
               "ceilings and tall walls covered in beautiful tapestries...")
    printPause("A huge chandelier hangs from the ceiling, casting "
               "a soft light that makes everything look magical..!")
    printPause("In the center of the hall, three people stand, "
               "each looking different and special.")
    printPause("The Guardian: A serious knight wearing shining "
               "armor. He looks strong and ready to protect.")
    printPause(" He stands tall and firm, watching everything closely.")
    printPause("The Seer: A calm person in long, flowing robes that shimmer.")
    printPause("Her eyes are deep and seem to see right through you. "
               "She has a peaceful and wise feeling about her.")
    printPause("The Prince: A rich young man wearing fancy "
               "clothes and gold jewelry. He has a charming "
               "smile and looks confident.")
    printPause("The hall is very quiet. The Guardian steps "
               "forward and says in a strong voice, ")
    printPause(f"\"Congratulations, {playerName} You've come far. "
               "Now, you have one last test to claim your prize.\"")
    printPause("The young man smiles and says, \"Here, your "
               "true intentions and abilities are shown.")
    printPause(" Be careful. Things are not always what they seem..\"")
    printPause("The Seer speaks softly, 'Patience and "
               "thoughtfulness will guide you to the truth.'")
    printPause(".")
    printPause("..")
    printPause("...")
    printPause("CHOOSE WISELY".center(21, "^"))
    printPause("1. The Guardian\n2. The Prince\n3. The Seer")

    while True:

        playerfinalchoice = input(">>> I will choose: ") \
            .lower().strip().replace(" ", "")

        # Checking whether the player want to use something from inventory
        if playerfinalchoice == "bluepotion" \
           or playerfinalchoice == "redpotion":
            # Unlocking the secret ending if conditions are met
            if "bluepotion" in inventory and \
               "redpotion" in inventory:
                printPause("The room shimmers and fades, revealing "
                           "a hidden path..!")
                printPause("ou follow it to a serene garden bathed in soft, "
                           "blue light..")
                printPause("In the center, a teen girl emerges, cloaked "
                           "in shadows yet exuding a comforting presence.")
                printPause(f"\"Congratulations, {playerName}\" the "
                           "figure says in a gentle, knowing voice.")
                printPause("\"You have reached a rare destination, a place "
                           "few ever find.")
                printPause("Your journey has been long, and your "
                           "choices have brought you here, to me.\"")
                printPause("The figure pauses, letting the moment sink in.")
                printPause("\"I am the creator of this world, who designed"
                           " your trials. You have shown wisdom and courage.")
                printPause("Remember, the journey and the destination "
                           "are equally important. Enjoy each moment.")
                printPause("\"You are unique, not just for reaching this "
                           "stage, but for the choices you've made along the ")
                printPause("way. Continue to trust yourself and embrace the "
                           "paths ahead with an open heart and mind.\"")
                printPause("The figure begins to fade, leaving you with "
                           "a sense of calm and wonder.")
                printPause("..."*10)
                print("Farewell, traveler. May your future journeys "
                      "be as enlightening as this one!".center(150, '"'))
                break

            # Asking the player to play agian and gather all requirements,
            # Also give them a chance to choose from the 3 characters of before
            else:
                printPause("You feel a surge of energy, but "
                           "nothing else seems to happen.")
                printPause("A soft, enigmatic voice whispers through the air:")
                printPause("So close, yet not quite there. One "
                           "journey alone cannot reveal all truths.")
                printPause("Seek beyond what you hold, delve deeper "
                           "into the unknown..")
                printPause("Only then will the ultimate secret unfold..!")

        # Go with the traditional endings depending on the player choice
        else:

            if playerfinalchoice == "1":
                printPause("The Guardian leads you to a big library full of "
                           "old books and scrolls")
                printPause("The room smells like old paper and ink. He gives "
                           "you a big book.")
                printPause("You sought truth and protection. Your prize is "
                           "knowledge, your greatest ally.")
                break
            elif playerfinalchoice == "2":
                printPause("The Prince takes you to a fancy room filled "
                           "with gold statues and treasures.")
                printPause("...")
                printPause("But when you touch them, they turn to dust..?!")
                printPause("The Prince laughs. \"You fell for the illusion. "
                           "Your prize is the lesson that not everything that "
                           "looks valuable is real.\"")
                break
            elif playerfinalchoice == "3":
                printPause("The Seer guides you through a hidden passage.")
                printPause("You come into a peaceful garden, filled with "
                           "colorful flowers. The Seer smiles and says,")
                printPause("\"You chose wisdom. Your prize is knowing you can "
                           "trust your instincts. "
                           "The journey made you wise.\"")
                break

            elif playerfinalchoice == "quit":
                if input("Are you sure you want to quit? (y/n): ") == "y":
                    quit()

            else:
                print("\n", "#"*10, random.choice(invalidInput), "#"*10, "\n")


# This func is used to see whether the player's awareness Level is ok
# if not, they lose ( if they weren't given the chance to use a
# redpotion and heal or revive )
def awarenesscheck(awarenessLevel, inventory: list, playerName,
                   fullyAware: list = fullyAware,
                   endings=endings):

    # Check generally whether the player can even continue
    if awarenessLevel > 0:

        # I offer different phrases depending on the player's situation
        if awarenessLevel == 3:
            printPause(f"{random.choice(fullyAware)}, {playerName}")
        else:
            printPause(f"Your awreness level is {awarenessLevel}")
            printPause("Pay attention, if your awareness level gets down "
                       "to Zero. You will be stuck in this maze forever.")

    # Before eliminating the player, I check whether they can revive using
    # the redpotion, if not they lose.
    else:
        if "redpotion" in inventory:
            printPause("+1")
            printPause(f"You were about to lose sense of your surroundings. "
                       "However, you used the \"RedPotion\".")
            printPause("Be careful, another fall might cost you a lot.")

            # I remove the redpotion so it's no longer can be used
            inventory.remove("redpotion")
            awarenessLevel = 1

        else:
            printPause("Unfortunatly, your awareness level is so low.")
            print(random.choice(endings))
            rePlay()

    organizing()

    # Look at note 1 in IMPORTANT NOTES:
    return awarenessLevel, inventory


# A func to replay the game:
def rePlay():
    while True:
        playAgain = input("Do you want to play again? (y/n)")
        playAgain.lower().strip()
        if playAgain == "y":
            main()
        elif playAgain == "n":
            quit()
        else:
            printPause("Invalid Input")


# creating a list to play the stages.
# I decided to make it global as it's not
# EVER going to be changed, only accessed.
stages = [stage_weirdBoxes, stage_shakyBridge, stage_shareSecret,
          stage_silentMan, stage_talkingStatues, stage_villageElder]


# I randomize the selection process so it's unique each time
random.shuffle(stages)
# A function that mainly and generally operates the big picture of the program


def main():
    while True:
        # Initializing variables that will be changed later inside the func,
        # so they are not global and delivered as arguments.
        awarenessLevel = 3
        playerName = ""
        inventory = []
        round = 1

        # We start the game and return the value of the player's name to the
        # Varible playerName to use it in the ending
        playerName = beginning()

        # Start a loop to play, where we always return the value of changed var
        # so they are not globaly accessed while also being changed freely.
        for stage in stages:
            printPause(f"Now, You will start round {round}")
            organizing()
            inventory, awarenessLevel = stage(awarenessLevel, inventory)
            awarenessLevel, inventory = awarenesscheck(awarenessLevel,
                                                       inventory, playerName)
            round += 1

        # We then play the ending.
        ending(inventory, playerName)

        rePlay()


main()
