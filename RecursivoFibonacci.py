def fibonacci_recursivo(n):
  """Calcula el enésimo número de Fibonacci de forma recursiva.

  Args:
    n: La posición del número a calcular.

  Returns:
    El enésimo número de Fibonacci.
  """

  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)