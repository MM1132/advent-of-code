with open("input.txt") as nums: input = [int(i) for i in nums.read().split(",")]
f = [0 for _ in range(9)]
for i in range(1, max(input)+1):
    f[i] = input.count(i)
for _ in range(256):
    f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8] = f[1], f[2], f[3], f[4], f[5], f[6], f[7] + f[0], f[8], f[0]
print(sum(f))