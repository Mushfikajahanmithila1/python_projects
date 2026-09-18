import random
import string

character = string.ascii_letters + string.digits + string.punctuation

length = 10

ranpass = "".join(random.choice(character) for i in range(length))
print(f"Random password is: {ranpass}")