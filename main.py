from tkinter import Tk, Label, Entry, Button, filedialog, StringVar, Checkbutton, Frame
from scrapper.main import iniciar_interacao_com_chatbots
from tkinter import Tk, Label, Entry, Button, Checkbutton, Frame, StringVar, BooleanVar
from scrapper.main import iniciar_interacao_com_chatbots


def iniciar_treino():
    chave_api = ""
    usar_gpt = False
    usar_grok = False 
    
    chave_api = chave_api_var.get()
    usar_gpt = gpt_var.get()
    usar_grok = grok_var.get()

    print("🔑 Chave da API:", chave_api)
    print("✅ GPT Ativo:", usar_gpt)
    print("✅ Grok Ativo:", usar_grok)

    if not chave_api:
        print("⚠️ Por favor, informe a chave da API!")
        return

    # Você pode ajustar aqui para alternar entre os modelos
    iniciar_interacao_com_chatbots(
        url="https://dev-esaude-frontend-dot-projetocaredev.uc.r.appspot.com/",
        chave_api=chave_api,
        usar_gpt=usar_gpt,
        usar_grok=usar_grok
    )


# === GUI ===
app = Tk()
app.title("Treinador de Chatbot")
app.geometry("600x400")

# --- Entrada da chave da API ---
Label(app, text="Chave da API:").pack(pady=5)
chave_api_var = StringVar()
Entry(app, textvariable=chave_api_var, width=50).pack()

# --- Seleção de modelos ---
Label(app, text="Modelos a utilizar:").pack(pady=5)
gpt_var = BooleanVar(value=True)
grok_var = BooleanVar(value=True)

Checkbutton(app, text="Utilizar GPT", variable=gpt_var).pack()
Checkbutton(app, text="Utilizar Grok", variable=grok_var).pack()

# --- Botão de início ---
Button(app, text="Iniciar Treino", command=iniciar_treino).pack(pady=20)

app.mainloop()
