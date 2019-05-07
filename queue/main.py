from queue import Queue


def main():
    myQueue = Queue()
    myQueue.enqueue('Venkat')
    myQueue.enqueue('Raj')
    myQueue.enqueue('Hari')
    print(myQueue)
    print(myQueue.dequeue())
    print(myQueue)
    print(myQueue.empty())
    print(myQueue.dequeue())
    print(myQueue.dequeue())
    print(myQueue)
    print(myQueue.empty())


if __name__ == '__main__':
    main()