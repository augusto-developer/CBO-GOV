# CBO-GOV

Bem-vindo ao repositório **CBO-GOV**! Este projeto oferece uma automação simples e eficaz para ajudar sua empresa a manter as descrições dos **CBOs (Classificação Brasileira de Ocupações)** em conformidade com os dados oficiais do governo. 

Se você já encontrou descrições incompatíveis entre o que está em seu documento e o que consta no site oficial, essa ferramenta pode ser a solução que você procura. A automação atualiza a descrição do código, caso haja uma correspondência no site do governo, facilitando a organização e atualização dos dados.


## Requisitos

Para rodar este programa, você precisa garantir que os seguintes requisitos estejam instalados:

1. **Python** (versão 3.6 ou superior)
2. **Selenium** – Biblioteca para automação de navegação na web
3. **Pandas** – Biblioteca para manipulação de dados
4. **WebDriver Manager** – Gerenciador automático do WebDriver necessário para o Selenium
5. **Google Chrome** – Navegador para execução do Selenium


## Como Usar

1. **Baixe e Extraia o Código:**
   - Extraia a pasta para qualquer local em seu computador.
   
2. **Configuração Inicial:**
   - Abra o código Python e atualize o caminho para o arquivo Excel no código. Este arquivo contém os dados dos CBOs e as colunas devem estar no formato:

     ```
     Código | Cargo | Descrição
     ```

3. **Arquivo de Exemplo:**
   - Na pasta, você encontrará arquivos de exemplo. O arquivo `CBOTest.xlsx` serve como base para o formato correto. Certifique-se de que o seu arquivo de dados esteja no mesmo formato.

4. **Execução:**
   - Execute o código Python. O programa vai buscar as descrições no site oficial do CBO e atualizar as informações no seu arquivo Excel.

5. **Processamento:**
   - Após executar o código, aguarde até que o processamento seja concluído. O código irá substituir as descrições existentes por aquelas obtidas do site do governo.


## Atenção

- **Feche o Arquivo de Saída:**
  Antes de executar o código, certifique-se de que o arquivo de saída esteja fechado. Isso é necessário para garantir que as alterações sejam salvas corretamente.

- **Múltiplos Processamentos:**
  Caso deseje executar o código para diferentes casos de uso, **não se esqueça de alterar o nome do arquivo de saída** para evitar sobrescrever arquivos existentes.


## Instalação das Dependências

Para garantir que todas as bibliotecas necessárias estejam instaladas, execute o seguinte comando no terminal:

```bash
pip install selenium pandas webdriver-manager
```


## Vídeo Explicativo:
em breve...
