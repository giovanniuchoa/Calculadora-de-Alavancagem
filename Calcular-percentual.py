import tkinter as tk

def calcular_alavancagem():
    perdaMax = float(perdaMax_entry.get())
    margem = float(margem_entry.get())
    entrada = float(entrada_entry.get())
    take = float(take_entry.get())
    stop = float(stop_entry.get())

    percMax = (perdaMax * 100) / margem
    difStop = stop - entrada
    percStop = (difStop * 100) / entrada

    if percStop < 0:
        percStop = percStop * -1

    if percStop > percMax:
        result_label.configure(text="Escolha um ponto de stop mais próximo, senão sua perda poderá ser maior que o máximo!")
        return

    alMax = 0
    temp = percStop
    while temp < percMax:
        if temp + percStop < percMax:
            alMax += 1
            temp = percStop * alMax
        else:
            break

    if alMax == 0:
        result_label.configure(text="O melhor a se fazer é não alavancar!")
    else:
        result_label.configure(text="Sua alavancagem máxima pode ser de {} vezes".format(alMax))

root = tk.Tk()
root.title("Calculadora de Alavancagem")
root.geometry("400x300")

perdaMax_label = tk.Label(root, text="Quantos dólares poderá perder na operação?")
perdaMax_label.pack()
perdaMax_entry = tk.Entry(root)
perdaMax_entry.pack()

margem_label = tk.Label(root, text="Quantos dólares serão aplicados?")
margem_label.pack()
margem_entry = tk.Entry(root)
margem_entry.pack()

entrada_label = tk.Label(root, text="Valor de entrada:")
entrada_label.pack()
entrada_entry = tk.Entry(root)
entrada_entry.pack()

take_label = tk.Label(root, text="Valor do alvo:")
take_label.pack()
take_entry = tk.Entry(root)
take_entry.pack()

stop_label = tk.Label(root, text="Valor do stop:")
stop_label.pack()
stop_entry = tk.Entry(root)
stop_entry.pack()

calcular_button = tk.Button(root, text="Calcular", command=calcular_alavancagem)
calcular_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
