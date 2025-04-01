-- 1. Top 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS"
-- no último trimestre
SELECT 
    o.nome_fantasia, 
    SUM(d.vl_saldo_final) AS total_despesas
FROM despesas d
JOIN operadoras o ON d.reg_ans = o.registro_ans::INTEGER
WHERE d.descricao ILIKE '%SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
AND d.data >= '2024-10-01'  -- Início do último trimestre de 2024
AND d.data <= '2024-12-31'  -- Fim do último trimestre de 2024
GROUP BY o.nome_fantasia
ORDER BY total_despesas DESC
LIMIT 10;


-- 2. Top 10 operadoras com maiores despesas no último ano
SELECT 
    o.nome_fantasia, 
    SUM(d.vl_saldo_final) AS total_despesas
FROM despesas d
JOIN operadoras o ON d.reg_ans = o.registro_ans::INTEGER
WHERE d.descricao ILIKE '%SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
AND d.data >= '2024-01-01'  -- Início de 2024
AND d.data <= '2024-12-31'  -- Fim de 2024
GROUP BY o.nome_fantasia
ORDER BY total_despesas DESC
LIMIT 10;