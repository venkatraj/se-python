def set_bit(x, position):
    mask = 1 << position
    return x | mask


def clear_bit(x, position):
    mask = 1 << position
    return x & ~mask


def flip_bit(x, position):
    mask = 1 << position
    return x ^ mask
