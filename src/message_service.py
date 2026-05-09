def criar_mensagem(nome, empresa, valor, tipo_envio):

    if tipo_envio == "ADIANTAMENTO":

        mensagem = f"""
Olá {nome}, tudo bem?

Empresa: {empresa}

Valor do adiantamento: R$ {valor}

Favor emitir a NF conforme prazo combinado.

Obrigado.
"""

    else:

        mensagem = f"""
Olá {nome}, tudo bem?

Empresa: {empresa}

Valor do fechamento: R$ {valor}

Favor emitir a NF conforme prazo combinado.

Obrigado.
"""

    return mensagem