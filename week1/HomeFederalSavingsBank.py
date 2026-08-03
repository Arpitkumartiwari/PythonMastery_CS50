def main():
    greet = input('Greeting: ')
    checkForMoney(greet)

def checkForMoney(greet):
    greet = greet.strip()
    if greet.startswith('hello'):
        print('$0')
    elif greet.startswith('h') and greet.split(" ")[0].casefold() != 'hello':
        print('$20')
    else:
        print('$100')

main()