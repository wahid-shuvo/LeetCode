import math
class Solution:
    def countPrimes(self, n: int) -> int:
        initial_list = list(range(2, n+1))
        prime_list = []
        if n == 0:
          return n
        elif n == 1:
          return 0
        elif n == 3:
          return 1
        num = 2
        for i in range(2, int(math.sqrt(n))+1):
            prime_list = [0 if item % num == 0 and item!=num else item for item in initial_list]
            print(prime_list)
            for j in prime_list:
                if j != 0 and j > num:
                    num = j
                    break
            initial_list = prime_list
        num_of_primes=len([item for item in prime_list if item!=0])
        if n in prime_list:
            print(num_of_primes-1)
        else:
            print(num_of_primes)

x=Solution()
x.countPrimes(12)
