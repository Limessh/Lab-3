list = [5, 10, 12, 7, 6, 11, 0, 4, 9, 8]
list1 = []
list2 =[]

for number in list:
    if number%2==0: 
        list1.append(number)
    else: 
        list2.append(number)
print(list1)
print(list2)


result = ("I don't want to set the world on fire." . split()) [1::2]
print(result)


stroka = "Why don't you do right, like some other men do?" 
result = stroka. replace(" ","") . replace ("'",""). replace (",","") . replace ("?","")
print(len(result))