-- Active: 1675141582370@@35.226.146.116@3306
CREATE TABLE robochatbot (
  id INT AUTO_INCREMENT PRIMARY KEY,
  numero_telefone VARCHAR(20) NOT NULL,
  mensagem TEXT NOT NULL,
  resposta TEXT NOT NULL,
  data_hora DATETIME NOT NULL
);

CREATE TABLE Usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(50) NOT NULL,
  numero_telefone VARCHAR(20) NOT NULL,
  email VARCHAR(100) NOT NULL,
  preferencias TEXT
);

CREATE TABLE RespostasPadrao (
  id INT AUTO_INCREMENT PRIMARY KEY,
  pergunta TEXT NOT NULL,
  resposta TEXT NOT NULL
);


CREATE TABLE Contexto (
  id INT AUTO_INCREMENT PRIMARY KEY,
  numero_telefone VARCHAR(20) NOT NULL,
  pergunta_atual TEXT NOT NULL,
  resposta_parcial TEXT
);


CREATE TABLE Produtos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  descricao TEXT NOT NULL,
  preco DECIMAL(10, 2) NOT NULL,
  disponibilidade INT NOT NULL
);
