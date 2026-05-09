import os
import sys

from excel_service import carregar_motoristas
from message_service import criar_mensagem
from whatsapp_service import enviar_mensagem, abrir_whatsapp

from datetime import datetime


def obter_caminho_base():

    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)

    return os.path.dirname(os.path.abspath(__file__))


BASE_DIR = obter_caminho_base()


def escolher_planilha():

    print("======== SISTEMA DE ENVIO ========")
    print("1 - Adiantamento")
    print("2 - Fechamento")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        return os.path.join(
            BASE_DIR,
            "data",
            "adiantamento.xlsx"
        ), "ADIANTAMENTO"

    elif opcao == "2":

        return os.path.join(
            BASE_DIR,
            "data",
            "fechamento.xlsx"
        ), "FECHAMENTO"

    else:

        print("Opção inválida.")
        exit()


def salvar_log(texto):

    caminho_log = os.path.join(
        BASE_DIR,
        "logs",
        "envios.log"
    )

    with open(caminho_log, "a", encoding="utf-8") as log:

        log.write(texto + "\n")


def main():

    caminho_planilha, tipo_envio = escolher_planilha()

    motoristas = carregar_motoristas(caminho_planilha)

    total = len(motoristas)

    enviados = 0
    erros = 0

    abrir_whatsapp()

    print(f"\nIniciando envio de {tipo_envio}...\n")

    for indice, motorista in enumerate(motoristas, start=1):

        try:

            nome = motorista["nome"]

            telefone = "+" + str(motorista["telefone"])

            empresa = motorista["empresa"]

            valor = motorista["valor"]

            if telefone == "+nan":

                print(f"Telefone inválido para {nome}")

                erros += 1

                continue

            mensagem = criar_mensagem(
                nome,
                empresa,
                valor,
                tipo_envio
            )

            print(f"\n[{indice}/{total}] Enviando para {nome}...")

            sucesso = enviar_mensagem(
                telefone,
                mensagem
            )

            horario = datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )

            if sucesso:

                enviados += 1

                salvar_log(
                    f"{horario} - ENVIADO - {nome} - {telefone}"
                )

            else:

                erros += 1

                salvar_log(
                    f"{horario} - ERRO - {nome} - {telefone}"
                )

        except Exception as erro:

            print(f"Erro geral com {motorista}")

            print(erro)

            erros += 1

    print("\n======== RESUMO ========")

    print(f"✅ Enviados: {enviados}")

    print(f"❌ Erros: {erros}")

    print("\nLogs salvos em logs/envios.log")


if __name__ == "__main__":
    main()