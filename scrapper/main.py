from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from models.grok import factory_message

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from openai import OpenAI


def configurar_driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )
    return webdriver.Chrome(service=service, options=options)

driver = configurar_driver()

def ativar_interface_chatbot():
    try:
        bot_frame = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "df-messenger"))
        )
        bot_frame.click()
    except Exception as e:
        print("❌ Erro ao ativar chatbot:", e)

def enviar_para_chatbot_dialogflow(mensagem):
    try:
        chat_bubble_shadow = driver.find_element(By.CSS_SELECTOR, "df-messenger-chat-bubble").shadow_root
        chat_window_shadow = chat_bubble_shadow.find_element(By.CSS_SELECTOR, "df-messenger-chat").shadow_root
        input_shadow = chat_window_shadow.find_element(By.CSS_SELECTOR, "df-messenger-user-input").shadow_root
        text_area = input_shadow.find_element(By.CSS_SELECTOR, "textarea")
        text_area.send_keys(mensagem)
        text_area.send_keys(Keys.ENTER)
        print(f"📤 Enviado para DialogFlow: {mensagem}")
    except Exception as e:
        print("❌ Erro ao enviar mensagem ao DialogFlow:", e)

def obter_ultima_resposta_bot():
    try:
        time.sleep(10)
        chat_bubble_shadow = driver.find_element(By.CSS_SELECTOR, "df-messenger-chat-bubble").shadow_root
        chat_window_shadow = chat_bubble_shadow.find_element(By.CSS_SELECTOR, "df-messenger-chat").shadow_root
        message_list = chat_window_shadow.find_element(By.CSS_SELECTOR, "df-messenger-message-list").shadow_root
        mensagens_do_bot = message_list.find_elements(By.CLASS_NAME, "bot")
        print(f"Temos {len(mensagens_do_bot)} mensagens")
        
        if not mensagens_do_bot:
            print("⏳ Ainda não há mensagens do bot.")
            return None

        ultima_mensagem = mensagens_do_bot[-1]
        utterance_shadow = ultima_mensagem.find_element(By.CSS_SELECTOR, "df-messenger-utterance").shadow_root
        markdown_shadow = utterance_shadow.find_element(By.CSS_SELECTOR, "df-markdown-message").shadow_root
        conteudo_mensagem = markdown_shadow.find_element(By.CLASS_NAME, "bot-message.markdown").find_element(By.TAG_NAME, "p")
        return conteudo_mensagem.text

    except Exception as e:
        print("❌ Erro ao capturar resposta do bot:", e)
        return None

def gerar_resposta_chatgpt(prompt_usuario, chave_api, usar_gpt, usar_grok):
    try:
        return factory_message(prompt_usuario=prompt_usuario,chave_api= chave_api, usar_gpt=usar_gpt, usar_grok=usar_grok)
    except Exception as e:
        print("❌ Erro ao gerar resposta via Grok:", e)
        return "Erro ao processar resposta."

def iniciar_interacao_com_chatbots(
        chave_api,
        usar_gpt,
        usar_grok,
        url="https://dev-esaude-frontend-dot-projetocaredev.uc.r.appspot.com/"):
    try:
        driver.get(url)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "df-messenger")))
        ativar_interface_chatbot()
        time.sleep(2)

        enviar_para_chatbot_dialogflow("Olá")

        ultima_resposta_botA = ""
        while True:
            nova_resposta_botA = obter_ultima_resposta_bot()

            if nova_resposta_botA and nova_resposta_botA != ultima_resposta_botA:
                print(f"🤖 DialogFlow respondeu: {nova_resposta_botA}")
                ultima_resposta_botA = nova_resposta_botA

                resposta_botB = gerar_resposta_chatgpt(chave_api=chave_api, usar_gpt=usar_gpt, usar_grok=usar_grok, prompt_usuario=nova_resposta_botA)
                print(f"🤖 Grok respondeu: {resposta_botB}")

                enviar_para_chatbot_dialogflow(resposta_botB)

            time.sleep(2)
    except Exception as e:
        print("❌ Erro no fluxo principal:", e)
