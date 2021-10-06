# import modules

import sys
import random

ans = True

while ans:
    question = input("Ask the Magic 8 Ball a question:(Press Enter to exit)")
    
    

    answers = ["It is decidedly so", \
    "Ask again later", \
    "It is certain", \
    "Without a doubt", \
    "Yes definitely", \
    "You may rely on it.", \
    ]

    final = answers[random.randint(0, len(answers)) - 1]
return final