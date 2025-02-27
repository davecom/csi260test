from collections import Counter

def counts(l):
	counts = {}
	for item in l:
		if item in counts:
			counts[item] += 1
		else:
			counts[item] = 1
	return counts

def counts2(l):
	return Counter(l)

print(counts(["James", "Sarah", "James", "Marge", "James", "Sarah"]))
print(counts([5, 5, 6, 7, 8, 7, 7]))
print(counts2(["James", "Sarah", "James", "Marge", "James", "Sarah"]))
print(counts2([5, 5, 6, 7, 8, 7, 7]))