# rock, scissors, paper
import random

user = str(input())

items = ["rock", "scissors", "paper"]

n = random.randint(0, 2)
pc = items[n]
print(pc)

if (user == "rock" and pc == "scissors") or (user == "paper" and pc == "rock") or (user == "scissors" and pc == "paper"): print("user")
elif (user == "rock" and pc == "paper") or (user == "paper" and pc == "scissors") or (user == "scissors" and pc == "rock"): print("pc")      
else: print("none")    
