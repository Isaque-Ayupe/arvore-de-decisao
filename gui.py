import tkinter as tk
from tkinter import ttk, messagebox
from dataset import load_csv, save_csv, insert_record, COLUMNS
from id3 import id3, predict
from tree_print import print_tree
import io
import sys

data = load_csv()
arvore = None

#função para treinar a arvore com os registros já existentes
def treinar():
    global arvore
    atributos = COLUMNS[:-1]
    arvore = id3(data, atributos)
    messagebox.showinfo("OK", "Árvore treinada!")

#def para registrar um novo usuario
def adicionar():
    registro = {
        "Nome": nome.get(),
        "Idade": idade.get(),
        "Pressao": pressao.get(),
        "Colesterol": colesterol.get(),
        "Fumante": fumante.get(),
        "Risco": risco.get()
    }
    insert_record(data, registro)
    save_csv(data)
    messagebox.showinfo("OK", "Registro salvo!")

#função para exibir a arvore POS TREINADA
def exibir_arvore():
    if arvore is None:
        messagebox.showwarning("Aviso", "Treine a árvore primeiro!")
        return

    # Captura a saída da função print_tree()
    buffer = io.StringIO()
    sys.stdout = buffer
    print_tree(arvore)
    sys.stdout = sys.__stdout__

    texto_arvore = buffer.getvalue()

    # Janela nova
    janela = tk.Toplevel(root)
    janela.title("Árvore de Decisão (ID3)")

    text_area = tk.Text(janela, width=70, height=30, font=("Consolas", 10))
    text_area.pack(padx=10, pady=10)

    text_area.insert("1.0", texto_arvore)
    text_area.config(state="disabled")


root = tk.Tk()
root.title("Classificador ID3 - Demo")

frame = ttk.Frame(root, padding=20)
frame.pack()

nome = tk.StringVar()
idade = tk.StringVar()
pressao = tk.StringVar()
colesterol = tk.StringVar()
fumante = tk.StringVar()
risco = tk.StringVar()

fields = [("Nome",nome), ("Idade", idade), ("Pressão", pressao), ("Colesterol", colesterol),
          ("Fumante", fumante), ("Risco", risco)]

for i, (label, var) in enumerate(fields):
    ttk.Label(frame, text=label).grid(row=i, column=0)
    ttk.Entry(frame, textvariable=var).grid(row=i, column=1)

ttk.Button(frame, text="Adicionar Registro", command=adicionar).grid(row=6, column=0)
ttk.Button(frame, text="Treinar Árvore", command=treinar).grid(row=6, column=1)
ttk.Button(frame, text="Visualizar Árvore", command=exibir_arvore).grid(row=7, column=0, columnspan=2, pady=10)


root.mainloop()
