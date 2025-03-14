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