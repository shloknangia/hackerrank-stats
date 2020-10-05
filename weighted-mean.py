# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = input()
X = [float(i) for i in x.split(' ')]

w = input()
W = [float(i) for i in w.split(' ')]

# import numpy as np

# x_np = np.array(X)
# w_np = np.array(W)

# print(sum(x_np*w_np)/sum(W))

s = 0
for i in range(n):
    s = s + (X[i] *W[i])

print("{:.1f}".format(s/sum(W)))
