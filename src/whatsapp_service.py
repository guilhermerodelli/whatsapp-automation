from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

import urllib.parse
import random
import time


# Configuração Chrome
options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")


# Inicializa navegador
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)


def abrir_whatsapp():

    driver.get("https://web.whatsapp.com/")

    print("Escaneie o QR Code do WhatsApp.")
    input("Depois pressione ENTER para continuar...")


def enviar_mensagem(telefone, mensagem):

    mensagem_codificada = urllib.parse.quote(mensagem)

    url = f"https://web.whatsapp.com/send?phone={telefone}&text={mensagem_codificada}"

    driver.get(url)

    try:

        botao_enviar = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//button[@aria-label="Enviar"]'
                )
            )
        )

        time.sleep(2)

        driver.execute_script(
            "arguments[0].click();",
            botao_enviar
        )

        print(f"✅ Mensagem enviada para {telefone}")

        # Delay aleatório
        pausa = random.randint(5, 10)

        print(f"Aguardando {pausa} segundos...")

        time.sleep(pausa)

        return True

    except Exception as erro:

        print(f"❌ Erro ao enviar para {telefone}")
        print(erro)

        return False