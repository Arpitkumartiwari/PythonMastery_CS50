def main() -> None:
    
    amount_due = 50
    
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        
        coin = int(input("Please Insert a Coin: "))
        
        if coin in (5,10,25):
            amount_due -= coin
        else:
            print("please insert Coin in 5, 10, 25 !")

    print(f"Change Owed: {amount_due}")
    
if __name__ == "__main__":
    main()