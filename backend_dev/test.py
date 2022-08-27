from Crypto.Hash import SHA256

n = 10000
r = 0
for i in range(n):
    r += int(SHA256.new(b"hello"+bytes(10+i)).hexdigest(), 16)/int(SHA256.new(b"hello"+bytes(2+i)).hexdigest(), 16)*100

print(r/n)