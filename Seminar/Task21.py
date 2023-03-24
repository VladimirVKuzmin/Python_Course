#Задача №21. Напишите программу для печати всех уникальных значений в словаре. 
#Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
#{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, 
#{" VIII ":" S007 "}] 
#Output: {'S005', 'S002', 'S007', 'S001', 'S009'

list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
         {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, 
         {" VIII ":" S007 "}] 

# print()
# dictionary = \
#     {
#        "I": "S001",
#        "II": "S002",
#        "III": "S001",
#        "IV": "S005",
#        "V": "S005",
#        "VI":"S009",
#        "VII": "S007"
#     }
# print(dictionary.values())
# print(type(dictionary))
# print()
# dictionary_B = dictionary.values
# print(set(dictionary_B()))

my_set = set()

for item in list_1:
    for key in item.keys():
        my_set.add(item.get(key))
print(my_set)
