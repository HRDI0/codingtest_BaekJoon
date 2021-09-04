#study_7_1.py
# N×M (5≤N, M≤100)의 모눈종이 위에 아주 얇은 치즈가 <그림 1>과 같이 표시되어 있다. 
# 단, N 은 세로 격자의 수이고, M 은 가로 격자의 수이다. 이 치즈는 냉동 보관을 해야만 하는데 실내온도에 내어놓으면 공기와 접촉하여 천천히 녹는다. 
# 그런데 이러한 모눈종이 모양의 치즈에서 각 치즈 격자(작 은 정사각형 모양)의 4변 중에서 적어도 2변 이상이 실내온도의 공기와 접촉한 것은 
# 정확히 한시간만에 녹아 없어져 버린다. 따라서 아래 <그림 1> 모양과 같은 치즈(회색으로 표시된 부분)라면 C로 표시된 모든 치즈 격자는 한 시간 후에 사라진다.
# <그림 2>와 같이 치즈 내부에 있는 공간은 치즈 외부 공기와 접촉하지 않는 것으로 가정한다. 그러므 로 이 공간에 접촉한 치즈 격자는 녹지 않고 
# C로 표시된 치즈 격자만 사라진다. 그러나 한 시간 후, 이 공간으로 외부공기가 유입되면 <그림 3>에서와 같이 C로 표시된 치즈 격자들이 사라지게 된다.
# 모눈종이의 맨 가장자리에는 치즈가 놓이지 않는 것으로 가정한다. 입력으로 주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 모눈종이의 크기를 나타내는 두 개의 정수 N, M (5 ≤ N, M ≤ 100)이 주어진다. 
# 그 다음 N개의 줄에는 모눈종이 위의 격자에 치즈가 있는 부분은 1로 표시되고, 치즈가 없는 부분은 0으로 표시된다. 
# 또한, 각 0과 1은 하나의 공백으로 분리되어 있다.

# 출력
# 출력으로는 주어진 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간을 정수로 첫 줄에 출력한다.
n,m = map(int,input().split())
list_nm = []
#out_cheese = []
#out_count = 0
one_count = 0
time = 0

for i in range(n):
    list_nm.append(list(map(int,input().split())))

# while(1):
#     for i in range(n):
#         for j in range(m):
#             out_count = 0
#             if list_nm[i][j] != 1:
#                 continue
#             if list_nm[i - 1][j] == 0:
#                 out_count +=1
#             if list_nm[i + 1][j] == 0:
#                 out_count +=1
#             if list_nm[i][j - 1] == 0:
#                 out_count +=1
#             if list_nm[i][j + 1] == 0:
#                 out_count +=1
#             if out_count >= 2:
#                 out_cheese.append(i)
#                 out_cheese.append(j)
#     for k in range(0,len(out_cheese),2):
#         list_nm[out_cheese[k]][out_cheese[k+1]] = 0
#     if not out_cheese:
#         break
#     else:
#         out_cheese.clear()
#         time +=1

while(1):
    one_count = 0
    for i in range(n):
        for j in range(m):
            if list_nm[i][j] == 0:
                list_nm[i][j] -=1   
                if j < m-1 and list_nm[i][j+1] > 0:
                    list_nm[i][j+1] +=1
                if j > 0 and list_nm[i][j-1] > 0:
                    list_nm[i][j-1] +=1
                if i > 0 and list_nm[i-1][j] > 0:
                    list_nm[i-1][j] +=1
                if i < n-1 and list_nm[i+1][j] > 0:
                    list_nm[i+1][j] +=1
    for k in range(n):
        for s in range(m):
            if list_nm[k][s] >= 3:
                list_nm[k][s] = 0
            elif list_nm[k][s] == -1:
                list_nm[k][s] = 0
            elif 0 < list_nm[k][s] < 3:
                one_count =1
                list_nm[k][s] = 1
    time +=1
    if one_count == 0:
        break
print(time)
