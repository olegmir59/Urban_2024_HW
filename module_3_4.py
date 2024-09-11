#  Самостоятельная работа по уроку "Произвольное число параметров".
#  Задача "Однокоренные":

def single_root_words(root_word, *other_words):
    same_words = []
    for w in other_words:
        s = str(root_word).upper()
        ws =str(w).upper()
        if s in ws or ws in s :
            same_words.append(w)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
