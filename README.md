# PONDERADA-S7-M6

# Construção de uma API com Integração para Geração de Histórias

Este projeto consiste na implementação de uma API para a gestão de histórias, integrada à API do ChatGPT para geração de conteúdo textual. Abaixo estão os detalhes sobre cada aspecto do projeto de acordo com o barema proposto:

## 1. CRUD de Histórias

A aplicação fornece operações CRUD (Create, Read, Update, Delete) para gerenciar histórias. As histórias são representadas por um modelo que inclui campos como ID e Conteúdo. As operações permitem a criação, recuperação, atualização e exclusão de histórias.

## 2. Integração com a API do ChatGPT

A API integra-se à API do ChatGPT para gerar histórias de forma dinâmica. A função `create_historia_from_gpt` utiliza a API do ChatGPT para gerar automaticamente o conteúdo de uma história.

## 3. Testes

### a. Testes Unitários
Foram implementados testes unitários para todas as funcionalidades do CRUD de histórias e usuários. Cada função importante da aplicação é testada para garantir seu comportamento esperado.

Create Historia: cria uma história
![createhistoria](https://github.com/emoly10022/PONDERADA-S7-M6/assets/110625232/4d791129-8f11-4573-95c5-6d70a0d19e73)

Get Historia: seleciona uma história por ID
![gethistoria](https://github.com/emoly10022/PONDERADA-S7-M6/assets/110625232/0f9bf7ef-0aa0-4bd1-b199-732b52f9b78b)

Get Histórias: Lista todas as histórias
![gethistorias](https://github.com/emoly10022/PONDERADA-S7-M6/assets/110625232/d2951dd0-51a5-4622-a60f-43d71913cba3)

Delete História: deleta uma história pelo ID
![deletehistorias](https://github.com/emoly10022/PONDERADA-S7-M6/assets/110625232/4a838ce0-8793-4be4-84b3-a28ce4e5cc71)

Update História: atualiza histórias 
![updatehistorias](https://github.com/emoly10022/PONDERADA-S7-M6/assets/110625232/8a600f2f-f65a-4ad2-a96d-4b9e7e42c2bd)

Testes funcionando:
![testhistoria](https://github.com/emoly10022/PONDERADA-S7-M6/assets/110625232/eefde818-d054-484f-88c1-45111d25aeba)
