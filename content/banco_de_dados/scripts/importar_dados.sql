-- Importar dados de saldos contábeis (ajuste o caminho conforme necessário)
COPY saldos_contabeis_trimestrais(data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'content/banco_de_dados/demonstracoes_contabeis/todos_os_saldos.csv'
DELIMITER ';'
ENCODING 'UTF8'
CSV HEADER;

-- Importar dados das operadoras ativas
COPY cadastro_operadoras_ans(
    registro_ans, cnpj, razao_social, nome_fantasia, modalidade,
    logradouro, numero, complemento, bairro, cidade, uf, cep,
    ddd, telefone, fax, endereco_eletronico, representante,
    cargo_representante, regiao_de_comercializacao, data_registro_ans
)
FROM 'content/banco_de_dados/operadoras/Relatorio_cadop.csv'
DELIMITER ';'
ENCODING 'UTF8'
CSV HEADER;