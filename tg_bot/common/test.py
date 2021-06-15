stack = []
 
elem = int(input())
for i in range(0,elem):
    stack.append(int(input()))
 
j = elem 
sum = 0
count = 1
elem = elem -1

while True:

    if stack[elem]%2 == 0:
        sum = sum + stack[elem] 
    
    if count == 3:
            print(sum)
            exit()
    count += 1

    elem = elem -1