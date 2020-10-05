# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = []
list = input()
a = [float(i) for i in list.split(' ')]

print(sum(a)/n) 
a.sort()
if n % 2  == 0:
    print(float((a[int(n/2 -1)] + a[int(n/2)]) /2))
else:
    pass
    print(a[int(n/2 -1)])

d = {x:a.count(x) for x in a}
max_k = 0
max_v =0
for attr, value in d.items():
    if value>max_v:
        max_v = value
        max_k = attr

print(max_k)


"""
Input (stdin)
    10


    64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

Expected Output

    43900.6

    44627.5

    4978
"""
