#Create issues in JIRA from a CSV file
import pandas as pd
from jira import JIRA

# Configurações do JIRA
JIRA_URL = 'https://daanloopes.atlassian.net/'
JIRA_USER = 'danilo.silva.lopes@hotmail.com'
JIRA_API_TOKEN = '*****'
JIRA_PROJECT_KEY = 'DTSC'

# Conectar ao JIRA
jira_options = {'server': JIRA_URL}
jira = JIRA(options=jira_options, basic_auth=(JIRA_USER, JIRA_API_TOKEN))

# Ler o CSV de épicos já criados
epicos_df = pd.read_csv('epicos.csv')  # Arquivo contendo os épicos já criados

# Ler o CSV de tarefas
df = pd.read_csv('dados.csv')  # Substitua pelo caminho do seu arquivo CSV

# Fazer o join entre os dois DataFrames usando o campo 'epico'
df = df.merge(epicos_df, how='left', left_on='epico', right_on='nome_epico')

# Iterar sobre as linhas do CSV e criar cards no JIRA
for index, row in df.iterrows():
    summary = row.get('titulo', f'Tarefa {index + 1}')

    # Verificar se a tarefa já existe no JIRA
    jql_query = f'project = {JIRA_PROJECT_KEY} AND summary ~ "{summary}"'
    existing_issues = jira.search_issues(jql_query)

    if existing_issues:
        print(f'Tarefa já existe: {existing_issues[0].key}')
        continue  # Pula para a próxima tarefa

    issue_dict = {
        'project': {'key': JIRA_PROJECT_KEY},
        'summary': summary,
        'description': row.get('descricao_x', 'Sem descrição'),  # usa a descrição da tarefa
        'issuetype': {'name': 'Task'},
        'priority': {'name': row.get('prioridade', 'Medium')},
        'assignee': {'name': row.get('responsavel', '')},
        'customfield_10011': row.get('epico_id', None)  # ID do épico do arquivo epicos.csv
    }

    # Remover campos nulos
    issue_dict = {k: v for k, v in issue_dict.items() if v is not None and v != ''}

    try:
        new_issue = jira.create_issue(fields=issue_dict)
        print(f'Tarefa criada: {new_issue.key}')
    except Exception as e:
        print(f'Erro ao criar tarefa na linha {index + 1}: {e}')
