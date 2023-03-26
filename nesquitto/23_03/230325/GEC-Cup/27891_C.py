SHORT_NAME = ["NLCS", "BHA", "KIS", "SJA"]
FULL_NAME = ["North London Collegiate School", "Branksome Hall Asia", "Korea International School", "St. Johnsbury Academy"]
for i in range(4):
    FULL_NAME[i] = FULL_NAME[i].replace(" ", "").replace(".", "")
    FULL_NAME[i] = FULL_NAME[i].lower()
    FULL_NAME[i] = FULL_NAME[i][0:10]

encryption = input().rstrip()
for i in range(4):
    tmp = ord(encryption[0])-ord(FULL_NAME[i][0])
    full_name_tmp = list(FULL_NAME[i])
    encryption_tmp = list(encryption)
    if tmp < 0:
        for j in range(10):
            encryption_tmp[j] = chr((ord(encryption_tmp[j])-97-tmp)%26+97)
    else:
        for j in range(10):
            full_name_tmp[j] = chr((ord(full_name_tmp[j])-97+tmp)%26+97)
    if full_name_tmp == encryption_tmp:
        print(SHORT_NAME[i])
        break
