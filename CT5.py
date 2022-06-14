
import sys
sys.stdin=open('input.txt')

# 양수를 출력하는 함수
def yangsoo(n):
    if n<0:
        n *= -1
    return n
# 입력된 데이터를 case = [[x1좌표,y2좌표,강도], [x2좌표, y2좌표, 강도], ...] 형태로 정리
x_list= []
y_list =[]
case = []
tc_num = int(input())
for i in range(tc_num):
    case += [list(map(int,input().split()))]
    x_list +=[case[i][0]]
    y_list +=[case[i][1]]
# print(case)

# 강도측정을 위해 시험해볼 좌표들을 test_list = [[x좌표,y좌표],[x좌표,y좌표],...]형태로 정리
# 시도해볼 x,y좌표들은 각각 위에서 주어진 x좌표의 최대값과 최소값 사이값, y좌표의 최대값과 최소값 사이값
test_list=[]
test_x = list(range(min(x_list),max(x_list)+1))
for i in test_x:
    test_list += [[i,k] for k in range(min(y_list),max(y_list)+1)]

# 위에서 정리한 test_list와 case를 이용하여 시험해본 각 좌표들 에서의 강도(hardenss)의 합을 정리한 sum_hardness_list 생성
# dictionary를 이용하여 axis_hardness = {강도:[x좌표, y좌표],...} 저장
sum_hardness_list = []
axis_hardness = dict()
for i in test_list:
    sum_hardness = 0
    for t in case:
        hardness = t[2]- yangsoo(i[0]-t[0])-yangsoo(i[1]-t[1])
        if hardness <0:
            hardness = 0
        sum_hardness += hardness
    sum_hardness_list += [sum_hardness]
    axis_hardness[sum_hardness] = i
# print(axis_hardness)
# print(sum_hardness_list)

# sum_hardness_list 에서 최대값을 찾은 후 axis_hardenss딕셔너리를 통해 좌표 찾기
max_sum = max(sum_hardness_list)
ans = axis_hardness[max_sum]
print(max_sum, ans)
