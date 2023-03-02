N = int(input())

ALPHABET_TREE = dict()
for i in range(N):
    root, left, right = input().split()
    ALPHABET_TREE[root] = (left, right)

def mid(TREE_DATA, root_alphabet):
    if root_alphabet == '.': return
    left, right = TREE_DATA[root_alphabet]
    if left == '.' and right == '.':
        print(root_alphabet, end = '')
        return
    else:
        mid(TREE_DATA, left)
        print(root_alphabet, end = '')
        mid(TREE_DATA, right)

def first(TREE_DATA, root_alphabet):
    if root_alphabet == '.': return
    left, right = TREE_DATA[root_alphabet]
    if left == '.' and right == '.':
        print(root_alphabet, end = '')
        return
    else:
        print(root_alphabet, end = '')
        first(TREE_DATA, left)
        first(TREE_DATA, right)

def last(TREE_DATA, root_alphabet):
    if root_alphabet == '.': return
    left, right = TREE_DATA[root_alphabet]
    if left == '.' and right == '.':
        print(root_alphabet, end = '')
        return
    else:
        last(TREE_DATA, left)
        last(TREE_DATA, right)
        print(root_alphabet, end = '')

first(ALPHABET_TREE, 'A')
print()
mid(ALPHABET_TREE, 'A')
print()
last(ALPHABET_TREE, 'A')


