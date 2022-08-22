# define a class to build a interpreter programming language


class Interpreter(object):

    def __init__(self, text):
        # Tokenize the input string
        self.tokens = self.tokenize(text)

    def tokenize(self, text):
        return text.split()

    def eval(self):
        # Initialize the stack
        stack = []
        # Loop through each token
        for token in self.tokens:
            try:
                # if the token is an integer push it to the stack
                stack.append(int(token))
            except ValueError:
                # evaluate operators and functions
                function = OPERATORS[token]
                args = stack.pop(), stack.pop()
                # Evaluate the function and push the result back to the stack
                result = function(*args)
                stack.append(result)
        # Return the result of the calculation
        return stack[0]


# Define operators
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return int(a / b)

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}

def main():

    while True:
        # Get user input
        text = input('rpn calc> ')
        # If the input is 'q', quit
        if text == 'q':
            return

        # Evaluate the input and print the result
        result = Interpreter(text).eval()
        print(result)

if __name__ == '__main__':
    main()