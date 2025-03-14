# Aplicativo de Gerenciamento de Finanças Pessoais

Este é um aplicativo simples para gerenciamento de finanças pessoais, desenvolvido em Python. Ele permite que os usuários cadastrem receitas e despesas, categorizem transações, visualizem relatórios e gráficos de gastos, e exportem os dados para um arquivo Excel. O aplicativo utiliza as seguintes tecnologias:

- **Python**: Linguagem de programação principal.
- **Tkinter**: Biblioteca para criação da interface gráfica.
- **SQLite**: Banco de dados embutido para armazenamento das transações.
- **Matplotlib**: Biblioteca para geração de gráficos.
- **Pandas**: Biblioteca para exportação de dados para Excel.

---

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

### 4. Exportação para Excel
O usuário pode exportar todas as transações para um arquivo Excel (`relatorio_financeiro.xlsx`), permitindo análise externa ou compartilhamento.

### 5. Planejamento de Orçamento
Embora não implementado diretamente, o código pode ser estendido para incluir funcionalidades de planejamento de orçamento, como definir limites de gastos por categoria e receber alertas quando esses limites forem excedidos.

---

## Estrutura do Projeto

O projeto é organizado em quatro arquivos principais:

1. **`database.py`**: Responsável por criar e gerenciar o banco de dados SQLite. Ele contém funções para criar a tabela de transações, inserir novas transações e buscar transações existentes.

2. **`gui.py`**: Contém a interface gráfica do aplicativo, desenvolvida com Tkinter. A interface permite ao usuário adicionar transações, gerar relatórios e exportar dados para Excel.

3. **`reports.py`**: Gera relatórios e gráficos usando Matplotlib. Também inclui a funcionalidade de exportação de dados para Excel usando Pandas.

4. **`main.py`**: Arquivo principal que inicia a aplicação.

---

## Como Executar

1. **Instale as dependências**:
   Certifique-se de ter Python instalado. Em seguida, instale as bibliotecas necessárias:
   ```bash
   pip install matplotlib pandas
   ```

2. **Execute o aplicativo**:
   No terminal, navegue até o diretório do projeto e execute:
   ```bash
   python main.py
   ```

3. **Use o aplicativo**:
   - Adicione transações informando o tipo, categoria, valor e data.
   - Clique em "Gerar Relatório" para visualizar o gráfico de gastos por categoria.
   - Clique em "Exportar para Excel" para salvar as transações em um arquivo Excel.

---

## Exemplo de Uso

1. **Adicionar uma Transação**:
   - Tipo: `Despesa`
   - Categoria: `Alimentação`
   - Valor: `100.00`
   - Data: `2023-10-01`

2. **Gerar Relatório**:
   - Clique no botão "Gerar Relatório" para visualizar um gráfico de pizza mostrando a distribuição dos gastos por categoria.

3. **Exportar para Excel**:
   - Clique no botão "Exportar para Excel" para salvar todas as transações em um arquivo Excel (`relatorio_financeiro.xlsx`).

---

## Exemplo de Saída no Excel

O arquivo Excel gerado terá a seguinte estrutura:

| ID  | Tipo     | Categoria   | Valor | Data       |
|-----|----------|-------------|-------|------------|
| 1   | Despesa  | Alimentação | 100.0 | 2023-10-01 |
| 2   | Receita  | Salário     | 3000.0| 2023-10-05 |
| 3   | Despesa  | Transporte  | 50.0  | 2023-10-06 |

---

## Contribuição

Sinta-se à vontade para contribuir com melhorias, correções ou novas funcionalidades. Basta fazer um fork do repositório, implementar suas alterações e abrir um pull request.

---
