# Modulo-Visualizacao-de-Dados
Estou no capitulo de vizualização de gráficos no curso de cientista de dados da EBAC. aonde me pediram para criar 5 gráficos diferentes (Calor, Pizza, Disperção, Barra, Densidade de um CSV de um e-commerce.

Este projeto realiza um pipeline completo de **Análise Exploratória de Dados (EDA)**, **Limpeza de Dados (Data Cleaning)** e **Visualização** utilizando uma base de dados de um e-commerce. O objetivo principal foi padronizar variáveis categóricas altamente bagunçadas, tratar inconsistências e gerar gráficos estatísticos claros para tomada de decisão.

---

## 🚀 Tecnologias Utilizadas

* **Python 3**
* **Pandas**: Manipulação, filtragem e limpeza dos dados estruturados.
* **Matplotlib**: Construção da estrutura dos gráficos e customizações de eixos.
* **Seaborn**: Plotagens estatísticas avançadas (KDE e Heatmap).

---

## 🛠️ Etapas de Tratamento de Dados (Data Cleaning)

A base original continha diversas inconsistências textuais e dados ausentes. As seguintes correções foram implementadas com sucesso:

### 1. Tratamento de Dados Ausentes (Missing Values)
* A coluna `Desconto` possuía valores nulos, os quais foram preenchidos com o termo padrão `"Sem Desconto"` usando `.fillna()`.
* Linhas com valores nulos críticos nas demais colunas foram removidas para garantir a integridade das análises matemáticas.

### 2. Padronização da Coluna `Temporada`
Havia muita variação de escrita para o mesmo período do ano (ex: misturando barras e traços). O texto foi limpo com `.str.strip()` e unificado via dicionário de mapeamento:
* `primavera/verão`, `primavera-verão` ➡️ **`pv`**
* `outono/inverno`, `outono-inverno` ➡️ **`oi`**
* Junções de todas as estações ➡️ **`pvoi`**
* O ano inválido `2021` foi removido da análise de temporadas.

### 3. Conversão de Texto para Número (`Qtd_Vendidos`)
Os dados de vendas estavam salvos como string (ex: `+100`, `+10mil`). Criou-se uma coluna numérica real (`Qtd_Vendidos_Num`) convertendo termos como `+10mil` para `10000`, permitindo a realização de operações matemáticas legítimas de soma e agrupamento.

### 4. Agrupamento de Baixa Frequência na Coluna `Gênero`
A coluna continha categorias com apenas 1 ou 2 registros (ex: nomes de produtos ou frases longas). 
* Termos como *Meninos*, *Meninas* e *Bebês* foram unificados em **`Infantil`**.
* Termos como *Unissex* e *Sem gênero* foram unificados em **`Sem Gênero`**.
* **Uso Estratégico do `.loc`**: Qualquer texto que estivesse fora das categorias oficiais foi movido automaticamente para a categoria **`Outros`**, eliminando ruídos nos dados.

---

## 📊 Visualizações Geradas

O script gera **5 gráficos fundamentais** para a análise do negócio:

1.  **Gráfico de Barras (Volume por Temporada):** Apresenta a soma real de produtos vendidos em cada período (`pv`, `oi`, `pvoi`).
2.  **Gráfico de Pizza (Proporção de Vendas):** Demonstra o percentual de participação de cada temporada no total vendido.
3.  **Gráfico de Dispersão (Avaliações vs Notas):** Cruza a nota dos produtos com a quantidade de avaliações recebidas para entender a satisfação do cliente.
4.  **Mapa de Calor (Gênero x Temporada):** Uma tabela cruzada que mostra de forma térmica quais públicos compram mais em quais épocas do ano.
5.  **Gráfico de Densidade (Distribuição de Notas):** Uma curva contínua (KDE) que exibe a concentração das notas dadas aos produtos da plataforma.

---

## 📁 Como Executar o Projeto

1. Certifique-se de ter o arquivo contendo a base de dados `ecommerce_preparados.csv` no mesmo diretório do script.
2. Instale as dependências necessárias através do terminal:
   ```bash
   pip install pandas matplotlib seaborn
