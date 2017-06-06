print("Hello, world")


def string_bits(str):
    temp = ""
    for i in range(0, len(str), 2):
        temp = temp + str[i]
    return temp
