import sys

N, M = map(int, sys.stdin.readline().split())

person1 = []
person2 = []
returnPerson = []
for i in range(N):
    person1.append(sys.stdin.readline().rstrip())
for i in range(M):
    person2.append(sys.stdin.readline().rstrip())
person1 = set(person1)
person2 = set(person2)
setPerson = person1.intersection(person2)

print(len(setPerson))
for i in sorted(setPerson):
    print(i)
