name = input()
str1 = name.split()
str2=[]
for i in str1:
    temp=''
    if(i.isalpha()):
        temp = temp+i
        temp = temp.lower()
        temp = temp.capitalize()
        str2.append(temp)
len = len(str2)
check=1
result=''
for i in str2:
    if(check<len):
        result = result+i[0]+'.'
    else:
        result=result+i
    check = check+1
print(result)
