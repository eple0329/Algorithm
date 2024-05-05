N = int(input())

sell_count = dict()

for i in range(N):
    book_name = input()
    if book_name in sell_count.keys():
        sell_count[book_name] += 1
    else:
        sell_count[book_name] = 1

max_sell_count = 0
max_sell_books = []
for i in sell_count.keys():
    if sell_count[i] > max_sell_count:
        max_sell_count = sell_count[i]
        max_sell_books.clear()
        max_sell_books.append(i)
    elif sell_count[i] == max_sell_count:
        max_sell_books.append(i)

#print(max_sell_books)
max_sell_books.sort()
print(max_sell_books[0])
        
