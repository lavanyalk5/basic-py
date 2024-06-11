n=123
temp=n 
reverse=0
while(temp>0):
    d=temp%10
    reverse=reverse*10+d
    temp=temp//10
if(n== reverse):
    print("Palindrome")
else:
    print("Not palindorme")