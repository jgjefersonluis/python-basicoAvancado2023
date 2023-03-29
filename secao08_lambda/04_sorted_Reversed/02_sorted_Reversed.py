notasL = [10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3]
print(reversed(notasL))
print(list(reversed(notasL)))

notasT = (10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3)
print(list(reversed(notasT)))

notasC = {10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3}
#print(list(reversed(notasC))) #TypeError

#Iterar sobre o reversed
notasL = [10, 7, 8.8, 3, 8, 6, 9, 1, 0, 3]
for nota in reversed(notasL):
    print(nota, end=' ')
