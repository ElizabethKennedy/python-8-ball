import sys
import random

# never ending loop:
while 1==1:
    # prompt for a question
    question = input("Ask the magic 8 ball a question: (press enter to quit)\n")

    if not question: 
        break
    print(random.choice(("It is certain", "Outlook good", "You may rely on it", "Ask again later", 
    "Concentrate and ask again",  "Reply hazy, try again", "My reply is no", "My sources say no",
     "Yes, definitely", "Outlook not so good", "Better not tell you now", "My sources say yes",
      "It is decidedly so", "Without a doubt", "As I see it, yes", "Most likely", "Yes", "Signs point to yes",
      "Cannot predict now", "Don't count on it", "Very doubtful" ),),"\n")