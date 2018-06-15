input=raw_input("Please enter desired length: ")
length=[]
length.append(input) 
password = []
import random
charlist=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",".","=","+","-","_"]

print ("your new password is: ")

for i in range(int(input)):
  print (random.choice(charlist)),