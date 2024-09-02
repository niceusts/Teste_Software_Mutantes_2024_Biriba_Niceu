# Aluno: Niceu Santos Biriba  
**Turma de Testes de Software, Universidade Federal de Sergipe**

## Atividade 2 - Guia de Testes de Mutação para Projetos Python

Este documento descreve o processo de configuração e execução de testes de mutação em um projeto Python, utilizando o WSL (Windows Subsystem for Linux), Ubuntu, e ferramentas como `pytest`, `pytest-cov`, e `mutmut`.

## Documentos e Artefatos

- [Documento tutorial em PDF](https://github.com/niceusts/Teste_Software_Mutantes_2024_Biriba_Niceu/blob/main/Artefatos/Niceu_Biriba_atividade_2.pdf)


## Instalação e Configuração

### 1. Instalação do WSL e Atualização da Imagem do Ubuntu

1. **Caso esteja no windows é necessário instalar o WSL (Windows Subsystem for Linux)**:
    ```bash
    wsl --install
    ```

2. **Atualizar a imagem do Ubuntu**:
    ```bash
    sudo apt update
    sudo apt install build-essential
    ```

### 2. Configuração do Ambiente Virtual

1. **Instalar o `venv` no projeto**:
    ```bash
    python3 -m venv venv
    ```
2. **Instalar o make para rodar o arquivo Makefile que contem as configurações do projeto**:
    Utilize o comando:
    ```bash
    make install
    ```
3. **Instalar os dependencias no projeto**:
    ```bash
    make dev
    ```
4. **Criar e Ativar o Ambiente Virtual**:
    No diretório do repositório, execute:
    ```bash
    source venv/bin/activate
    ```

### 3. Uso do Makefile
1. **Comandos Adicionais**:
    - **Limpar o Projeto**:
        ```bash
        make clean
        ```
    - **Executar Testes**:
        ```bash
        make test
        ```
    - **Criar Distribuição do Projeto**:
        ```bash
        make dist
        ```
    **Nota**: Caso ocorra algum erro, verifique a compatibilidade da rota de instalação do `pip` no arquivo `venv`. O trecho abaixo pode ser adicionado ao seu `Makefile`:
    ```makefile
    dev: ## create dev env
        python3 -m venv venv --prompt cards_proj
        venv/bin/pip install -U pip
        venv/bin/pip install pytest tox pytest-cov coverage mutmut
        venv/bin/pip install -e .
    ```

### 4. Execução de Testes

1. **Executar Testes Disponíveis**:
    Para testar arquivos específicos, execute:
    ```bash
    pytest -vv tests/api/nome_arquivo.py
    pytest -vv tests/cli/nome_arquivo.py
    ```

    Para rodar todos os testes:
    ```bash
    pytest -vv
    ```

    Salvar/Exibir resultados dos testes em uma página .html
    ```bash
    pytest -vv --cov=cards --cov-branch --cov-report html
    ```

### 5. Testes de Mutação com `mutmut`

1. **Executar Testes de Mutação**:
    ```bash
    mutmut run
    ```

2. **Ver Resultados do `mutmut`**:
    ```bash
    mutmut results
    ```

3. **Mostrar um Teste Específico**:
    ```bash
    mutmut show <id>
    ```

4. **Salvar Resultados em um Arquivo de Texto**:
    ```bash
    mutmut results > resultados_mutmut.txt
    ```

## Recursos Adicionais

- [Documentação do Python](https://www.python.org/)
- [pytest](https://docs.pytest.org/en/stable/)
- [pytest-cov](https://pypi.org/project/pytest-cov/)
- [mutmut](https://github.com/boxed/mutmut)

---

## Melhorias Realizadas

### Casos de Teste Adicionados
- **Arquivo `src/cards/api.py`**: Adicionados testes para cobrir as linhas 2, 4, 6, 9, 14. Esses testes verificam a inicialização e a manipulação dos atributos da classe `Card`.
- **Arquivo `src/cards/cli.py`**: Adicionados testes para cobrir as linhas 41-42, 64-67, 73, 86, 89-91, 95-96. Estes testes verificam a lógica condicional e a manipulação de dados.

### Mudanças na Cobertura de Testes
- **Verificação de Tipos Inválidos**: Foram adicionados testes para verificar se o código lida corretamente com anotações de tipo inválidas.

### Comparação de Resultados
- **Resultados Anteriores**:
-   ![image](https://github.com/user-attachments/assets/ffb807fb-6832-4858-b2d0-7e3b2758ae23)



- **Resultados Atuais**:
- ![Imagem do WhatsApp de 2024-09-01 à(s) 23 33 57_0898a31e](https://github.com/user-attachments/assets/426df612-3550-42fb-831f-abd55a7309e3)
- ![Imagem do WhatsApp de 2024-09-01 à(s) 23 03 33_95fffc58](https://github.com/user-attachments/assets/c11eba32-944d-45f5-b1e9-55cf7fef4691)



### Conclusão
A adição de novos casos de teste e a revisão dos testes existentes resultaram em uma melhor detecção de mutantes, melhorando a robustez e a confiabilidade do código.

----

Como usar o software de Cards
---------------------------------

Aqui está uma demonstração de como funciona:

    $ cards add a todo
    $ cards add -o Brian another task
    $ cards list

    ID   state   owner   summary
    ───────────────────────────────────
    1    todo            a todo
    2    todo    Brian   another task

    $ cards update 1 -o Brian


    $ cards finish 1
    $ cards

      ID   state   owner   summary
     ───────────────────────────────────
      1    done    Brian   a todo
      2    todo    Brian   another task


    $ cards delete 1
    $ cards

      ID   state   owner   summary
     ───────────────────────────────────
      2    todo    Brian   another task

    $ cards --help

     Usage: cards [OPTIONS] COMMAND [ARGS]...

     Cards is a small command line task tracking application.

    ╭─ Options ────────────────────────────────────────────────────────╮
    │ --help          Show this message and exit.                      │
    ╰──────────────────────────────────────────────────────────────────╯
    ╭─ Commands ───────────────────────────────────────────────────────╮
    │ add       Add a card to db.                                      │
    │ config    List the path to the Cards db.                         │
    │ count     Return number of cards in db.                          │
    │ delete    Remove card in db with given id.                       │
    │ finish    Set a card state to 'done'.                            │
    │ list      List cards in db.                                      │
    │ start     Set a card state to 'in prog'.                         │
    │ update    Modify a card in db with given id with new info.       │
    │ version   Return version of cards application                    │
    ╰──────────────────────────────────────────────────────────────────╯
