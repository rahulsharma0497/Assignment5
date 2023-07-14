def staircase(n):
  """
  Returns the number of complete rows of a staircase with n coins.

  Args:
    n: The number of coins.

  Returns:
    The number of complete rows of the staircase.
  """

  rows = 0
  while n > 0:
    rows += 1
    n -= rows
  return rows


if __name__ == "__main__":
  print(staircase(5))