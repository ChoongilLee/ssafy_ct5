
import sys
sys.stdin=open('input.txt')


def yangsoo(n):
    if n<0:
        n *= -1
    return n

x_list= []
y_list =[]
case = []
tc_num = int(input())
for i in range(tc_num):
    case += [list(map(int,input().split()))]
    x_list +=[case[i][0]]
    y_list +=[case[i][1]]


test_list=[]
test_x = list(range(min(x_list),max(x_list)+1))
for i in test_x:
    test_list += [[i,k] for k in range(min(y_list),max(y_list)+1)]


sum_hardness_list = []
axis_hardness = dict()
for i in test_list:
    sum_hardness = 0
    for t in case:
        hardness = t[2]- yangsoo(i[0]-t[0])-yangsoo(i[1]-t[1])
        if hardness <0:
        # 예상 실수 발생지점입니다, 해당 지점에서 강도가 음수가 되었을때 강도 자체가 0이 되는게 아니라 
        # 강도에서 빼는 값을 0으로 만든것 같습니다.
            hardness = t[2]
        sum_hardness += hardness
    sum_hardness_list += [sum_hardness]
    axis_hardness[sum_hardness] = i

max_sum = max(sum_hardness_list)
ans = axis_hardness[max_sum]
print(max_sum, ans)

# 최대값 27, 좌표(6,1) 출력