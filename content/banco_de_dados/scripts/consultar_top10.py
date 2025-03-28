import psycopg2
import pandas as pd

# Conexão com o banco
conn = psycopg2.connect(
    dbname="teste_intuitive",
    user="intuitive",
    password="intuitive",
    host="localhost",
    port="5432"
)

# 4º Trimestre de 2024
query_trimestre = """
SELECT 
    reg_ans,
    SUM(vl_saldo_final) AS total_despesa
FROM saldos_contabeis_trimestrais
WHERE descricao ILIKE '%SINISTROS CONHECIDOS%'
  AND descricao ILIKE '%ASSISTÊNCIA A SAÚDE%'
  AND data BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY reg_ans
ORDER BY total_despesa DESC
LIMIT 10;
"""

# Ano completo de 2024
query_ano = """
SELECT 
    reg_ans,
    SUM(vl_saldo_final) AS total_despesa
FROM saldos_contabeis_trimestrais
WHERE descricao ILIKE '%SINISTROS CONHECIDOS%'
  AND descricao ILIKE '%ASSISTÊNCIA A SAÚDE%'
  AND data BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY reg_ans
ORDER BY total_despesa DESC
LIMIT 10;
"""

# Executar e imprimir resultados
print("Top 10 - 4º Trimestre de 2024:")
df_tri = pd.read_sql_query(query_trimestre, conn)
print(df_tri)

print("\nTop 10 - Ano de 2024:")
df_ano = pd.read_sql_query(query_ano, conn)
print(df_ano)

conn.close()