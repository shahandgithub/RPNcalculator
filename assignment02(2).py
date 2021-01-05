class MyStack:
    # Constants
    MAX_SIZE = 100000
    DEFAULT_SIZE = 10

    def __init__(self, default_item, capacity=DEFAULT_SIZE):
        # If the capacity is bad, fail right away
        if not self.valid_capacity(capacity):
            raise Exception("Capacity " + str(capacity) + " is invalid")
        self.capacity = capacity
        self.default_item = default_item

        # Make room in the stack and make sure it's empty to begin with
        self.clear()

    def push(self, item_to_push):
        if self.is_full():
            raise Exception("Push failed - capacity reached")
        elif type(item_to_push) != type(self.default_item):
            raise Exception("Push failed - wrong type for item")

        self.stack[self.top_of_stack] = item_to_push
        self.top_of_stack += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Pop failed - stack is empty")

        self.top_of_stack -= 1
        return self.stack[self.top_of_stack]

    def clear(self):
        # Allocate storage the storage and initialize top of stack
        self.stack = [self.default_item for _ in range(self.capacity)]
        self.top_of_stack = 0

    def is_empty(self):
        return self.top_of_stack == 0

    def is_full(self):
        return self.top_of_stack == self.capacity

    def get_capacity(self):
        return self.capacity

    # class methods ------------------------
    @classmethod
    def valid_capacity(cls, test_capacity):
        return 0 <= test_capacity <= cls.MAX_SIZE


class RpnCalculator:
    ADD = '+'
    MUL = '*'
    DIV = '//'
    SUB = '-'

    def __init__(self):
        None

    @staticmethod
    def eval(rpn_expression):
        RpnCalculator.eval_tokens(RpnCalculator.parse(rpn_expression))

    @staticmethod
    def parse(rpn_expression):
        return rpn_expression.split()

    @staticmethod
    def eval_tokens(tokens):
        Stack = MyStack(1, len(tokens))

        i = 0
        while i < len(tokens):
            try:
                op = int(tokens[i])
                Stack.push(op)

            except ValueError:
                operand = tokens[i]
                if operand == RpnCalculator.ADD:
                    try:
                        op1 = Stack.pop()
                        op2 = Stack.pop()

                    except Exception as e:
                        print("Not a valid expression. Exception: ", e)
                        return

                    result = op1 + op2
                    Stack.push(result)

                elif operand == RpnCalculator.SUB:
                    try:
                        op1 = Stack.pop()
                        op2 = Stack.pop()

                    except Exception as e:
                        print("Not a valid expression. Exception: ", e)
                        return

                    result = op2 - op1
                    Stack.push(result)

                elif operand == RpnCalculator.DIV:
                    try:
                        op1 = Stack.pop()
                        op2 = Stack.pop()

                    except Exception as e:
                        print("Not a valid expression. Exception: ", e)
                        return

                    result = int(op2 // op1)
                    Stack.push(result)

                elif operand == RpnCalculator.MUL:
                    try:
                        op1 = Stack.pop()
                        op2 = Stack.pop()

                    except Exception as e:
                        print("Not a valid expression. Exception: ", e)
                        return

                    result = RpnCalculator.multiply(op1, op2)
                    Stack.push(result)

                else:
                    print("Not a valid Rpn Expression")
                    print("Not enough operator")
                    return

            i += 1;
        try:
            result = Stack.pop()

        except Exception as e:
            print("Not a valid expression. Exception: ", e)
            return

        if Stack.is_empty():
            print("The result of this expression is ", result)

        else:
            print("Not a valid Rpn Expression")
            return

    @staticmethod
    def multiply(a, b):
        if b == 0:
            return 0
        else:
            return a + RpnCalculator.multiply(a, b - 1)


def test():
    Expressions = []
    Expression1 = "3"
    Expression2 = "2 3 +"
    Expression3 = "2 3 -"
    Expression4 = "1 1 1 + -"
    Expression5 = "1 1 + -"
    Expression6 = "1 1"
    Expression7 = "1 1 fly"
    Expression8 = "This is Shahand"
    Expression9 = "4 -5 *"
    Expression10 = "20 5 //"
    Expression11 = "15 7 1 1 + - // 3 * 2 1 1 + + -"
    Expression12 = "1000 990 1 2 + * +"

    Expressions.append(Expression1)
    Expressions.append(Expression2)
    Expressions.append(Expression3)
    Expressions.append(Expression4)
    Expressions.append(Expression5)
    Expressions.append(Expression6)
    Expressions.append(Expression7)
    Expressions.append(Expression8)
    Expressions.append(Expression9)
    Expressions.append(Expression10)
    Expressions.append(Expression11)
    Expressions.append(Expression12)

    i = 0
    while i < 12:
        try:
            RpnCalculator.eval(Expressions[i])

        except Exception as e:
            print("Exception: ", e)

        i += 1


if __name__ == "__main__":
    test()

"""
 * Something like that you use to decrease the redundancy in your code for the 4 operands 
ops = {
  "+": (lambda a, b: a + b),
  "-": (lambda a, b: a - b),
  "*": (lambda a, b: a * b),
  "/": (lambda a, b: a / b)
}

def eval(expression):
  tokens = expression.split()
  stack = []

  for token in tokens:
    if token in ops:
      arg2 = stack.pop()
      arg1 = stack.pop()
      result = ops[token](arg1, arg2)
      stack.append(result)
    else:
      stack.append(int(token))

  return stack.pop()
"""