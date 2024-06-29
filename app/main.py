import os

clear = lambda: os.system('clear')

print("Welcome to my world, what is your character's name?")
name = input()
health = 100
clear()
print(f"Welcome {name}, I hope today isn't too tiring yet. We're going to spice things up")

print("What would you like to do? \n 1) Ask silly questions \n 2) Play bikes")
activity = float(input())
clear()
match activity:
  case 1:
    print("So you want to ask me a silly question do you...")
    print("I guess we'll have to take some hp away for wasting my time...")
    health = health - 10
    print(f"Your health is now at {health}")
  case 2:
    print("Playing Bikes sounds like a fun time")
    print("Here's a health booster because it sounds like a good time")
    health = health + 10
    print(f"Your health is now at {health}")
