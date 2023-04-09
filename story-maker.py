import time
import sys


def meeting():
    print(
        "Hello my friend. Today it is I, who will help you create your own New Year's story. \n"
        "In order to get started we need to get to know you \n"
        "Me name is Egor. what's your name?")

    user_name = input()

    print("Nice to meet you. {}, how old are you?".format(user_name))

    user_age = input()

    if user_age.isdigit():
        print("Thank you a lot. Now we start to write our story")
        write_story()

    else:
        while user_age.isdigit() == False:
            print("Oh... {}. {} is not number... try to write your age with number".format(user_name, user_age))
            user_age = input()
            if user_age.isdigit():
                print("Thank you a lot. Now we start to write our story")
                write_story()


def write_story():
    global story_value

    story_value = []
    name_value = ['name of main character', "friend's name", "place name", "your favourite dish", "color"]

    print("First of all, I need some information. \nYou also can imagine \nFirst of all we need the main character")
    print("What will we call it?")
    main_character = input()
    story_value.append(main_character)

    print("Our hero need friend. What name will you choose?")
    friend_name = input()
    story_value.append(friend_name)

    print("Also we need place. It seems to me that the name of some village is the right one, that we need choose")
    place_name = input()
    story_value.append(place_name)

    print("Since we have a New Year's story. Then what new year can not do without food.\nWhat is your favorite dish?")
    food_name = input()
    story_value.append(food_name)

    print("What is your favourite color?")
    color_name = input()
    story_value.append(color_name)

    print("Do uou want to change something? Yes/No")
    booling = input()

    if booling == "Yes":
        circle = True

        while circle:
            print("Ok, choose what you want to change")

            for count, name in enumerate(name_value):

                print(f'You want change {name}? Yes/No')
                decision = input()

                if decision == 'Yes':

                    print("On what do you want to change?")
                    change_el = input()
                    story_value[count] = change_el

                else:
                    continue

            print("That's all? Yes/No")
            final_answer = input()

            if final_answer == "Yes":
                circle = False

            else:
                continue

        loading()

    else:
        print("Ok in few seconds, you will have your story.")
        loading()


def loading():
    print("Oh... Yes it's time to get our story")
    print("Loading:")

    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")

    story(*story_value)

def story(main_character, friend_name, place_name, food, color):
    print(f"It was New Year's Eve. {main_character} sat alone at home and was sa"
          f"d. \nSuddenly a call rang, his friend called him - {friend_name}.\n A friend invited me to cel"
          f"ebrate the New Year at the dacha, called {place_name}. \nI was there for the first time, so the roof of the house s"
          f"erved as a reference point {color}. \nI drove into the village, saw the right house, and there are a lot of peopl"
          f"e there, {food} is preparing. \nI went into the yard, got acquainted. When asked where {friend_name} is, it was said that "
          f"{friend_name} went to the store, will be soon. \nI call him, but the phone is unavailable, the connection is bad. \nThe"
          f"y put me at the table, had a little snack and started heating the bathhouse.\n {friend_name} arrived, but, as it turn"
          f"ed out, not mine! I got the country villages mixed up. \nThat's how new friends appeared! <3")



def main():
    print("Hi, everyone. Have fun!")
    meeting()

