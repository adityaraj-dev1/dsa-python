def divisors(num):
    result = []

    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            result.append(i)

            if i != num // i:
                result.append(num // i)

    return sorted(result)


num = int(input("Enter a number: "))
print("Divisors:", divisors(num))
