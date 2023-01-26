T = int(input())

lenOfTriangle = [0 for i in range(101)]
lenOfTriangle[1:10] = [1,1,1,2,2,3,4,5,7,9]
for i in range(11, 101):
    lenOfTriangle[i] = lenOfTriangle[i-1] + lenOfTriangle[i-5]
for _ in range(T):
    print(lenOfTriangle[int(input())])
