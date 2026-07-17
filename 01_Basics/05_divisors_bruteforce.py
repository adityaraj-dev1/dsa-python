def divisors(num):
    result = []

    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)

    return result


num = int(input("Enter a number: "))
print(divisors(num))
