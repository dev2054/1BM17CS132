import string
import random


def password(userinput):
    specialcharacter = [random.choice(string.punctuation)
                        for character in range(userinput)
                        ]
    
    Lower = [random.choice(string.ascii_lowercase)
                 for lower in range(userinput)
             ]
    
    Upper = [random.choice(string.ascii_uppercase)
                 for upper in range(userinput)
             ]
    
    numbers = [random.choice(string.digits)
               for number in range(userinput)
               ]
    generatePassword = ''.join(specialcharacter + Lower + Upper + numbers)
    print(generatePassword)
    
    generatedPassword = ''.join(random.choice(generatePassword)
                                for value in range(userinput))
    return generatedPassword


size=8
pwd= password(size)
print(pwd)
