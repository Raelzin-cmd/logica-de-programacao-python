# O que é __pycache__ ?

O arquivo .pyc é uma versão compilada do seu código Python.

Explicando de forma simples:

- O Python não executa diretamente o código escrito em texto (.py)
- Ele primeiro converte esse código em uma forma chamada bytecode (algo mais próximo da linguagem da máquina virtual do Python)
- Esse bytecode é armazenado como um arquivo .pyc

Assim, na próxima vez que o módulo for importado, o Python já terá o bytecode pronto e não precisará recompilar

Resultado: executa mais rápido.