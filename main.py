from tkinter import Tk, Label, Entry, Button, filedialog, StringVar, Checkbutton, Frame

def select_folder() -> None:
    folder = filedialog.askdirectory()
    output_folder_var.set(folder)

def teste():
    print("Treino iniciado")
    print("Pasta de saída:", output_folder_var.get())

app = Tk()
app.title("Treinador de Chatbot")
app.geometry("600x400")

# Pasta de saída
Label(app, text="Pasta de Saída:").pack(pady=5)

folder_frame = Frame(app)
folder_frame.pack(pady=5)

output_folder_var = StringVar()
Entry(folder_frame, textvariable=output_folder_var, width=50).pack(side="left", padx=10)
Button(folder_frame, text="Selecionar Pasta", command=select_folder).pack(side="left", padx=5)

# Chave da API
Label(app, text="Chave da API:").pack(pady=5)
CHAVE_API = Entry(app, width=50).pack()

# Checkbuttons
Label(app, text="Modelos a utilizar:").pack(pady=5)
grok = Checkbutton(app, text="Utilizando GPT").pack()
gpt =Checkbutton(app, text="Utilizando Grok").pack()

# Botão para iniciar o treino
Button(app, text="Iniciar Treino", command=teste).pack(pady=20)

app.mainloop()
