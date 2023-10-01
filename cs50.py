def main():
    num = get_num()
    meow(num)


def get_num():
    while True:
        n = int(input('>'))
        if n > 0:
            return n


def meow(n):
    print('******\n' * n)


main()
