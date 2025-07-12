total_jackfruit, festival = list(map(int,input().split()))

arr = list(map(int, input().split()))

arr.sort(reverse=True)
total = 0
for i in range(festival):
    total += arr[i]
print(total)
