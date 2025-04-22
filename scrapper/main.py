from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
)

navegador = webdriver.Chrome(service=service, options=options)


def enviar_mensagem(mensagem):
    host2 = navegador.find_element(By.CSS_SELECTOR, "df-messenger-chat-bubble")
    shadow2 = host2.shadow_root
    host3 = shadow2.find_element(By.CSS_SELECTOR, "df-messenger-chat")
    shadow3 = host3.shadow_root
    input_component = shadow3.find_element(By.CSS_SELECTOR, "df-messenger-user-input")
    print("Elemento de input encontrado!")
    shadow_input = input_component.shadow_root
    text_area = shadow_input.find_element(By.CSS_SELECTOR, "textarea")
    text_area.send_keys(mensagem)
    text_area.send_keys(Keys.ENTER)
    
    
def envio_inicial():
    enviar_mensagem("Olá")


def capturar_ultima_mensagem(n=2):
    try:
        elemento = WebDriverWait(navegador, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, f'//*[@id="message-list"]/div/div[{n}]/df-messenger-utterance//div/df-markdown-message//div')
            )
        )
        return elemento.text
    except:
        print("Mensagem não encontrada.")
        return None


def ativar_chat_bot():
    try:
        campo_bot = WebDriverWait(navegador, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/df-messenger')
            )
        )
        campo_bot.click()
    except Exception as e:
        print("Não encontrado chatbot", e)


def fluxo_principal(url):
    try:
        navegador.get(url)
        time.sleep(10)
        ativar_chat_bot()
        time.sleep(10)
        envio_inicial()
        n = 2
        while True:
            mensagem = capturar_ultima_mensagem(n)
            if mensagem:
                print("Bot:", mensagem)
            else:
                print("Sem nova mensagem.")
            time.sleep(10)
            n += 2
    except Exception as e:
        print("Erro no fluxo principal:", e)


fluxo_principal("https://dev-esaude-frontend-dot-projetocaredev.uc.r.appspot.com/")
