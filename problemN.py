import collections

raw_input = input()
detailed_mode = '?' in raw_input
L = raw_input.replace('?', '')

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
offending_counts = []
for count, frequency in freq.items():
    if frequency != 2:
        result = "いいえ"
        offending_counts.append(str(count))

if result == "はい":
    print("はい")
else:
    print("いいえ")
    if detailed_mode:
        reason = ", ".join(offending_counts)
        print(f"理由: グループサイズ「{reason}」の出現回数が2回ではありませんでした。")
        print(f"解析: グループサイズのリストは {counts} です。")