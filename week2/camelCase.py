def convert_to_snake_case(str: str) -> str:
    converted_str = ""
    
    for s in str:
        if s.isupper():
            converted_str += "_"+s.lower()
        else:
            converted_str += s.lower()
    
    return converted_str

def to_snake_case(value: str) -> str:
    return "".join(
        f"_{char.lower()}" if char.isupper() else char for char in value
    ).lstrip("_")

def main() -> None:
    value = input("please Input the String to be converted to Snake Case: ")
    snake_case_value = convert_to_snake_case(value)
    print(snake_case_value)
    
    print("Pro Version:",to_snake_case(value))

if __name__ == "__main__":
    main()