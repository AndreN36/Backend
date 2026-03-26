-- Atividade SQL - Tabela Livros

-- Passo 1: Criar a tabela Livros
CREATE TABLE Livros (
    id INT PRIMARY KEY,
    titulo VARCHAR(100),
    autor VARCHAR(100),
    ano INT,
    genero VARCHAR(50),
    disponivel BOOLEAN
);

-- Passo 2: Inserir livros
INSERT INTO Livros (id, titulo, autor, ano, genero, disponivel) VALUES 
(1, 'Devoradores de Mortos', 'Paul Lin', 2018, 'Terror', TRUE),
(2, 'Haunted Highway', 'Ellen Robson', 2021, 'Scify', TRUE),
(3, 'O Código Secreto', 'Ricardo Levi', 1935, 'Mistério', FALSE),
(4, 'Fogo na Torre', 'Antonio Castro', 2015, 'Aventura', TRUE),
(5, 'Memórias Esquecidas', 'Jose Henrique', 2023, 'Drama', FALSE);

-- Passo 3: Selecionar todos os livros disponíveis
SELECT * FROM Livros WHERE disponivel = TRUE;

-- Passo 4: Atualizar a disponibilidade de 1 livro
UPDATE Livros SET disponivel = TRUE WHERE id = 3;

-- Passo 5: Listar os livros do mais recente para o mais antigo
SELECT * FROM Livros ORDER BY ano DESC;

-- Passo 6: Deletar um livro com ano anterior a 1940
DELETE FROM Livros WHERE ano < 1940;

-- Passo 7: Apagar e recriar a tabela Livros
DROP TABLE Livros;

CREATE TABLE Livros (
    id INT PRIMARY KEY,
    titulo VARCHAR(100),
    autor VARCHAR(100),
    ano INT,
    genero VARCHAR(50),
    disponivel BOOLEAN
);