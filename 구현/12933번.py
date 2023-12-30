quack = 'quack' #오리 울음소리
duck = input() #녹음된 울음소리
visited = [0] * len(duck) #duck의 각 문자를 확인했는지 파악하는 리스트

def find(start):
    global cnt
    j = 0 
    first = 1 #아직 확인하지 않은 녹음된 울음소리에서 처음으로 제대로 된 오리의 울음소리를 발견했다는 뜻 
    for i in range(start, len(duck)):
        if duck[i] == quack[j] and not visited[i]: #아직 확인하지 않은 녹음한 울음소리와 원래 울음소리 비교
            visited[i] = 1 #두 울음소리가 같다면, 확인 했다고 표시
            if duck[i] == 'k': #만약 녹음한 울음소리가 k라면
                if first: #그리고 처음으로 그걸 확인했다면,
                    cnt += 1 #오리를 찾았다는 뜻
                    first = 0 #한 오리가 여러번 울 수 있기 때문에, 다음 번에 또 k를 확인했다면 같은 오리가 운 것임
                              #그러므로 다음에 k를 확인했을 때 오리 1마리를 추가하지 않도록 first를 0으로 바꿈
                j = 0 # 마지막 문자인 k까지 나왔으면 다시 q부터 찾아서 비교해야 함
            
            else:
                j += 1 # k가 아니면 순서대로 다음 문자를 비교하기 위해 index ++

if len(duck) % 5 != 0: # 입력된 문자열의 길이가 5의 배수가 아니라면 올바르지 않은 울음소리임
    print(-1)
    exit() # -1을 출력하고 exit를 해주어야 프로그램이 종료되어 다음 for문 실행이 안됨

cnt = 0 # 오리의 수
for i in range(len(duck)):
    if duck[i] == 'q' and not visited[i]: #아직 확인하지 않은(not visited[i]) duck의 q(duck[i] == 'q')를 찾는 반복문
        find(i)

if cnt == 0 or not all(visited): # 오리의 수가 0마리거나 모든 문자를 방문하지 않았을 경우
    print(-1) # 올바르지 않은 울음소리

else: # 올바른 울음소리일 경우 오리의 수 출력
    print(cnt)