def main():
    print("Get the value for E = mc^2")
    m = int(input("Enter the Value for Mass (m) :: "))
    c = 300000000
    print(f"E = mc^2 Becomes :: {calcEVal(m,c)}")

def calcEVal(m,c):
    return m * getSquared(c)

def getSquared(c):
    return c * c

main()