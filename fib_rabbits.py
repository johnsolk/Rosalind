def fib(n):
    if n<2:
        return n
    #print(n)
    return (fib(n-1) + fib(n-2))
print('Fib',fib(6))

#f(n)=(previousoriginalparents + previous-previousnewborns)
#+(eachparenthaving_k_newborns)
#+ previousnewborns

#(a) find the code that calculates the number of rabbits that were alive two months prior
#(b) mulitply it by k.


def rab(n,k):
    if n<2:
        return n
    return (rab((n-1),k)+k*rab((n-2),k))
print('Rab',rab(6,3))
