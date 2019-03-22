from functools import reduce
from fractions import gcd
a = map(int,input().split(' '))
b = map(int,input().split(' '))
a_lcm = reduce(lambda x,y: x*y//gcd(x,y), a)
b_gcd = reduce(gcd, b)
print(sum(1 for i in range(a_lcm, b_gcd+1, a_lcm) if b_gcd%i==0))