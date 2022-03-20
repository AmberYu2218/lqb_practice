if __name__ == '__main__':
    a = int(input(), 16)
    if 0 <= a <= int('FFFFFFFF', 16):
        print(a)