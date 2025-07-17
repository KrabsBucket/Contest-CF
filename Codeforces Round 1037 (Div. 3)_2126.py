

# ONLY ONE DIGIT
# t = int(input())

# for _ in range(t):
#     x = int(input())
#     m = []
#     for i in str(x):
#         m.append(int(i))


#     y = min(m)

#     print(y)

#No Casino in the Mountains
# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())

#     arry = list(map(int, input().split()))

#     i =0
#     m = 0
#     while i <= n-k:
#         if all(x == 0 for x in arry[i:i+k]):
#             m += 1
#             i += k+1
#         else:
#             i += 1

#     print(m)


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arry = list(map(int, input().split()))
    ip = arry[k-1] 
    arry.sort() 
    f = arry.index(ip)  
    h_max = max(arry)
    m = 1

    if ip == h_max:
        print("YES")
        continue

    success = False

    while ip >= m :
        for i in range(n-f):
            if arry[f+1] - arry[f] <= (ip-m+1):
                m += 1
                ip += (arry[f+1] - arry[f])
                break
        else:
            break
        if ip == h_max:
            success = True
            break

    if success:
        print("YES")   
    else:
        print("NO")