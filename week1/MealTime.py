def main() -> None:
    current_time = str(input('Whats time is it? '))
    print(convert(current_time))


def convert(time: str) -> str:
    hours, mints = time.split(':')
    formatted_time = int(hours) + int(mints) / 60
    if formatted_time >= 7 and formatted_time < 8:
        return 'Breakfast Time'
    elif formatted_time >= 12 and formatted_time <= 13:
        return 'Lunch time '
    elif formatted_time >= 18 and formatted_time <= 19:
        return 'Dinner Time'
    else:
        return

if __name__ == "__main__":
    main()