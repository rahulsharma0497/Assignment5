def sorted_squares(nums):
  """
  Returns an array of the squares of each number in nums sorted in non-decreasing order.

  Args:
    nums: An array of integers sorted in non-decreasing order.

  Returns:
    An array of the squares of each number in nums sorted in non-decreasing order.
  """

  squares = []
  for num in nums:
    squares.append(num * num)

  squares.sort()
  return squares


if __name__ == "__main__":
  print(sorted_squares([-4,-1,0,3,10]))