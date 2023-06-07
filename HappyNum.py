N = 10000
def convert(n):
   i = 0
   while n>0:
      i += (n%10)*(n%10)
      n = n//10
   return i

happyNum = set()
unhappyNum = set()
for i in range(N):
   cache = set()
   j = i
   while j > 1 and j not in unhappyNum and j not in happyNum and j not in cache:
      cache.add(j)
      j = convert(j)

   if j == 1 or j in happyNum:
      happyNum.add(i)
      happyNum.update(cache)
   else:
      unhappyNum.add(i)
      unhappyNum.update(cache)

print(sorted(happyNum))
