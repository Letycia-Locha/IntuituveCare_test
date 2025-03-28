-- Tabela de saldos contábeis trimestrais
CREATE TABLE IF NOT EXISTS saldos_contabeis_trimestrais (
    id SERIAL PRIMARY KEY,
    data DATE,
    reg_ans INTEGER,
    cd_conta_contabil VARCHAR(20),
    descricao TEXT,
    vl_saldo_inicial NUMERIC(18,2),
    vl_saldo_final NUMERIC(18,2)
);

-- Tabela de operadoras ativas
CREATE TABLE IF NOT EXISTS cadastro_operadoras_ans (
    registro_ans INTEGER PRIMARY KEY,
    cnpj VARCHAR(20),
    razao_social TEXT,
    nome_fantasia TEXT,
    modalidade TEXT,
    logradouro TEXT,
    numero TEXT,
    complemento TEXT,
    bairro TEXT,
    cidade TEXT,
    uf VARCHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(5),
    telefone TEXT,
    fax TEXT,
    endereco_eletronico TEXT,
    representante TEXT,
    cargo_representante TEXT,
    regiao_de_comercializacao TEXT,
    data_registro_ans DATE
);