-- Top 10 operadoras com maiores despesas no 4º Trimestre de 2024

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


-- Top 10 operadoras com maiores despesas no ano de 2024

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
