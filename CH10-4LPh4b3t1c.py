print ('-='*30,'\n4LPH4B3t1c\n','-='*30)
word = input("Enter a word: ").strip()
abc = ("abcdefghijklmnopqrstuvxz")
for letter in word.lower():
    if letter.isalpha():
        print(f"The letter {letter} is the {abc.index(letter)+1}° of the ABC")