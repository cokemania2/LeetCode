N = int(input())
x_list = []
for i in range(N):
    x_list.append(list(map(int, input().split())))

x_list.sort(key=lambda x: (x[1], x[0]))
answer_list = [x_list[0]]

for i in range(1, N):
    if x_list[i][0] >= answer_list[-1][1]:
        answer_list.append(x_list[i])
print(len(answer_list))