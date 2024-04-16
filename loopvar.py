'a for loop is a type of loop that willloop through a group'


birGame = ['duck','duck','goose','duck','duck']

for x in birGame:
    if x == 'goose':
        print(f'found the goose at index{birGame.index('goose')}')
        continue

#while x == birGame[0]:
   # print(x)