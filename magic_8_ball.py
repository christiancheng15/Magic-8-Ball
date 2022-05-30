from random import randint
import time

# DO NOT TOUCH
magic_8_ball_responses = ["It is certain.", "It is decidely so.", "Without a doubt", "Yes definitely", "You may rely on it.", "As I see it, yes.", "Most likely", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

# USER INPUT
q1 = input("What is your name? ")
print(f"Welcome {q1} to the Magic 8 Ball!")
q2 = input("Fees: $1 per question. Do you wish to continue? [y/n] ")
if q2.lower() == "y":
    user_question = input("What do you want to know? ")
    input("Press ENTER to shake")
    thinking_time = randint(1,5)
    if thinking_time > 1:
        time.sleep(thinking_time)
        print("Give me a few more seconds...")
        time.sleep(thinking_time)
        print(magic_8_ball_responses[randint(0,len(magic_8_ball_responses))])
    else:
        time.sleep(thinking_time)
        print(f"This is an easy one. {magic_8_ball_responses[randint(0,len(magic_8_ball_responses))]}")
    print(f"Thank you for stopping by. That will be $1.")
    input("Card or Cash? ")
    print("Only joking, its on the house. Have a nice day.")
    input("Press ENTER to exit")
else:
    print("Thank you for stopping by. Have a nice day.")
    input("Press ENTER to exit")