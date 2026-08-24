FruitCal = {
    'Apple': 130,
    'Avocado': 50,
    'Banana': 110,
    'Cantaloupe': 50,
    'Grapefruit': 60,
    'Grapes': 90,
    'Honeydew Melon':50,
    'Kiwifruit': 90,
    'Lime': 15,
    'Nectarine': 20,
    'Orange': 60,
    'Peach': 80,
    'Pear': 60,
    'Pineapple': 100,
    'Plums': 50,
    'Strawberries': 70,
    'Sweet Cherries': 50,
    'Tangerine': 100,
    'Water Melon': 80,
}

def caloric_value(fruit: str) -> int:
    for name, calories in FruitCal.items():
        if name.casefold() == fruit.casefold():
            return calories
            
def main() -> None:
    fruit = input("Please Enter Fruit: ")
    print(caloric_value(fruit))

if __name__ == "__main__":
    main()
