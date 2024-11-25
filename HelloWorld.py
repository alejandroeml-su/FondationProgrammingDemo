def fibonacci_lista(n):
    n=3
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_list = [0, 1]
    while len(fib_list) < n:
      fib_list.append(fib_list[-1] + fib_list[-2])
      return print("",fib_list[n])  