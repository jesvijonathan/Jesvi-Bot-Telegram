def main():

    f = s = n = None
    v = x = a = b = c = d = list()
    
    n = int(input(""))

    for i in range(n): 
        x = input("").split()
        
        a.insert(i,x[0])
        b.insert(i,x[1])
        c.insert(i,x[2])
        d.insert(i,x[3])

        s = int(x[0]) + int(x[1]) + int(x[2]) + int(x[3])
        v.insert(i,s)

    for i in range(n):
        x.insert(i,0)

        for j in range(n):
            
            if v[i] < v[j]:
                s = x[i]
                x.insert(i,s+1)
    
    f = x[0] + 1
    print(f)


if __name__ == '__main__':
    main()

""" Greatest Sort Func -
5
100 98 100 100
100 100 100 100
100 100 99 99
90 99 90 100
100 98 60 99
"""