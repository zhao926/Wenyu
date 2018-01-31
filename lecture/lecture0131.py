# Dynamic programming techniques
# top down-->Memoization
def fib_memoization (n:int, lookup:dict)->int:
    if n<1:
        return-1
    #base case
    if n==1 or n==2 :
        lookup[n]=1
    if lookup.get(n, None) is None:
        lookup[n]=fib_memoization(n-1, lookup)+fib_memoization(n-2,lookup)
    return lookup[n]
    

#Bottom up -->Tabulation
def fib_tab(n:int)->int:
    f=[0]*(n+1)
    f[1]= 1#base case
    for i in range (2, n+1):
        f[i]=f[i-1]+f[i-2]
    return f[n]




def main()->int:
    my_dictionary={}
    f=fib_memoization(6,my_dictionary)#6--n,my_dict--lookup
    print(f)

if __name__=='__main__':
    main()
