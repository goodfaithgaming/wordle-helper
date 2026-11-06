def valid(word, state):
    for i in range(5):
        if state[word[i]][i] is False:
            return False
        for letter in "qwertyuiopasdfghjklzxcvbnm":
            if state[letter][i] is True:
                if letter != word[i]:
                    return False
    return True

def main():
    with open("words/valid-wordle-words.txt", "r", encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]
    
    state = dict(zip("qwertyuiopasdfghjklzxcvbnm", [[None for _ in range(5)] for _ in range(26)]))

    while True:
        word = input("Guess: ").lower()
        print("Per-character clues are of the format Y/M/N, meaning here/elsewhere/nowhere, respectively")
        clues = input("Clues: ").upper() # Y/M/N here/elsewhere/nowhere, respectively

        for i in range(5):
            if clues[i] == "Y":
                state[word[i]][i] = True
            elif clues[i] == "M":
                state[word[i]][i] = False
            elif clues[i] == "N":
                state[word[i]] = [False, False, False, False, False]
        
        for word in lines:
            if valid(word,state):
                print(word)

if __name__ == "__main__":
    main()
