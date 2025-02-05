# Guia de Execução do Script para Criação de Cards no Jira

## Requisitos

### 1. Instalação de Bibliotecas Python
Certifique-se de ter o Python instalado (versão 3.6 ou superior). Em seguida, instale as bibliotecas necessárias:

```bash
pip3 install pandas 
pip3 install jira
```   

### 2. IDE Recomendada
Recomenda-se o uso de uma IDE para facilitar o desenvolvimento e a execução do script. Algumas opções populares:
- **Visual Studio Code**
- **PyCharm**
- **Jupyter Notebook** (para testes rápidos)

## Configurações do Jira
- **URL do Jira:** Ex: `https://seu-dominio.atlassian.net`
- **Usuário do Jira:** E-mail associado à sua conta Jira.
- **Token da API:** Gere o token na [página de gerenciamento de tokens do Atlassian](https://id.atlassian.com/manage/api-tokens).
- **Chave do Projeto:** O código do projeto no Jira (Ex: `PROJ`).

## Estrutura dos Arquivos CSV

### 1. `epicos.csv`
Contém as informações dos épicos já criados no Jira.

**Colunas obrigatórias:**
- `nome_epico`: Nome identificador do épico.
- `epico_id`: ID do épico no Jira.

**Exemplo:**
```csv
nome_epico,epico_id
EPI-123,EPIC-1001
EPI-124,EPIC-1002
```

### 2. `dados.csv`
Contém as informações das tarefas que serão criadas.

**Colunas obrigatórias:**
- `titulo`: Título da tarefa.
- `descricao`: Descrição da tarefa.
- `prioridade`: Prioridade da tarefa (Ex: `High`, `Medium`, `Low`).
- `epico`: Nome do épico correspondente (deve existir no `epicos.csv`).
- `responsavel`: Usuário responsável pela tarefa no Jira.

**Exemplo:**
```csv
titulo,descricao,prioridade,epico,responsavel
"Configurar ambiente de teste","Instalar dependências.","High","EPI-123","jose.silva"
"Revisar código do módulo X","Revisar o código.","Medium","EPI-124","maria.souza"
```

## Execução do Script

1. Configure as credenciais do Jira no script:
   ```python
   JIRA_URL = 'https://seu-dominio.atlassian.net'
   JIRA_USER = 'seu-email@dominio.com'
   JIRA_API_TOKEN = 'seu-token-api'
   JIRA_PROJECT_KEY = 'PROJ'
   ```

2. Coloque os arquivos `epicos.csv` e `dados.csv` na mesma pasta do script.

3. Execute o script:
   ```bash
   python jira_cards_from_csv.py
   ```

## Observações Importantes
- O script **não cria tarefas duplicadas**. Ele verifica se já existe uma tarefa com o mesmo `summary` antes de criar uma nova.
- O campo `customfield_10011` é usado para associar a tarefa ao épico. Verifique se este campo está configurado corretamente no seu Jira.

## Possíveis Erros e Soluções
- **Erro de autenticação:** Verifique o token da API e o e-mail usado.
- **Problemas com o campo de épico:** Confirme o ID do campo `customfield_10011` com o administrador do Jira.
- **Erro de permissão:** O usuário precisa ter permissão para criar tarefas no projeto especificado.

---

Agora é só configurar e executar o script para automatizar a criação de tarefas no Jira!

