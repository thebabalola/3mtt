#Pig Latin

# ------- Ahoy! (or Should I Say Ahoyay!) -------
print('Pig Latin')


# ------ Input! ------
name = input("What's your name?")
print(name)
 
 # .isalpha()
x = "J123"
x.isalpha() # method to know if strings contains only letters


# ------- Check Yourself! ------
print('Welcome to the Pig Latin Translator!')

pyg = 'ay' # will append ay to the end of each word
original = input("Enter a word: ")  #receives user input and store inoriginal variable

if len(original) > 0 and original.isalpha():   # checkas to see if user inputs any word/character more than 0 and is an alphabet
  word = original.lower()  #coverts all character to lowercase and stores in word
  first = word[0]		# takes first charcter of the word inputed
  
  new_word = word + first + pyg  #concertenates 
  new_word = new_word[1:len(new_word)]	# slices first character index of the word inputed

  print(new_word)
else:
  print('empty')

