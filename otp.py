#program for the OTP generator
import random

otp = random.randrange(100000,1000000)
print(otp)

user = int(input('Enter the otp:'))
if otp == user:
    print('Generated!!')
else:
    print('Denied!!')
