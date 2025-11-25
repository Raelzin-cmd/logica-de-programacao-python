Para utilizar biblioteca externas, é importante que nao instale no computador, mas em cada projeto que for utiliza-lo.

Iremos instalar o pacote .venv para usarmos localmente as bibliotecas.

```bash
python -m venv .venv
```

E ativar o ambiente virtual

```bash
source .venv/Scripts/activate
```

E verifique o caminho que o venv está utilizando

```bash
which python
```

Para verficar que está ativo: 

```bash
python -m pip list
```

Para desativar:

```bash
deactivate
```

SEMPRE ative o ambiente virtual no projeto para que nada seja instalado de forma global, e ao terminar o projeto, desative o ambiente virtual.

Instale o pacote arrow:

```bash
python -m pip install arrow
```
