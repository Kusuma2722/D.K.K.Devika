def tog(n):
    res= ""
    for i in n:
        if i == "0":
            res+= "1"
        else:
            res+= "0"
    return res

def gms(arr, k):
    max_sum = 0
    max_subset = []

    for start in range(len(arr)):
        current_sum = 0
        current_subset = []

        for end in range(start, min(start + 2 * k + 1, len(arr))):
            current_sum += arr[end]
            current_subset.append(arr[end])

        if current_sum > max_sum:
            max_sum = current_sum
            max_subset = current_subset

    for element in max_subset:
        arr.remove(element)

    return max_sum, arr



a=list(map(int, input().split()))  
x1,y1=input().split()
x2,y2=input().split()

k=int(input())

rahul=0
rupesh=0

while a:
    s1,a=gms(a,k) 
    rahul+=s1
    
    if not a:
        break
        
    s2,a=gms(a,k)
    rupesh+=s2
    
if rahul>rupesh:
    x1=tog(x1)
    y2=tog(y2)
else:
    x2=tog(x2) 
    y1=tog(y1)

xor1=int(x1,2)^int(y1,2)  
xor2=int(x2,2)^int(y2,2)

if xor1>xor2:
    print("Rahul")
elif xor2>xor1:
    print("Rupesh")
else:
    print("both")
