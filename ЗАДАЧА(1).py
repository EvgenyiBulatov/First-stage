with open('245.txt') as f:
    k = 0
    n = 0
    for s in f:
        v = 0
        с = 0
        t = 0
        for i in range(len(s) - 2):
            if s[i] == 'A':
                if s[i+2] == 'S':
                    t += 1
                elif s[i+2] == 'Z':
                    с += 1
                elif s[i+2] == 'X':
                    v += 1
        n += 1
        if v > t + с:
            k += 1
            lasts = n
print(k, lasts)
f.close()    
                
