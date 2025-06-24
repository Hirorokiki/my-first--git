import collections

L = input()
l = sorted(L)

if len(l) < 2:
    print("いいえ")
    exit()

counts = []
start_index = 0
for i in range(1, len(l)):
    if l[i] != l[i-1]:
        counts.append(i - start_index)
        start_index = i

counts.append(len(l) - start_index)

freq = collections.Counter(counts)

result = "はい"
for f in freq.values():
    if f != 2:
        result = "いいえ"
        break

print(result)





