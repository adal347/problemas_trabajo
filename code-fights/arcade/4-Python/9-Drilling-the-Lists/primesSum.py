def primesSum(a, b):
    return sum(filter(lambda x:len(list(filter(lambda y:x%y==0,range(2,int(x**0.5)+1))))==0,range((lambda x:x+1-x%2)(max(a,2)),b+1,2)))+(2 if a<=2 else 0)
