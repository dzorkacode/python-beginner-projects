def main():
    word_dictionary={
        'hi':'a friendly, informal, casual greeting said when meeting someone',
        'eye':'an organ through which animals see',
        'earth':'our planet, the third planet from the Sun'
    }


    while True:
        word=input("Enter the word you're looking for: ")
        if word=="":
            break
        elif word in word_dictionary:
            print(f"{word}: {word_dictionary[word]}")
        else:
            print('word not found')
    
main()