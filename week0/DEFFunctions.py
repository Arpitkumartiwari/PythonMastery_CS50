"""def hello(name='World'):
        print(f"Hello There {name}")

fname = input("whats your name? ::  ")
hello(fname)
hello()
"""


def main():
    name = input("Whats your name ?? ::  ")
    hello(name)
    hello()
    print(squarefunc())
    print(powerfunc())

def hello(to="world"):
    print(f"Hello, {to}")

def squarefunc():
    x = float(input("enter a No to be squared :: "))
    return x * x;

def powerfunc():
    no = int(input("enter the no :: "))
    toThePower = int(input("enter the power :: "))
    return pow(no, toThePower)


main()