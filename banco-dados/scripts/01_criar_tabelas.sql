-- Criando a tabela de demonstrativos contábeis
CREATE TABLE despesas (
    DATA DATE,
    REG_ANS INTEGER,
    CD_CONTA_CONTABIL INTEGER,
    DESCRICAO TEXT,
    VL_SALDO_INICIAL NUMERIC(15, 2),
    VL_SALDO_FINAL NUMERIC(15, 2)
);


CREATE TABLE operadoras (
    registro_ans INTEGER,
    cnpj VARCHAR(20),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(255),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf VARCHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(5),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(100),
    regiao_de_comercializacao VARCHAR(10),
    data_registro_ans DATE
);
