lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

set1 = set(lst1)
set2 = set(lst2)

result = set1.intersection(set2)

print(list(result))