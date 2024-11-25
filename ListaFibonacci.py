def fibonacci_lista(n):
   if n <= 1:
    return n
   fib_list = [0, 1]  # Inicializamos la lista con los dos primeros términos
   for i in range(2, n):
    next_fib = fib_list[i-1] + fib_list[i-2]
    fib_list.append(next_fib)

   return fib_list