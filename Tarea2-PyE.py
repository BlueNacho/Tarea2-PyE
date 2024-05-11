import random


def game(times):

    juan_wins = 0
    maria_wins = 0
    tie = 0

    for _ in range(times):
        # Estategia Juan
        juan = [random.randint(1, 6), random.randint(1, 6)]
        juan_result = checkResult(juan)

        #Si saca 0 tira ambos dados nuevamente
        if (juan_result == 0):
            juan = [random.randint(1, 6), random.randint(1, 6)]
            juan_result = checkResult(juan)
        #Si saca 1, 2 o 3 tira de nuevo el dado que no es 4 para intentar mejorar el resultado
        elif (juan_result in [1, 2, 3]):
            if (juan[0] != 4):
                juan[0] = random.randint(1, 6)
            else:
                juan[1] = random.randint(1, 6)
            juan_result = checkResult(juan)
        
        #Estrategia Maria (Para mejorar chances de victoria sobre Juan)
        maria = [random.randint(1, 6), random.randint(1, 6)]

        maria_result = checkResult(maria)

        #Si saca 0 tira el menor de los dos dados para intentar sacar un 4
        if (maria_result == 0):
            if (maria[0] >= juan_result and juan_result >= 4):
                maria[1] = random.randint(1,6)
            elif (maria[1] >= juan_result and juan_result >= 4):
                maria[0] = random.randint(1, 6)
            else:
                #Si ningun dado es mayor al puntaje tota de juan tira los dos
                maria = [random.randint(1, 6), random.randint(1, 6)]
            maria_result = checkResult(maria)
        #Si el resultado obtenido es menor que el de juan, o se encuentra entre 1, 2 o 3 tira el dado que no es 4 para intentar mejorar el resultado
        elif (maria_result < juan_result or maria_result in [1, 2, 3]):
            if (maria[0] != 4):
                maria[0] = random.randint(1, 6)
            else:
                maria[1] = random.randint(1, 6)
            maria_result = checkResult(maria)

        if (juan_result > maria_result):
            juan_wins += 1
        elif (maria_result > juan_result):
            maria_wins += 1
        else:
            tie += 1

    return {"win_frecuency": {"juan": juan_wins / times, "maria": maria_wins / times, "tie": tie / times}}


def checkResult(result):
    if (result == [4, 1] or result == [1, 4]):
        return 1
    elif (result == [4, 2] or result == [2, 4]):
        return 2
    elif (result == [4, 3] or result == [3, 4]):
        return 3
    elif (result == [4, 4]):
        return 4
    elif (result == [4, 5] or result == [5, 4]):
        return 5
    elif (result == [4, 6] or result == [6, 4]):
        return 6
    else:
        return 0


result = game(100)

print("Frecuencias:")
print("Juan gana: ", round(result["win_frecuency"]["juan"], 3))
print("Maria gana: ", round(result["win_frecuency"]["maria"], 3))
print("Empate: ", round(result["win_frecuency"]["tie"], 3))

