from stack import Stack

def is_balance(str):
    brackets_stack = Stack()
    for char in str:
        if char not in ['(', '[', '{', '}', ']', ')']:
            continue
        if char in ['(', '[', '{']:
            brackets_stack.push(char)
        else:
            popped_bracket = brackets_stack.pop()
            if (char == ']' and popped_bracket != '[') \
                    or (char == ')' and popped_bracket != '('):
                return False
    return brackets_stack.empty()


def main():
    if is_balance("Hello (how) [are] you?"):
        print('It is balance')
    else:
        print('Not balanced')


if __name__ == '__main__':
    main()