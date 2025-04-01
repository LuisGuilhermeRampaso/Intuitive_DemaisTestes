COPY operadoras(registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero,
complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante,
cargo_representante, regiao_de_comercializacao, data_registro_ans)
FROM 'C:\Users\luish\Desktop\TesteIntuitive\banco-dados\dados_ANS\dados_cadastrais_ativos.csv'
DELIMITER ';' CSV HEADER ENCODING 'LATIN1';

-- Importando os dados cadastrais das operadoras ativas
COPY operadoras_ativas(registro_ans, cnpj, razao_social, modalidade, uf, municipio)
FROM 'C:\dados_ANS\dados_cadastrais_ativos.csv'
DELIMITER ';' CSV HEADER ENCODING 'UTF8';
