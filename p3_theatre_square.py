#n = int(input())
# m = int(input())
# a = int(input())
n , m  , a = map(int, input().split())
if n % a == 0:
    count1 = n//a
else:
    count1 = (n//a) + 1

if m % a == 0:
    count2 = m//a
else:
    count2 = (m//a) + 1

print(count1 * count2)

