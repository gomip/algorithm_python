# 프로그램 분배 
# input : 컴퓨터 n대, 실행할 프로그램 m개
import copy

def getInput():
    c = int(input("컴퓨터 수 입력 : "))
    p = list(map(int,input("프로그램 수 입력 : ").split()))
    return c,p

def works2(input):
    c,p = input
    _p = copy.deepcopy(p)
    wList = []  # 컴퓨터 리스트
    sList = []  # 컴퓨터가 수행할 작업 시간

    totW = sum(input[1])    # p들이 전부 수행하는데 소모하는 시간
    avgW = totW / c         # 총수행시간 / 컴퓨터 수로 평균 시간 계산
    for i in range(c):
        wList.append([])    # 컴퓨터 수만큼 리스트 생성
        sList.append(0)     # 컴퓨터 수만큼 우선 0으로 채워준다
    
    p.sort(reverse=True)

    for b in p:
        l = sList.index(min(sList))
        print('min',min(sList))
        wList[l].append(b)
        sList[l] += b
    
    return wList

if __name__ == "__main__":
    input = getInput()
    # w = works(input)
    w= works2(input)
    print(w)
