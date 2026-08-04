import random
import string

ALL_CHARS = (
    list(string.ascii_uppercase)
    + list(string.ascii_lowercase)
    + list(string.digits)
    + list(string.punctuation)
)


def get_password_length(max_length:int) -> int:

    """
    check for negative Scenarios and Return Length of password
    """

    while True:
        pass_length = input('Please Enter Length of Password to be generated: ')
        
        if not pass_length.isdigit():
            print('Please Enter Correct Password Length in Numeric Values')
            continue
        
        pass_length = int(pass_length)
        
        if pass_length < 0 or pass_length > max_length:
            print(f"Password length should be between 1 and {max_length}")
            continue
        return pass_length
    

def generate_password(length: int) -> str:
    """
    generate random password upto provided length
    """
    return "".join(random.sample(ALL_CHARS,length))



def main() -> None:
    """
    Application Entry Point
    """
    
    passLength = get_password_length(len(ALL_CHARS))
    password = generate_password(passLength)
    
    print(f"\n Your System Generated Strong Password is: {password}")
    

if __name__ == "__main__":
    main()