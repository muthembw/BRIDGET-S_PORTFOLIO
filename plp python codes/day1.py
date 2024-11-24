import random

def display_joke():
    # List of programming jokes
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🪲",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings. 😢",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem. 💡",
        "Why do Python programmers prefer snakes? Because they don’t need braces. 🐍",
        "Why did the programmer quit his job? He didn’t get arrays. 😂",
        "What is a programmer’s favorite hangout place? The foo bar. 🍸",
        "Why are Assembly programmers often shorter? Because they can’t grow beyond their bytes. 🤏",
        "Why was the function feeling stressed? It had too many calls to handle! 📞",
        "Why don’t programmers like nature? It has too many bugs. 🦟",
        "What do you call 8 hobbits? A hobbyte. 🧙‍♂️",
    ]

    # Randomly select a joke
    joke = random.choice(jokes)
    print("\nHere’s a joke for you: 😂")
    print(joke)

# Main function
if __name__ == "__main__":
    display_joke()
