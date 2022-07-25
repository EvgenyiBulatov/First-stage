f = open('245.txt')
s = f.readline()
k = 0
f = 0
for i in range(len(s)):
    if 0 <= (ord(s[i]) - ord('A')) <= 26:
        k += 1
    elif 0 <= (ord(s[i]) - ord('a')) <= 26:
        f += 1
god = k - f
print(god)
        
