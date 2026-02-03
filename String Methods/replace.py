str1 = "Java Programming"

print(str1.replace("Java","Python"))  

#Return a copy with all occurrences of substring old replaced by new.


num = [1,2,3,4,5,6]

for i in num[:]:
    if i % 2 == 0:
        num.remove(i)

print(num)