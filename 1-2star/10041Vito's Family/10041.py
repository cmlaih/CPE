from sys  import stdin
z=int(stdin.readline())
for _ in range(z):
    arr=[int(x) for x in stdin.readline().split()]
    r=arr[0]
    arr=arr[1:]
    arr.sort()
    mid=arr[r//2]
    arr1=[abs(mid-x) for x in arr]
    print(sum(arr1))
