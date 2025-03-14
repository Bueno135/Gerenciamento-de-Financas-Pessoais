# Aplicativo de Gerenciamento de Finanças Pessoais

Este é um aplicativo simples para gerenciamento de finanças pessoais, desenvolvido em Python. Ele permite que os usuários cadastrem receitas e despesas, categorizem transações e visualizem relatórios e gráficos de gastos. O aplicativo utiliza as seguintes tecnologias:

- **Python**: Linguagem de programação principal.
- **Tkinter**: Biblioteca para criação da interface gráfica.
- **SQLite**: Banco de dados embutido para armazenamento das transações.
- **Matplotlib**: Biblioteca para geração de gráficos.

## Funcionalidades

### 1. Cadastro de Receitas e Despesas
O usuário pode adicionar transações informando:
- **Tipo**: Receita ou Despesa.
- **Categoria**: Categoria da transação (ex: Alimentação, Transporte, Lazer).
- **Valor**: Valor da transação.
- **Data**: Data da transação no formato `YYYY-MM-DD`.

### 2. Categorização de Transações
As transações são armazenadas no banco de dados com suas respectivas categorias, permitindo uma análise detalhada dos gastos.

### 3. Relatórios e Gráficos de Gastos
O aplicativo gera um gráfico de pizza que mostra a distribuição dos gastos por categoria. Isso ajuda o usuário a visualizar onde está gastando mais.

### 4. Planejamento de Orçamento
Embora não implementado diretamente, o código pode ser estendido para incluir funcionalidades de planejamento de orçamento, como definir limites de gastos por categoria e receber alertas quando esses limites forem excedidos.

## Estrutura do Projeto

O projeto é organizado em quatro arquivos principais:

1. **`database.py`**: Responsável por criar e gerenciar o banco de dados SQLite. Ele contém funções para criar a tabela de transações, inserir novas transações e buscar transações existentes.

2. **`gui.py`**: Contém a interface gráfica do aplicativo, desenvolvida com Tkinter. A interface permite ao usuário adicionar transações e gerar relatórios.

3. **`reports.py`**: Gera relatórios e gráficos usando Matplotlib. Atualmente, ele cria um gráfico de pizza que mostra a distribuição dos gastos por categoria.

4. **`main.py`**: Arquivo principal que inicia a aplicação.

## Como Executar

1. **Instale as dependências**:
   Certifique-se de ter Python instalado. Em seguida, instale a biblioteca Matplotlib:
   ```bash
   pip install matplotlib
   ```

2. **Execute o aplicativo**:
   No terminal, navegue até o diretório do projeto e execute:
   ```bash
   python main.py
   ```

3. **Use o aplicativo**:
   - Adicione transações informando o tipo, categoria, valor e data.
   - Clique em "Gerar Relatório" para visualizar o gráfico de gastos por categoria.

## Exemplo de Uso

1. **Adicionar uma Transação**:
   - Tipo: `Despesa`
   - Categoria: `Alimentação`
   - Valor: `100.00`
   - Data: `2023-10-01`

2. **Gerar Relatório**:
   - Clique no botão "Gerar Relatório" para visualizar um gráfico de pizza mostrando a distribuição dos gastos por categoria.


