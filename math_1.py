def fx():
    return x ^ 2 - 2 * x


def dfx():
    return 2 * x - 2

x = 2

for i in range(10):
    x = x - fx()/dfx()

print x