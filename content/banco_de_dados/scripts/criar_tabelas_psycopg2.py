import psycopg2

conn = psycopg2.connect(
    dbname="teste_intuitive",
    user="intuitive",
    password="intuitive",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS saldos_contabeis_trimestrais (
    id SERIAL PRIMARY KEY,
    data DATE,
    reg_ans INTEGER,
    cd_conta_contabil VARCHAR(20),
    descricao TEXT,
    vl_saldo_inicial NUMERIC(18,2),
    vl_saldo_final NUMERIC(18,2)
)
""")

conn.commit()
cur.close()
conn.close()

print("Tabela criada com sucesso.")