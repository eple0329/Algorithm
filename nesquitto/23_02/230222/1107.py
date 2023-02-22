N = int(input())
M = int(input())
if M == 0:
    BUTTON_LIST = []
else:
    BUTTON_LIST = list(map(int, input().split()))

difference = abs(N-100)
count = 0
while difference > count + len(str(N)):
    if N-count >= 0:
        can_buttoned = True
        for i in str(N-count):
            if int(i) in BUTTON_LIST:
                can_buttoned = False
                break
        if can_buttoned:
            # print(N-count)
            print(len(str(N-count))+count)
            break
        
    can_buttoned = True
    for i in str(N+count):
        if int(i) in BUTTON_LIST:
            can_buttoned = False
            break
    if can_buttoned:
        # print(N+count)
        print(len(str(N+count))+count)
        break
    
    
    
    count += 1

if difference <= count + len(str(N)):
    print(difference)