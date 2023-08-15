def valid_equation(equation):
    valid_chars = ['+', '-', '*', '/', '(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for char in equation:
        if char not in valid_chars:
            return False
    return True


def calculate(operand1, operator, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2


def cal_equation(equation):
    listnum = []
    list_op = []
    num = ""
    for i in range(len(equation)):
        if equation[i].isdigit():
            num = equation[i] + num
        else:
            list_op.append(equation[i])
            listnum.append(int(num))
            num = ""
    listnum.append(int(num))

    result = listnum[0]
    for i in range(len(list_op)):
        result = calculate(result, list_op[i], listnum[i + 1])

    return result


equation = input("Enter your equation: ")
if valid_equation(equation):
    result = cal_equation(equation)
    if result is not None:
        print("Result: ", result)
else:
    print("Invalid equation!")
