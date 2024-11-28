import tkinter as tk

# 1 - Criando uma janela
window = tk.Tk()
window.geometry("300x150")
window.title("Gerenciador de Frases")

# 2 - Adicionando frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# 3 - Adicionando label
label = tk.Label(frame, text="Hello, World!",)
label.pack(fill="x", expand=True)

# 4 - Adicionando o input ao text
fraseLab = tk.Label(frame, text="Frase")
fraseLab.pack(fill="x", expand=True)

fraseInput = tk.Entry(frame)
fraseInput.pack(fill="x", expand=True)

# 5 - Função para alterar o texto label
def click():
    label.config(text=fraseInput.get())

# 6 - Adicionando botão
button = tk.Button(frame, text="Enviar", command=click)
button.pack()

window.mainloop()