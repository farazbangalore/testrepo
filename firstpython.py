print("Hello World...!")


def sum_numbers(numbers):
  if len(numbers) == 0:
    return 0
  return numbers[0] + sum_numbers(numbers[1:])
