# coding=utf-8
"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.

1) A square number can end only with digits 00,1,4,6,9, or 25 in base 10; So that eliminates 2 digits, we now end
with a 9.
2) Squares of odd numbers are odd.
3) If the last digit of a number is 3 or 7, its square ends in 9.

"""
import math


class Euler206:
    def test(self, n):
        N = str(n * n)
        if N[0] == '1':
            if N[2] == '2':
                if N[4] == '3':
                    if N[6] == '4':
                        if N[8] == '5':
                            if N[10] == '6':
                                if N[12] == '7':
                                    if N[14] == '8':
                                        if N[16] == '9':
                                            return True
        return False

    def solution(self):
        number = 0
        start = int(math.floor(math.sqrt(10203040506070809)))
        end = int(math.floor(math.sqrt(192939495969798999)))
        for i in range(start, end):
            if i % 2 == 0:
                if int(str(i)[-1]) == 3 or int(str(i)[-1]) == 7:
                    if self.test(i):
                        number = int(math.sqrt(int(str(i * i) + "00")))
                        break

        print "Answer =", number


if __name__ == '__main__':
    p = Euler206()
    p.solution()
