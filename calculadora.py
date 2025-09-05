import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Funções
# -----------------------------
def adicionar(caractere):
    display_texto.set(display_texto.get() + str(caractere))

def limpar():
    display_texto.set("")

def calcular():
    try:
        resultado = eval(display_texto.get())
        display_texto.set(str(resultado))
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Não é possível dividir por zero!")
        display_texto.set("")
    except:
        messagebox.showerror("Erro", "Entrada inválida!")
        display_texto.set("")

# -----------------------------
# Janela principal
# -----------------------------
janela = tk.Tk()
janela.title("Calculadora Dark")
janela.resizable(False, False)
janela.configure(bg="#2b2b2b")  # Cor de fundo dark

# -----------------------------
# Display
# -----------------------------
display_texto = tk.StringVar()
display = tk.Entry(
    janela, 
    textvariable=display_texto, 
    font=("Consolas", 24), 
    bd=0, 
    relief="ridge", 
    justify="right",
    bg="#1e1e1e", 
    fg="white", 
    insertbackground="white"
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)

# -----------------------------
# Cores dos botões
# -----------------------------
cor_numero = "#3c3f41"
cor_operador = "#ff9500"
cor_igual = "#4CAF50"
cor_limpar = "#f44336"

# -----------------------------
# Criar botões
# -----------------------------
botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

for (text, row, col) in botoes:
    if text == "=":
        tk.Button(janela, text=text, width=5, height=2, font=("Consolas", 18),
                  bg=cor_igual, fg="white", bd=0, command=calcular).grid(row=row, column=col, padx=5, pady=5)
    elif text == "C":
        tk.Button(janela, text=text, width=22, height=2, font=("Consolas", 18),
                  bg=cor_limpar, fg="white", bd=0, command=limpar).grid(row=row, column=col, columnspan=4, padx=5, pady=10)
    elif text in "+-*/":
        tk.Button(janela, text=text, width=5, height=2, font=("Consolas", 18),
                  bg=cor_operador, fg="white", bd=0, command=lambda t=text: adicionar(t)).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(janela, text=text, width=5, height=2, font=("Consolas", 18),
                  bg=cor_numero, fg="white", bd=0, command=lambda t=text: adicionar(t)).grid(row=row, column=col, padx=5, pady=5)

# -----------------------------
# Rodar aplicação
# -----------------------------
janela.mainloop()
