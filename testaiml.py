import aiml as AI
import os

mybot = AI.Kernel()
# If there is a brain file named standard.brn, Kernel() will initialize using bootstrap() method
if os.path.isfile("standard.brn"):
    mybot.bootstrap(brainFile="standard.brn")
else:
# If there is not brain file, load all AIML files and save a new brain
    mybot.bootstrap(learnFiles="startup.xml", commands="init")
    mybot.saveBrain("standard.brn")
while True:
    print mybot.respond(raw_input("Enter your message >> "))
