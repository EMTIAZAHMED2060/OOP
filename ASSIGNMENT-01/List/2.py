n = int(input())
max = 0
for i in range(n):
    sum = 0
    inp_list = input().split(" ")
    inp_list = [int(x) for x in inp_list]
    for x in inp_list:
        sum+=x
    if sum > max:
        max = sum
        max_list = inp_list
print(f"{max}\n{max_list}")