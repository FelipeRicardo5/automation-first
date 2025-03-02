# README - Automação de Teste com Selenium

## Descrição

Este script automatiza o processo de login, adição de produto ao carrinho e remoção de produto no site de demonstração **SauceDemo** (https://www.saucedemo.com/), utilizando a biblioteca Selenium.

A automação simula a interação de um usuário no site, realizando as seguintes etapas:

1. Acesso à página inicial.
2. Login com credenciais válidas.
3. Adição de um produto ao carrinho de compras.
4. Verificação do contador do carrinho.
5. Remoção do produto do carrinho.
6. Verificação do contador do carrinho após a remoção.

## Dependências

- **Selenium**: Biblioteca para controle do navegador e automação de testes web.
- **WebDriver**: O script utiliza o driver do Chrome (`chromedriver`).

## Requisitos

1. Instalar o Python (recomenda-se a versão 3.6 ou superior).
2. Instalar o Selenium:

```bash
pip install selenium
```

3. Baixar o **ChromeDriver** compatível com sua versão do Google Chrome a partir do [site oficial do ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/).

4. Certificar-se de que o `chromedriver` esteja no PATH do sistema ou especificar o caminho correto no código.

## Estrutura do Código

### 1. Configuração do Driver

O script inicia com a configuração do driver para o navegador Chrome. Ele instancia o `webdriver.Chrome()` para controlar o navegador.

### 2. Acesso ao Site

O navegador é direcionado para o site de demonstração `https://www.saucedemo.com/` e a janela do navegador é maximizada para facilitar a visualização.

### 3. Login

As credenciais de login são preenchidas nos campos correspondentes e o botão de login é acionado. O login é realizado com sucesso utilizando os seguintes dados:
- **Usuário**: `standard_user`
- **Senha**: `secret_sauce`

### 4. Adição de Produto ao Carrinho

O script aguarda a carga da página de produtos e então localiza o botão para adicionar um produto ao carrinho. O produto selecionado é o "Sauce Labs Backpack", e o botão de adicionar ao carrinho é clicado.

### 5. Verificação do Contador do Carrinho

Após a adição do produto, o script verifica se o contador do carrinho foi atualizado para "1".

### 6. Remoção de Produto do Carrinho

O script então navega para o carrinho de compras, localiza o botão para remover o produto e executa a remoção.

### 7. Verificação do Contador Após Remoção

O script aguarda e verifica se o contador do carrinho foi atualizado para "0" após a remoção do produto.

### 8. Encerramento do Navegador

Independentemente do sucesso ou falha do script, o navegador é fechado ao final da execução do script com `driver.quit()`.

## Execução

1. Clone o repositório ou baixe o arquivo Python.
2. Certifique-se de que o `chromedriver` está configurado corretamente.
3. Execute o script:

```bash
python script_automacao.py
```

## Exceções

Durante a execução, se ocorrer algum erro, o script irá capturar e exibir uma mensagem de erro. Exceções como a falha em localizar elementos ou problemas de carregamento da página são tratadas com `try-except`.

## Possíveis Melhorias

- **Tratamento de Erros Mais Detalhado**: O script pode ser aprimorado para tratar erros de maneira mais específica, informando qual etapa falhou.
- **Uso de Esperas Explícitas**: Embora já esteja sendo usado o `WebDriverWait`, o uso mais abrangente de esperas explícitas pode melhorar a robustez.
- **Execução em Diferentes Navegadores**: A automação pode ser estendida para outros navegadores, como Firefox, utilizando o respectivo WebDriver.

---

## Autor

Desenvolvido por: Felipe Ricardo B. Ferreira

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para mais detalhes.
