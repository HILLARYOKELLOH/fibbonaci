#fibbonaci
n=int(input('enter a number:'))
first=0
second=1
i=0
print(first,second,end='')
while i<=n:
      next=first+second
      first=second
second=next
i+=1
print(next,end='')
