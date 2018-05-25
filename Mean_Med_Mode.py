n = int(input())
a = [int(x) for x in input().split()]
len_ = len(a)
sum = 0
for i in range(len_):
    sum += a[i]
mean =round(sum/len_, 1)
print(mean)

# Median
sort_a = sorted(a)
mid =(0+(len_ - 1))//2
if len_ % 2 == 0:
    median = (sort_a[mid]+sort_a[mid+1])/2
    median = round(median, 1)
else:
    median = sort_a[mid]
print(median)

# Mode
set_a = list(set(a))
item_count = []
for i in range(len(a)):
    item_count.append(a.count(set_a[i]))
if all(item_count) == 1:
    print(min(set_a))
else:
    print(sorted([list(x) for x in zip(set_a, item_count)], key=lambda x: x[1], reverse=True)[0][0])

# Read number from file separated by space
'''
with open('num.txt') as f:
	b = [int(x) for x in f.read().split()]
'''
