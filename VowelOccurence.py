s=input()
count=0
flag=0
s=s.lower()
a=s.strip()
for x in a:
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        count+=1
    else:
        flag+=1
print('No of consonants = %d'%(flag))
print('No of Vowels = %d'%(count))