import psycopg2

conn = psycopg2.connect(
    dbname="teste_intuitive",
    user="intuitive",
    password="intuitive",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Caminho para o CSV consolidado
csv_path = "../demonstracoes_contabeis/todos_os_saldos.csv"

with open(csv_path, encoding='utf-8') as f:
    next(f)  # pula o cabeçalho
    cur.copy_expert(
        sql="""
        COPY saldos_contabeis_trimestrais(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
        FROM STDIN WITH CSV DELIMITER ';' NULL '' ENCODING 'UTF8'
        """,
        file=f
    )

conn.commit()
cur.close()
conn.close()

print("Importação com COPY concluída com sucesso.")