import pandas as pd
import matplotlib.pyplot as plt

def generate_report(transactions):
    categories = {}
    for transaction in transactions:
        category = transaction[2]
        amount = transaction[3]
        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    labels = categories.keys()
    sizes = categories.values()

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Distribuição de Gastos por Categoria")
    plt.show()

def export_to_excel(transactions, filename="relatorio_financeiro.xlsx"):
    try:
        # Verifica se há transações para exportar
        if not transactions:
            print("Nenhuma transação encontrada para exportar.")
            return False

        # Cria um DataFrame a partir da lista de transações
        df = pd.DataFrame(transactions, columns=["ID", "Tipo", "Categoria", "Valor", "Data"])
        
        # Exporta o DataFrame para um arquivo Excel
        df.to_excel(filename, index=False)
        print(f"Relatório exportado para {filename}")
        return True
    except Exception as e:
        print(f"Erro ao exportar para Excel: {e}")
        return False