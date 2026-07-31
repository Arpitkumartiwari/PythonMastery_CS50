def main():
    str = input("Whats on your Mind? :: ")
    print(ConvertToSmiley(str))

def ConvertToSmiley(value):
    value = value.replace(":)","🙂").replace(":(","🙁")
    return value

main()