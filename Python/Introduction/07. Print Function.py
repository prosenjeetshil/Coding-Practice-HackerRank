if __name__ == '__main__':
    n = int(input())
    result = []

    for number in range(1, n + 1):
        result.append(str(number))
    print("".join(result))
