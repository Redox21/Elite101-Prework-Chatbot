#Elite 101 - C2C Wave 5 2023 - Chatbot
import random

#Random Functions
def awkward():
  print(".......")

def printLine():
  print("")
  
q1= ["How's the weather", "How are you doing", "What's your favorite color..."]
q2 = random.choice(q1)

f1 = ["interesting...", "fascinating...", "Well I think that's pretty cool"]
f2 = random.choice(f1)

#def feedback():
def question(q2):
  print(f'Well...{q2}?')

##Chatbot could ask about weather, current condition, emotional status...

#Actual Program

print("Hello, I am a ChattyBox. I can chat and I am not a box.")
name = input("So what is your name friend??? ")

print(f'Well welcome, {name} Its nice meeting you.')

awkward()
printLine()

#Chat1 with a question/feedback
input(q2 + "? ")

#Still Working on adding additional chat features, but I'll leave it like this for now
print(f2 + " do you have any more questions?")
awkward()

print(f"Okay fine ignore me, it was nice meeting you {name}.")





