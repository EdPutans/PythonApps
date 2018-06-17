spisok = ["apple", "banana", "orange", "lemon", "tomato" , "maracuya"] 

import random
word = random.choice(spisok) # word - word from list
splited = list(word)      #debugging

spisok2 = []
import collections
compare = lambda spisok, spisok2: collections.Counter(spisok) == collections.Counter(spisok2)
  
n=6 #number of total attempts
gg = raw_input("Hi. welcome to hangman. You have 6 attempts to guess a fruit. The word has " + str(len(word)) + " letters in it. Try to guess letters and when you are ready - enter the complete word to win absolutely nothing:")
if splited.count(gg) == 2:
  spisok2.append(gg)
elif splited.count(gg) == 3:
  spisok2.append(gg)
  spisok2.append(gg)
  
while gg != str(word): 
  if gg == gg in splited:
      #this algorythm to be analyzed:
    if gg in splited:
      counter = 0
      elem_pos = []
      for i in splited:
        if i == gg:
          elem_pos.append(counter+1)
        counter = counter + 1
      print("Letter appears in positions " + str(elem_pos))
    
      spisok2.append(gg)
      print(spisok2)
      if compare(splited, spisok2) == True:
          print ("WELL DONE. The word was " +str(word))
          break
      else:
        gg = raw_input("good job. your letter repeats  " + str(splited.count(gg)) + " time(s). Next letter: ")
        if splited.count(gg) == 2:
          spisok2.append(gg)
        else:
            if splited.count(gg) == 3:
              spisok2.append(gg)
              spisok2.append(gg)
  else:
       if n >= 2: 
        gg = raw_input("nope, you have " + str(n-1) + " attempts left.. Your letter is ")
        n = n-1
       else:
         print ("sorry, you lost. The word was " + str(word))
         break
while gg == str(word):
  print("good job smart boi")
  break
