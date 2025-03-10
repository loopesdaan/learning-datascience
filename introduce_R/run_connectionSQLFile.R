require(DBI)
require(RMySQL)  # Use RMariaDB se estiver usando MariaDB

# Estabelecendo a conexão com o banco de dados
con <- dbConnect(RMySQL::MySQL(), 
                 dbname = "db_learning",  # Nome do banco de dados
                 host = "127.0.0.1",  # Endereço do servidor MySQL
                 user = "dbuser01",  # Nome do usuário
                 password = "password")  # Senha do usuário

# Executar a consulta e ler a tabela no R
query <- "SELECT * FROM persons_score"  # Sua consulta SQL
df <- dbGetQuery(con, query)

# Exibir os dados
print(df)

# Fechar a conexão
dbDisconnect(con)

head(df)
