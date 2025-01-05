import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configurações iniciais do arquivo Excel e da planilha
caminho_arquivo_excel = "caminhoDaPasta\\CBOTest.xlsx"
nome_planilha = "Planilha1"

# Leitura do arquivo Excel
df = pd.read_excel(caminho_arquivo_excel, sheet_name=nome_planilha, header=0)

# Configuração do WebDriver
service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)

# Função para buscar descrição
def buscar_descricao(codigo):
    navegador.get("https://cbo.mte.gov.br/cbosite/pages/pesquisas/BuscaPorCodigo.jsf")
    time.sleep(2)

    # Inserir o código e buscar
    input_element = navegador.find_element(By.XPATH, '//*[@id="formBuscaPorCodigo"]/div[3]/input[1]')
    input_element.click()
    input_element.send_keys(codigo)
    time.sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="formBuscaPorCodigo:btConsultarCodigo"]').click()
    time.sleep(2)

    descricao = None
    try:
        # Esperar o link do código carregar e clicar nele
        link_element = WebDriverWait(navegador, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="formBuscaPorCodigo:objetos:tbody_element"]/tr/td[2]/p/a'))
        )
        link_element.click()
        time.sleep(2)

        # Procurar pela linha correta no id=list2 onde o código está presente
        tabela_element = WebDriverWait(navegador, 20).until(
            EC.presence_of_element_located((By.ID, 'list2'))
        )

        # Iterar sobre as linhas e verificar o código na primeira linha, depois capturar a descrição
        linhas = tabela_element.find_elements(By.TAG_NAME, 'tr')
        for linha in linhas:
            try:
                # Obter o texto do título do código e verificar se corresponde ao código buscado
                titulo_element = linha.find_element(By.TAG_NAME, 'p').find_element(By.TAG_NAME, 'span')
                titulo_texto = titulo_element.text.strip()
                if titulo_texto.startswith(f"{codigo} -"):
                    # Encontrar a descrição correspondente abaixo do título
                    descricao_element = linha.find_elements(By.TAG_NAME, 'p')[1]
                    descricao = descricao_element.text.strip()
                    break
            except Exception:
                continue

    except Exception as e:
        print(f"Erro ao capturar a descrição para o código {codigo}: {e}")

    return descricao  # Retorna None se não encontrar descrição

# Identificar a coluna de Descrição
descricao_coluna = df.columns[2]  # Nome da coluna de Descrição (assumindo que é a terceira coluna)

# Garantir que a coluna de descrição seja do tipo string
df[descricao_coluna] = df[descricao_coluna].astype(str)

# Dicionário para evitar buscas duplicadas
codigos_ja_processados = {}

# Loop para processar cada código no DataFrame
for index, row in df.iterrows():
    codigo = row.iloc[0]  # Assumindo que o código está na primeira coluna
    descricao_existente = row[descricao_coluna]

    # Verificar se o código já foi processado anteriormente
    if codigo in codigos_ja_processados:
        print(f"Código {codigo} já processado anteriormente.")
        # Copiar a descrição já obtida
        df.at[index, descricao_coluna] = codigos_ja_processados[codigo]
    else:
        # Se não foi processado e não há descrição válida, buscar descrição
        if pd.isna(descricao_existente) or descricao_existente.strip().lower() in ["", "nan"]:
            print(f"Buscando descrição para o código {codigo}...")
            descricao = buscar_descricao(codigo)
            if descricao:
                # Atualizar o DataFrame e armazenar no dicionário de códigos processados
                df.at[index, descricao_coluna] = descricao
                codigos_ja_processados[codigo] = descricao
            else:
                # Atribuir None se a descrição não for encontrada
                print(f"Descrição não encontrada para o código {codigo}. Atribuindo None.")
                df.at[index, descricao_coluna] = None
                codigos_ja_processados[codigo] = None  # Armazenar None para evitar buscas duplicadas
        else:
            # Se já existe uma descrição, armazenar no dicionário de códigos processados
            codigos_ja_processados[codigo] = descricao_existente

# Salvar o DataFrame atualizado no Excel
caminho_saida_excel = "caminhoDaPasta\\CBO.xlsx"
df.to_excel(caminho_saida_excel, index=False)
print("Atualização concluída e salva no arquivo Excel.")

# Fechar o navegador
navegador.quit()
