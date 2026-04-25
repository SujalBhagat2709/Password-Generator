import random
import string

def generate_strong_password(length=12):
    
    chars = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*"
    )
    
    password = "".join(random.choice(chars) for _ in range(length))
    
    return password


if __name__ == "__main__":
    
    print(generate_strong_password())