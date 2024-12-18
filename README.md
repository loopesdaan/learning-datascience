## Learning Data Science

> Este projeto integra análises de dados utilizando Python e R para fornecer uma abordagem prática em análise de dados e visualização interativa para iniciantes.

---

### Índice

1. [Sobre o Projeto](#sobre-o-projeto)
2. [Funcionalidades](#funcionalidades)
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)
4. [Instalação e Configuração](#instalação-e-configuração)
5. [Exemplos de Uso](#exemplos-de-uso)

---

### Sobre o Projeto

> O objetivo deste projeto é realizar análises de dados utilizando bibliotecas Python e R para manipulação dos dados.

---

### Funcionalidades

- Análise exploratória de dados utilizando Python.
- Modelagem estatística utilizando R.
- Geração de gráficos interativos.
- Exportação de resultados em formatos como CSV, JSON, ou RDS.
- Integração entre Python e R para execução de scripts de forma automatizada.

---

## Tecnologias Utilizadas


#### Python:

- `pandas` – Texto.
- `polars` – Texto.
- `pyspark` – Texto.
- `numpy` – Texto.

#### R:

- `dplyr` – Manipulação de dados.
- `ggplot2` – Visualização de dados.
- `tidyr` – Limpeza e organização de dados.

---

## Instalação e Configuração

> Este projeto foi desenvolvido em um ambiente Mac Os X, logo os comandos abaixo, em grande maioria, serão aplicado em `bash`.

#### Pré-requisitos

Antes de começar, você precisa ter:

- Python 3.x instalado.
- R instalado.
- Acesso ao terminal.

#### Passos para instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-projeto.git
   cd seu-projeto
   ```

2. Instale as dependências do Python:

   ```bash
   pip install -r requirements.txt
   ```

3. Instale as dependências do R (caso tenha algum script em R):

   ```R
   install.packages(c("dplyr", "ggplot2", "rpy2"))
   ```

4. Configure o ambiente de integração (caso seja necessário):
   ```bash
   pip install rpy2
   ```

---

## Exemplos de Uso

#### Exemplo 1: Análise de Dados com Python

```python
import pandas as pd

# Carregar os dados
data = pd.read_csv('dados.csv')

# Realizar análise básica
summary = data.describe()
print(summary)
```

#### Exemplo 2: Executando Script em R via Python

```python
import rpy2.robjects as ro

# Definir o código R
r_code = """
library(ggplot2)
data <- data.frame(x = c(1, 2, 3, 4), y = c(1, 4, 9, 16))
ggplot(data, aes(x, y)) + geom_line()
"""

# Executar o código R
ro.r(r_code)
```

---

