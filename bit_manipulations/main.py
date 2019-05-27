from bit_manipulations import set_bit, clear_bit, flip_bit


def main():
    # result = set_bit(0b0000110, 0b00000000)
    print('Binary of 7', bin(7))
    print('Binary of 3', bin(3))
    print('Now setting 4th bit')
    result = set_bit(7, 3)
    print(result)
    print('Binary Result', bin(result))

    print('Binary of 6', bin(6))
    print('Binary of 2', bin(2))
    print('Now clearing 3rd bit')
    result = clear_bit(6, 2)
    print(result)
    print('Binary result', bin(result))

    print('Binary of 102', bin(102))
    print('Binary of 2', bin(2))
    print('Now flipping 3rd bit')
    result = flip_bit(102, 2)
    print(result)
    print('Binary result', bin(result))


if __name__ == '__main__':
    main()
