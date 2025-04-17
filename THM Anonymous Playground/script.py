s = "hEzAdCfHzA::hEzAdCfHzAhAiJzAeIaDjBcBhHgAzAfHfN"
result = []
for i in range(0, len(s), 2):
    if i + 1 >= len(s):
        break  # Skip incomplete pairs
    c1, c2 = s[i], s[i+1]
    if c1.islower() and c2.isupper():
        lower_pos = ord(c1) - ord('a') + 1
        upper_pos = ord(c2) - ord('A') + 1
        total = lower_pos + upper_pos
        mod = total % 26
        if mod == 0:
            mod = 26
        result.append(chr(96 + mod))
    else:
        # Skip non-conforming pairs
        continue
print(''.join(result))
