from stack import Stack


def main():
    my_stack = Stack()
    print(my_stack)
    my_stack.push(10)
    print(my_stack.empty())
    print(my_stack)
    my_stack.push(20)
    print(my_stack)
    my_stack.push(30)
    print(my_stack)
    print(my_stack.peek())
    popped_data = my_stack.pop()
    print(popped_data)
    print('Empty?: ', my_stack.empty())
    print(my_stack)


if __name__ == '__main__':
    main()
