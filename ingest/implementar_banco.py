import sqlite3
import pandas as pd

# --- Etapa 1: Definição dos Arquivos e Caminhos ---
# Os caminhos agora são relativos à pasta onde o script está sendo executado.
# O ".." significa "voltar uma pasta".
sql_file = '../db/schema_sqlite.sql'
csv_file = 'todos_os_dados_sensores.csv'
db_file = '../db/sensores.db'

print("Iniciando a integração do projeto...")

# Conecta-se ao banco de dados SQLite
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# --- Etapa 2: Criação das tabelas do banco de dados ---
try:
    print(f"Lendo o script SQL do arquivo {sql_file}...")
    with open(sql_file, 'r') as f:
        sql_script = f.read()

    # Executa o script SQL para criar as tabelas
    cursor.executescript(sql_script)
    print("Tabelas do banco de dados criadas com sucesso.")

except FileNotFoundError:
    print(f"Erro: O arquivo SQL '{sql_file}' não foi encontrado. Verifique se ele está na pasta 'db'.")
    conn.close()
    exit()
except sqlite3.Error as e:
    print(f"Erro ao criar as tabelas: {e}")
    conn.close()
    exit()

# --- Etapa 3: Inserção dos dados do CSV para o banco de dados ---
try:
    print(f"Lendo os dados do arquivo CSV {csv_file}...")
    df = pd.read_csv(csv_file)

    # Remove a primeira linha com valores nulos, que é um problema comum em CSVs do Wokwi
    df = df.iloc[1:]

    # Renomeia as colunas para corresponder à tabela SQL
    df.columns = ['amostra', 'temperatura', 'umidade', 'aceleracao_x', 'aceleracao_y', 'aceleracao_z', 'potenciometro']

    # Converte tipos para garantir que correspondam ao schema do SQLite
    df['amostra'] = df['amostra'].astype(int)
    df['temperatura'] = pd.to_numeric(df['temperatura'], errors='coerce')
    df['umidade'] = pd.to_numeric(df['umidade'], errors='coerce')
    df['aceleracao_x'] = df['aceleracao_x'].astype(int)
    df['aceleracao_y'] = df['aceleracao_y'].astype(int)
    df['aceleracao_z'] = df['aceleracao_z'].astype(int)
    df['potenciometro'] = df['potenciometro'].astype(int)

    # Insere os dados do DataFrame na tabela 'LeiturasSensor'
    df.to_sql('LeiturasSensor', conn, if_exists='replace', index=False)
    print("Dados do arquivo CSV inseridos na tabela 'LeiturasSensor' com sucesso!")

except FileNotFoundError:
    print(f"Erro: O arquivo CSV '{csv_file}' não foi encontrado. Verifique se ele está na pasta 'ingest'.")
    conn.close()
    exit()
except Exception as e:
    print(f"Ocorreu um erro ao processar o CSV: {e}")
    conn.close()
    exit()

# --- Etapa 4: Inserindo dados na tabela 'Sensores' para complementar o DER ---
try:
    cursor.execute("INSERT OR IGNORE INTO Sensores (id_sensor, tipo, localizacao) VALUES (?, ?, ?)", (1, 'DHT22', 'Linha de Produção 1'))
    cursor.execute("INSERT OR IGNORE INTO Sensores (id_sensor, tipo, localizacao) VALUES (?, ?, ?)", (2, 'MPU6050', 'Máquina de Corte'))
    cursor.execute("INSERT OR IGNORE INTO Sensores (id_sensor, tipo, localizacao) VALUES (?, ?, ?)", (3, 'Potenciometro', 'Esteira de Montagem'))
    conn.commit()
    print("Dados de sensores inseridos na tabela 'Sensores' com sucesso.")
except sqlite3.Error as e:
    print(f"Erro ao inserir dados na tabela 'Sensores': {e}")
finally:
    conn.close()

print("Processo de integração concluído. O arquivo sensores.db está pronto.")
