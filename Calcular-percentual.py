perdaMax = int(input("\nQuantos dólares poderá perder na operação? ")) # Perda Máxima em $
margem = int(input("\nQuantos dólares serão aplicados? ")) # Dinheiro aplicado na operação

percMax = (perdaMax*100)/margem # Percentual de perda máxima

entrada = float(input("\nValor de entrada: "))
take = float(input("\nValor do alvo: "))
stop = float(input("\nValor do stop: "))

difStop = stop-entrada # Diferença do stop para a entrada

percStop = (difStop*100)/entrada # Percentual na diferença do stop para a entrada

if (percStop < 0):
    percStop = percStop*-1

if (percStop > percMax):
    print("\nEscolha um ponto de stop mais próximo, senão sua perda poderá ser maior que o máximo!\n")
    exit()

alMax = int(0)
temp = percStop
while (temp < percMax):
    if (temp+percStop < percMax):
        alMax += 1
        temp = percStop*alMax
    else:
        break

if (alMax==0):
    print("O melhor a se fazer é não alavancar!")
else:
    print("\nSua alavancagem máxima pode ser de ",alMax," vezes\n")