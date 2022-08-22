# create an advenced interpreter
# which can interpret language like
# "1 + 1 * 2 * (3 - 4) * 5"
# as "((1 + (1 * 2)) * ((3 - 4) * 5))"
# and return the result

# The operators +, -, *, /, (, ) and whitespace
# can be used only in this form

# The operator priority is
# "*" > "/" > "+" > "-" > "(" > ")"
# and they can be used only so that they
# do not break the "()" priority

# You can assume that the input is correct,
# that is, you need only to handle the
# operators "+", "-", "*", "/", "(", ")"
# and whitespace and you can
# assume that the input is valid Python code
# which does not include any other operators,
# such as //, **, +="...

# FOR YOUR OWN SAFETY
# YOU CAN USE ONLY THE
# LIST, DICT, SET, int, float, str
# BUILT-IN FUNCTIONS AND METHODS
# BUT NOT OTHER DATA STRUCTURES OR
# BUILT-IN FUNCTIONS AND METHODS
# BECAUSE SOME OF THEM MAY CAUSE
# INFINITE LOOP


def convert(expr):
    # you can convert the expr to whatever you want
    # but the function needs to return a str
    # the str will be evaluated by Python interpreter
    # and the result will be returned to the main function
    # which will print it
    # you can assume that the input is correct

    # you can use only the
    # list, dict, set, int, float, str
    # built-in functions and methods
    # but not other data structures or
    # built-in functions and methods
    # because some of them may cause
    # infinite loop

    # Example:
    # convert the expression "1 + 1 * 2 * (3 - 4) * 5" to
    # "((1 + (1 * 2)) * ((3 - 4) * 5))"

    # The expression is already a string
    # you can split it into a list
    # for example:

    expr = expr.replace(" ", "")
    expr = expr.replace("*", " * ")
    expr = expr.replace("/", " / ")
    expr = expr.replace("+", " + ")
    expr = expr.replace("-", " - ")
    expr = expr.replace("(", " ( ")
    expr = expr.replace(")", " ) ")

    expr = expr.split(" ")

    # expr = ["1", "+", "1", "*", "2", "*", "(", "3", "-", "4", ")", "*", "5"]
    # which is a list of strings

    # you can use a list to store the operator and operand
    # for example:

    # stack = []
    # for item in expr:
    #     stack.append(item)

    # stack = ["1", "+", "1", "*", "2", "*", "(", "3", "-", "4", ")", "*", "5"]
    # which is a list of strings

    # then you can write a loop to handle the operator and operand
    # for example:

    # for item in stack:
    #     if item == "+":
    #         print("addition")
    #     elif item == "-":
    #         print("subtraction")
    #     elif item == "*":
    #         print("multiplication")
    #     elif item == "/":
    #         print("division")
    #     else:
    #         print(item)


    # which will print the following:
    # 1
    # addition
    # 1
    # multiplication
    # 2
    # multiplication
    # (
    # 3
    # subtraction
    # 4
    # )
    # multiplication
    # 5

    # or you can use a dict to handle the operator and operand
    # for example:

    # stack = []
    # for item in expr:
    #     if item in ["+", "-", "*", "/"]:
    #         print("operator: " + item)
    #     else:
    #         print("operand: " + item)

    # which will print the following:
    # operand: 1
    # operator: +
    # operand: 1
    # operator: *
    # operand: 2
    # operator: *
    # operand: (
    # operand: 3
    # operator: -
    # operand: 4
    # operand: )
    # operator: *
    # operand: 5


    # you can also handle the operator and operand
    # in a different way

    # for example:

    # stack = []
    # for item in expr:
    #     stack.append(item)
    #     if item in ["+", "-", "*", "/"]:
    #         print(stack)
    #         stack.clear()

    # which will print the following:
    # ['1', '+']
    # ['1', '*']
    # ['2', '*']
    # ['(', '3', '-', '4', ')']
    # ['*', '5']

    # You can do whatever you want
    # but you need to return the result
    # as a string
    # so that it can be evaluated by Python interpreter
    # and the result will be returned to the main function

    # Example:
    # return "((1 + (1 * 2)) * ((3 - 4) * 5))"
    # which is the result of "1 + 1 * 2 * (3 - 4) * 5"

    # you can convert the expr to whatever you want
    # but the function needs to return a str
    # the str will be evaluated by Python interpreter
    # and the result will be returned to the main function
    # which will print it

    # You can not use the
    # list, dict, set, int, float, str
    # built-in functions and methods
    # because some of them may cause
    # infinite loop

    stack = []
    result = ""
    for i in expr:
        stack.append(i)
        if i in ["+", "-", "*", "/"]:
            stack.insert(0, "(" + "".join(stack[:-2]) + ")")
            stack.insert(2, i)
            stack.pop()
            stack.pop()
        if i == ")":
            stack.insert(0, "(" + "".join(stack[:-1]) + ")")
            stack.insert(2, "*")
            stack.pop()
            stack.pop()
        if i == "(":
            stack.insert(0, "(" + "".join(stack[:-1]) + ")")
            stack.insert(2, "*")
            stack.pop()
            stack.pop()
    result = "".join(stack)
    return result


def main():
    # testing part
    # you can change the value of expr to test your function
    # for example, you can change expr to "1 + 2 * 3 / (4 - 5)"
    # or "1 + 2 * 3 / (4 - 5)"
    expr = "1 + 1 * 2 * (3 - 4) * 5"

    # convert the expr to whatever you want
    # but the function needs to return a str
    result = convert(expr)
    print(result)


main()