x = input("Введите слово : ").upper()

ScrabbleENG = {'1': 'A, E, I, O, U, L, N, S, T, R,А, В, Е, И, Н, О, Р, С, Т',
               '2': 'D, G,Д, К, Л, М, П, У',
               '3': 'B, C, M, P,Б, Г, Ё, Ь, Я',
               '4': 'F, H, V, W, Y, Й, Ы',
               '5': 'k,Ж, З, Х, Ц, Ч',
               '8': 'J, X,Ш, Э, Ю',
               '10': 'Q,Z,Ф, Щ, Ъ'}


result = 0
for i in x:
    for j in ScrabbleENG.keys():
        if i in ScrabbleENG[j]:
            result += int(j)
            break

print(f'В вашем слове {result} очоков ')
