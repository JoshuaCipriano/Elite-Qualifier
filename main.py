import random


def generate_joke(user_input):
    jokes = [
        "I'm afraid for the calendar. Its days are numbered.",
        "Why do fathers take an extra pair of socks when they go golfing? In case they get a hole in one!",
        "What did the ocean say to the beach? Nothing, it just waved.",
        "Where do fruits go on vacation? Pear-is!",
        "I asked my dog what's two minus two. He said nothing.",
        "What did Baby Corn say to Mama Corn? Where's Pop Corn?",
        "Why couldn't the bicycle stand up by itself? It was two tired.",
        "Why can't a nose be 12 inches long? Because then it would be a foot.",
        "What do you call it when a snowman throws a tantrum? A meltdown.",
        "I have a joke about chemistry, but I don't think it will get a reaction.",
        "What does a bee use to brush its hair? A honeycomb!",
        "That car looks nice but the muffler seems exhausted.",
        "Have you ever tried to catch a fog? I tried yesterday but I mist.",
        "I've got a great joke about construction, but I'm still working on it.",
    ]
    return random.choice(jokes)


def init_chat():
    quit_character = 'bye'

    user_input = input("Hello, want to hear a joke? (Type 'bye' to quit)\n")

    while user_input != quit_character:
        user_input = input(generate_joke(user_input) + "\n")
        if user_input == "Not funny":
            print("You're not funny. Here have another joke.")
        elif user_input == "That was funny":
            print("Thanks, here have another joke.")
        elif user_input == "Wow":
            print("Hilarious right?")
        elif user_input == "Sure":
            print("Here we go.")
        elif user_input == "No way":
            print("Come on its funny.")
        elif user_input == "One more":
            print("Sure, how about this one.")
        elif user_input == "Already heard this one":
            print("Ok don't have to be so rude about it.")


if __name__ == "__main__":
    init_chat()
