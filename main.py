from tkinter import Tk, Label, Entry, Button, filedialog, StringVar, Checkbutton, Frame
from scrapper.main import iniciar_interacao_com_chatbots
from tkinter import Tk, Label, Entry, Button, Checkbutton, Frame, StringVar, BooleanVar
import random
from tkinter import *

# Prompt padrão inicial
prompt_start = (
    "Responda com no máximo 90 caracteres. "
    "Adote um tom sério e profissional. Haja como se tivesse anos. Possua um nome. "
    "Procure ter dúvidas sobre o serviço oferecido pela IA, tente executar falhas e retomar. "
    "Não utilize emojis, peça para não utilizar emojis. "
    "Responda com no máximo 90 caracteres. Pelo amor de Deus"
)

def iniciar_treino():
    chave_api = ""
    usar_gpt = False
    usar_gemini = False
    prompt = ""
    
    chave_api = chave_api_var.get()
    usar_gpt = gpt_var.get()
    usar_gemini = gemini_var.get()
    prompt = prompt_text.get("1.0", END).strip()

    if not chave_api:
        print("⚠️ Por favor, informe a chave da API!")
        return

    print("🔑 Chave da API:", chave_api)
    print("✅ GPT Ativo:", usar_gpt)
    print("✅ Gemini Ativo:", usar_gemini)

    iniciar_interacao_com_chatbots(
        url = "https://dev-esaude-frontend-dot-projetocaredev.uc.r.appspot.com/",
        chave_api=chave_api,
        usar_gpt=usar_gpt,
        usar_gemini=usar_gemini,
        prompt=prompt,
    )

# === GUI ===
app = Tk()
app.title("Treinador de Chatbot")
app.geometry("600x500")

# --- Entrada da chave da API ---
Label(app, text="Chave da API:").pack(pady=5)
chave_api_var = StringVar()
Entry(app, textvariable=chave_api_var, width=50).pack()

# --- Seleção de modelos ---
Label(app, text="Modelos a utilizar:").pack(pady=5)
gpt_var = BooleanVar(value=True)
gemini_var = BooleanVar(value=True)
Checkbutton(app, text="Utilizar GPT", variable=gpt_var).pack()
Checkbutton(app, text="Utilizar Gemini", variable=gemini_var).pack()

# --- Campo para prompt customizado ---
Label(app, text="Prompt Personalizado:").pack(pady=5)
prompt_text = Text(app, height=6, width=70, wrap=WORD)
prompt_text.insert(END, prompt_start)
prompt_text.pack(pady=5)

# --- Botão de início ---
Button(app, text="Iniciar Treino", command=iniciar_treino).pack(pady=20)

app.mainloop()