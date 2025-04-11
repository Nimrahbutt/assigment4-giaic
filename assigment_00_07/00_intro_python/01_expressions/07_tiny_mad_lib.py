SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my"

def main():
    adjective: str = input("Enter an adjective and press enter: ")
    noun: str = input("Enter a noun and press enter: ")
    verb: str = input("Enter a verb and press enter: ")

    print(f"{SENTENCE_START} {adjective} {noun} {verb}.")

if __name__ == "__main__":
    main()
