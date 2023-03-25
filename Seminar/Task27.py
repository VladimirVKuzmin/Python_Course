# Задача №27. Пользователь вводит текст(строка).
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов.
# Определите, сколько различных слов содержится в этом тексте. 
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells 
# I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

import string

liter_list = """She sells sea shells on the sea shore The shells that she sells are sea shells 
                I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"""
print(liter_list)
punct = list(string.punctuation) + ['\n', '\t']

for char in punct:
    liter_list = liter_list.replace(char, ' ')

liter_list = liter_list.lower().split()

dict_count = {}
for key in liter_list:
    dict_count[key] = dict_count.get(key, 0) + 1
print(*dict_count.items(), sep='\n')

print(len(set(dict_count)))






