from random import choice, randint

# def get_response(user_input: str) -> str:
#     raise NotImplementedError("Code has not been added yet.")

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == "":
        return("Well you are awfully silent ...")
    elif "hello" in lowered:
        return("Hello, there!")
    elif "how are you" in lowered:
        return "Good, thanks!"
    elif "bye" in lowered:
        return "See you!"
    elif "roll dice" in lowered:
        return f"🎲 You rolled: {randint(1, 6)}"
    else:
        return choice(["Random 1", "Random 2", "Random 3", "I don't understand."])