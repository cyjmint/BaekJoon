n = int(input())
stock = list(map(int,input().split()))

bnp = 0; timing = 0 #매수한 주식의 수
bnp_cash = n; timing_cash = n #현재 보유 현금

for i in range(14):
    amount = bnp_cash//stock[i] #매수할 주식의 수
    if amount != 0:
        bnp += amount
        bnp_cash -= stock[i]*amount
bnp_cash += stock[-1]*bnp #1월 14일의 보유 자산

for i in range(3,14):
    if stock[i-3] < stock[i-2] < stock[i-1] < stock[i]: #3일 연속 전일 대비 주가가 오른다면
        timing_cash += stock[i]*timing #전량 매도
    if stock[i-3] > stock[i-2] > stock[i-1] > stock[i]: #3일 연속 전일 대비 주가가 내린다면
        amount = timing_cash//stock[i] #매수할 주식의 수
        if amount != 0: #주가가 현재 보유 현금보다 크지 않다면 전량 매수
            timing += amount 
            timing_cash -= stock[i]*amount 
timing_cash += stock[-1]*timing #1월 14일의 보유 자산

if bnp_cash > timing_cash:
    print('BNP')
if bnp_cash < timing_cash:
    print('TIMING')
if bnp_cash == timing_cash:
    print('SAMESAME')