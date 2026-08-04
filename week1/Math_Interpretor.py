VALID_OPERATORS = {'+', '-', '*', '/'}

def get_expression_list() -> list:
    while True:
        expression = input('Please Enter your Maths Expression : ')
        expression_list = []
        expression_list.extend(expression.split(" "))
        if len(expression_list) != 3:
            print("Expression must be: number operator number")
            continue
        if not (expression_list[0].isdigit() and expression_list[2].isdigit()):
            print('Please Enter a Correct Value')
            continue
        if expression_list[1] not in VALID_OPERATORS:
            print('Please Enter a Operator')
            continue
        return expression_list

def get_result(expr_list: list) -> float:
    val1, operator, val2 = expr_list
    
    if operator == '+':
        return val1 + val2
    elif operator == '-':
        return val1 - val2
    elif operator == '*':
        return val1 * val2
    elif operator == '/':
        return val1 / val2

def main() -> None:
    expression_list = get_expression_list()
    result = get_result(expression_list)

    print('\n ------------------------------------')
    print(f"Result : {result:.2f}")


if __name__ == "__main__":
    main()