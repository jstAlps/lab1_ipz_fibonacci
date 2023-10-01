def fibonacci(n):
    fib = [0, 1]  # Початкові значення для чисел Фібоначчі 0 та 1

    if n <= 0:
        return "Введіть додатнє ціле число."
    elif n == 1:
        return fib[0]
    elif n == 2:
        return fib[1]
    else:
        for i in range(2, n):
            next_fib = fib[i - 1] + fib[i - 2]
            fib.append(next_fib)
        return fib[-1]


# Введіть число n, для якого ви хочете знайти число Фібоначчі
n = int(input("Введіть ціле число n: "))

result = fibonacci(n)
if isinstance(result, str):
    print(result)
else:
    print(f"Число Фібоначчі для n={n}: {result}")
