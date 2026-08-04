import re


def get_password_strength_score(password: str) -> str:
    if len(password) < 8:
        return "WEAK ! password must be more than 8 characters !!"
    elif not any(char.isupper() for char in password):
        return "WEAK ! Password must have atleast one character in UpperCase !!"
    elif not any(char.islower() for char in password):
        return "WEAK ! Password must have atleast one character in LowerCase !!"
    elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return (
            "MEDIUM ! password must contain a special character to improve strength !!"
        )

    else:
        return "STRONG ! Password is Secure !!"


def password_checker() -> None:

    print("Welcome To Password Strength Checker !!!")

    while True:
        password = str(
            input('Please Enter Your Password ! (type "EXIT" or "QUIT" to stop): ')
        )

        if password.casefold() == "exit" or password.casefold() == "quit":
            print("Thankyou for using Password Strength Checker !!! Bye !")
            break
        result = get_password_strength_score(password)
        print(result)


def main() -> None:
    password_checker()


if __name__ == "__main__":
    main()
