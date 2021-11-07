import sys
sys.stdin = open('enc', 'r')

# Following 2 lines are just for reference
flag = '**'
enc =  ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

# Reversing the above encryption
flag = input()
sol = []
for i in range(len(flag)):
	sol.append(ord(flag[i]))
print(sol)

sol1 = []
for x in sol:
	# getting the first and last 8 bits
	f = x >> 8
	mask = (1 << 8) - 1
	s = x & mask
	sol1.append(f)
	sol1.append(s)
print(sol1)

print(''.join(chr(x) for x in sol1))
