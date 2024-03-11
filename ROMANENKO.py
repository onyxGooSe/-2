def left_side(n):
    sum1 = sum([(i*5) for i in range(1, n+1)])
    sum2 = sum([(i*7) for i in range(1, n+1)])
    return sum1 + sum2

def right_side(n):
    sum_n = sum([i for i in range(1, n+1)])
    return 2 * (sum_n**4)

def check_equality(n):
    return left_side(n) == right_side(n)

N = 10  # Задаем значение N

for i in range(1, N+1):
    if check_equality(i):
        print(f"Утверждение верно для n={i}")
    else:
        print(f"Утверждение неверно для n={i}")
