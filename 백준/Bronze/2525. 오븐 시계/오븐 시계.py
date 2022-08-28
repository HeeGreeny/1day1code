H,M = map(int,input().split())
C = int(input())
M = M+C
if M < 60:
    print(H,M)
elif M >= 60:
    if H+(M//60) >= 24:
       print(H-24+(M//60),M%60)
    else :
       print(H+(M//60),M%60)