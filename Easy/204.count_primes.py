# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


class Solution:
    def countPrimes(self, n: int) -> int:


        # prime_set = set()
        isPrime = [0]*(n+1)

        count = 0


        i = 2
        while i * i <= n:
            # if i in prime_set:
            if isPrime[i] == 1:
                # print('found: ', i)
                i+=1
                continue
            # while j<= n:

            for c in range(i, (n//i)+1):
                # k = j*c
                # if k > n:
                #     break
                # prime_set.add(i*c)
                isPrime[i*c] = 1

            i+=1

        k = 2
        while k < n:
            # if k not in prime_set:
            if isPrime[k] == 0:
                count += 1
            k+=1


        return count

        #Without opt.
        def isPrime(n):
            print(n)
            # for i in range(2, int(n**0.5)+1):
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i+=1
            return True


        count = 0

        if n > 2:
            count+=1

        for i in range(3, n, 2):
            if isPrime(i):
                count += 1
        return count
