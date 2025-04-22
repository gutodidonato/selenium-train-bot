from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Inicializa o navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://dev-esaude-frontend-dot-projetocaredev.uc.r.appspot.com/")
driver.maximize_window()
time.sleep(5)


campo_bot = driver.find_element(By.XPATH, '//*[@id="root"]/df-messenger')
campo_bot.click()


host2 = driver.find_element(By.CSS_SELECTOR, "df-messenger-chat-bubble")
shadow2 = host2.shadow_root
host3 = shadow2.find_element(By.CSS_SELECTOR, "df-messenger-chat")
shadow3 = host3.shadow_root
input_component = shadow3.find_element(By.CSS_SELECTOR, "df-messenger-user-input")
print("Elemento de input encontrado!")
shadow_input = input_component.shadow_root
text_area = shadow_input.find_element(By.CSS_SELECTOR, "textarea")
text_area.send_keys("Olá!")
text_area.send_keys(Keys.ENTER)

# Aguarda resposta
time.sleep(5)
driver.quit()
