def make_sentence(word, part_of_speech):
    # Check the part of speech and generate the sentence accordingly
    if part_of_speech == 0:
        # If part_of_speech is 0, it's a noun
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        # If part_of_speech is 1, it's a verb
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        # If part_of_speech is 2, it's an adjective
        print(f"Looking out my window, the sky is big and {word}!")

def main():
    # Prompt the user for input
    word = input("Please type a noun, verb, or adjective: ")
    part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
    
    # Call the make_sentence function to generate and print the sentence
    make_sentence(word, part_of_speech)

# Call the main function to run the program
if __name__ == "__main__":
    main()
