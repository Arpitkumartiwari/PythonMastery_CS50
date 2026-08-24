def remove_vowel(val: str) -> str:
    vowels = "aeiouAEIOU"
    
    for v in vowels:
        val = val.replace(v,"")
    
    return val

def main() -> None:
    print(remove_vowel(input("please enter the Value: ")))

if __name__ == "__main__":
    main()