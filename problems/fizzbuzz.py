from typing import List
class Solution:
  def fizzBuzz( n: int) -> List[str]:
    answers = []
    for i in range(1, n):
      if i % 3 == 0:
        answers.append("Fizz")
      elif i % 3 == 0 and i % 5 == 0:
        answers.append("Buzz")
      else:
        answers.append(i)
    return answers

  print(fizzBuzz(5))