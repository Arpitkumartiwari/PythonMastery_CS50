str = "\n!!!!! Topic of Strings !!!!!\n"

intro = input("Kindly introduce yourself.\n")

print(str)

### Remove Leading or Trailing WhiteSpaces
intro = intro.strip()
print(f"intro :: {intro}", )


### Capitalize the First Words First Letter
intro = intro.capitalize()
print(f"Capitalized intro :: {intro}")

### Capitalize First Letter of Every Word
intro = intro.title()
print(f"Title Intro :: {intro}")


intro2 = input("\nKindly introduce yourself.\n")

### Combining These Commands
intro2 = intro2.strip().capitalize()
print(f"Combined Capitalize :: {intro2}")
intro2 = intro2.strip().title()
print(f"Combined Title :: {intro2}")


### Best way to do it 

intro3 = input("\nKindly introduce yourself.\n").strip().title()

print("Best way to do it :: "+intro3)
