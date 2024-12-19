## Learning Data Science

> Este projeto integra análises de dados utilizando Python e R para fornecer uma abordagem prática em análise de dados e visualização interativa para iniciantes.

---

### Índice

1. [Sobre o repositorio](#sobre-o-repositorio)
2. [Funcionalidades](#funcionalidades)
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)
4. [Instalação e Configuração](#instalação-e-configuração)
5. [Exemplos de Uso](#exemplos-de-uso)
6. [Como Contribuir](#como-contribuir)
7. [Licença](#licença)

---

### Sobre o repositorio

> O objetivo deste projeto é realizar análises de dados utilizando bibliotecas Python e R para manipulação dos dados.

---

### Funcionalidades

- Análise exploratória de dados utilizando Python.
- Modelagem estatística utilizando R.
- Geração de gráficos interativos.
- Exportação de resultados em formatos como CSV.
- Integração entre Python e R para execução de scripts de forma automatizada.

---

### Bibliotecas Utilizadas


#### Python:

- `pandas` – Pandas é uma das bibliotecas mais populares para manipulação e análise de dados em Python..
- `polars` – Polars é uma biblioteca de manipulação de dados de alto desempenho escrita em Rust e com bindings em Python.
- `pyspark` – PySpark é a interface Python para o Apache Spark, um framework de processamento de dados distribuído.
- `numpy` – NumPy é uma biblioteca fundamental para a computação científica em Python.
- `seaborn`- Seaborn é uma biblioteca de visualização de dados em Python baseada no Matplotlib.
- `Matplotlib` - Biblioteca básica para criação de gráficos estáticos em Python, permitindo gerar gráficos 2D (e 3D com algumas extensões) como barras, linhas, dispersão, histograma.

#### R:

- `dplyr` – Manipulação de dados.
- `ggplot2` – Visualização de dados.
- `tidyr` – Limpeza e organização de dados.
- `lubridate`- Manipulação de datas e horários.
- `shiny` - Desenvolvimento de aplicações interativas.
- `knitr` - Criação de documentos dinâmicos.
- `data.table` - Manipulação de grandes volumes de dados.
- `stringr` - Manipulação de strings.
- `rpy2` - Integração com Python.

---

### Instalação e Configuração

> Este projeto foi desenvolvido em um ambiente Mac Os X, logo os comandos abaixo, em grande maioria, serão aplicado em `bash`.

#### Pré-requisitos

Antes de começar, você precisa ter:

- Python 3.x instalado.
- R instalado.
- RStudio.
- Visual Studio Code.
- Jupyter Notebook.
- Acesso ao terminal.

#### Passos para instalação

1. Clone o repositório:

   ```bash
   cd Desktop
   mkdir learning
   cd learning
   git clone https://github.com/loopesdaan/learning-datascience.git
   cd learning-datascience
   ```

2. Instale as dependências do Python:

   ```bash
   pip install -r requirements.txt
   ```

3. Instale as dependências do R (caso tenha algum script em R):

   ```R
   install.packages(c("dplyr", "ggplot2", "rpy2", "tidyr", "lubridate", "shiny", "knitr", "data.table", "stringr"))
   ```

4. Configure o ambiente de integração (caso seja necessário):

   ```bash
   pip install rpy2
   ```

---

### Exemplos de Uso

#### Exemplo 1: Análise de Dados com Python

```python
import pandas as pd

# Carregar os dados
data = pd.read_csv('Data/base_test.csv')

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
#### Exemplo 3: Executando Script em R

```r

require(ggplot2)

# Definir o código R
data <- data.frame(x = c(1, 2, 3, 4), y = c(1, 4, 9, 16))

ggplot(data, aes(x, y)) + geom_line()
```
---

### Como Contribuir

Contribuições são sempre bem-vindas! Se você deseja contribuir para o projeto, siga os passos abaixo:

1. **Faça um fork** deste repositório.
2. **Clone** o repositório para o seu computador:
    ```bash
    git clone https://github.com/loopesdaan/learning-datascience.git
    ```
3. **Crie uma nova branch** para sua contribuição:
    ```bash
    git checkout -b minha-contribuicao
    ```
4. **Realize suas alterações** e adicione as mudanças:
    ```bash
    git add .
    ```
5. **Faça commit** das suas mudanças:
    ```bash
    git commit -m "Descrição da minha contribuição"
    ```
6. **Envie as alterações para o seu fork**:
    ```bash
    git push origin minha-contribuicao
    ```
7. **Abra um pull request** para que possamos revisar suas alterações.

## Licença

Este projeto está licenciado sob a licença **MIT** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.



