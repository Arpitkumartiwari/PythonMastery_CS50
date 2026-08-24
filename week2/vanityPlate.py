import string


def validate_plate(plate: list) -> str:

    invalid = "Invalid"
    valid = "Valid"
    
    if not 2 <= len(plate) >= 6:
        return invalid

    if plate[0].isdigit() or plate[1].isdigit():
        return invalid

    if not plate[-1].isdigit() and plate[-2].isdigit():
        return invalid

    if not "".join(plate).isalnum():
        return invalid
    
    digit_started = False
    
    for char in plate:
        if char in string.punctuation or char.isspace():
            return invalid
        elif char.isdigit():
            if not digit_started and int(char) == 0:
                return invalid
        
            digit_started = True
        elif digit_started:
            return invalid
            

    return valid


def main() -> None:
    value = list(input("Please enter the Vanity Plate you want to request: "))
    print(validate_plate(value))


if __name__ == "__main__":
    main()
