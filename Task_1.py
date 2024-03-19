from nltk.tokenize import word_tokenize, sent_tokenize

enteredText = input("Enter Your Text : ")

print("\nChoose an option : \n 1-print tokenized words \n 2-print tokenized sentences \n 3-print output using split function.")
userChoice = int(input("\nEnter Your Choice : "))

while(userChoice <1 or userChoice>3):
    print("\nPlease choose a valid option")
    userChoice = int(input("Enter Your Choice : "))

if userChoice == 1:

    tokenized_words = word_tokenize(enteredText)

    i = 0
    while i < len(tokenized_words) - 1:
        if tokenized_words[i].istitle() and tokenized_words[i + 1].istitle():
            tokenized_words[i] += " " + tokenized_words[i + 1]
            del tokenized_words[i + 1]
        else:
            i += 1

    print(tokenized_words)
elif userChoice == 2:
    tokenized_sentences = sent_tokenize(enteredText)
    print(tokenized_sentences)
else:
    words = enteredText.split(" ")
    sentences = enteredText.split(".")
    print(f"words = {words}")
    print(f"sentences = {sentences}")
