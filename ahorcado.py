# -*- coding: utf-8 -*-
#   0
#  /|\
#   |
#  /\
IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

#Main del programa
def main():
    name = get_name()
    to_welcome(name)
    word = get_word()
    spaces_letters(word)
    try_get_word(word)

#Obtiene el nombre
def get_name():
    return str(raw_input('Ingresa tu nombre: '))

#Mensaje de Bienvenida
def to_welcome(name):
    print('================================')
    print('Bienvendo al juego del Ahorcado')
    print('================================')
    print('{}'.format(name))

#Obtiene palabra a adivinar
def get_word():
    return str(raw_input('Ingresa palabra a adivinar: ')).upper()



#Genera un espacio de las palabras
def spaces_letters(word ):
    array_space = list()
    array_word = list(word)
    for i in array_word:
        array_space.append('|___| ')
    print('\n')
    print(''.join(array_space))

#Pide la letra y verifica si es correcta
def try_get_word(word):
    word_array = list()
    word_array_true = list()
    complete = False
    intents = 0
    array_space = ['|___| '] * len(word)
    letter_true = list()
    print(IMAGES[intents])
    while complete == False:
        if intents < 7:
            word_array.append(str(raw_input('Ingresa una letra: ')).upper())
            letter_false = word.find(str(word_array[len(word_array)-1]))
            if(letter_false == -1):
                intents += 1
                print(IMAGES[intents])
                print('...:::Letra incorrecta:::...\n')

            else:
                print(IMAGES[intents])
                array_word_correct = ''.join(word_array)
                for i in range(0, len(word), 1):
                    for j in range(0, len(array_word_correct), 1):
                        if word[i] == array_word_correct[j]:
                            #//Detrerminar si gane
                            result = win(array_space, word)
                            if( result == True):
                                print('----------------------------')
                                print('...::: G A N A S T E :::...')
                                print('----------------------------')
                                print(IMAGES[intents])
                                complete =  True
                            else:
                                array_space[i] =  list(word[i])
                                print('\n...:::Letra correcta:::...\n')
                print(array_space)



        else:
            print('...:::Has perdido:::...\nLa palabra correcta era {}.'.format(word))
            complete = True
    try_now()

#gane
def win(array_space, word):
    lista = list()
    for i in word:
        lista.append(list(i))

    if lista == array_space:
        return True
    else:
        return False

#Funcion para volver a intertalo
def try_now():
    res = str(raw_input('\n¿Quieres intentarlo nuevamente?\n1 = si:\ncualquier cosa = no:\n'))
    if res == '1':
        word = get_word()
        spaces_letters(word)
        try_get_word(word)



#Indica donde incia el programa
if __name__ == '__main__':
    main()
