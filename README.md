# 📚 Biblioteca Pessoal - API Documentation

## 🚀 Visão Geral
A Biblioteca Pessoal API é uma aplicação Flask para gerenciamento de livros pessoais com autenticação JWT, banco de dados TinyDB.

ROTAS DISPONÍVEIS NO SISTEMA
🔐 Autenticação
1.	POST /api/auth/register - Registrar novo usuário
2.	POST /api/auth/login - Fazer login
📚 Gerenciamento de Livros (requer autenticação)
3.	POST /api/books - Adicionar livro
4.	GET /api/books - Listar livros do usuário
5.	GET /api/books/search?q=termo - Buscar livros
