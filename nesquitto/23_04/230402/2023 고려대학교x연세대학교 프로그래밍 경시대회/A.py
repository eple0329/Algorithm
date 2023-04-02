STRING = list(input().rstrip())

KOREA = list("KOREA")
KOREA_idx = 0
YONSEI = list("YONSEI")
YONSEI_idx = 0

for i in STRING:
    if i == KOREA[KOREA_idx]:
        KOREA_idx += 1
        if KOREA_idx == 5:
            print("KOREA")
            break
    if i == YONSEI[YONSEI_idx]:
        YONSEI_idx += 1
        if YONSEI_idx == 6:
            print("YONSEI")
            break