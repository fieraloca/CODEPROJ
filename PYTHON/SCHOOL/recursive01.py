##  1. Take a number of with four digits (N)
##  2. Sort digits small to big (ASC)
##  3. Sort digits big to small (DESC)
##  4. Result  - DESC - ASC
##  5. If Result = N exit and record number of iterations


def sortAsc(n):
    """ Sort the input number by characters from small to big"""
    a = str(n)
    b = sorted(a)
##    print(b)
    return int(''.join(b))

               
def sortDesc(n):
    """ Sort the input number by characters from big to small"""
    a = str(n)
    b =sorted(a,reverse=True)
##    print (b)
    return int(''.join(b))

##print(sortAsc(3471))
##print(sortDesc(3471))

maxval = 0


##use this script to find the numbers in the specified range
thehist = [0,0,0,0,0,0,0,0,0,0]
ini = 1000
fin = 9999

for m in range(ini,fin):
    k = 0
    nstart = m
    nend = 0
    pausenow = 0
    
    while pausenow == 0:
        k = k +1
        nasc = sortAsc(nstart)
        ndesc = sortDesc(nstart)
        nend = ndesc - nasc
        if nstart == nend:
            pausenow = 1
        else:
             nstart = nend
    if k >= maxval:
        maxval = k
    thehist[k] = thehist[k] +1  
print(ini,fin,thehist)



    
    
####====================================================================
####use this script to bin the data in chunks of 1000 numbers
##
##for no in range(1,10):
##    ini = no*1000
##    fin = no*1000 + 999
##    
##    thehist = [0,0,0,0,0,0,0,0,0,0]
##
##    for m in range(ini,fin):
##        k = 0
##        nstart = m
##        nend = 0
##        pausenow = 0
##        
##        while pausenow == 0:
##            k = k +1
##            nasc = sortAsc(nstart)
##            ndesc = sortDesc(nstart)
##            nend = ndesc - nasc
##    ##        print (ndesc,nasc,nend)
##            
##            if nstart == nend:
##                pausenow = 1
##            else:
##                 nstart = nend
##        if k >= maxval:
##            maxval = k
##        thehist[k] = thehist[k] +1    
##                
####        print("m: ", m, "k: ",k)
##
##    ##print(maxval)
##    print(ini,fin,thehist)
##    
##
##
##
