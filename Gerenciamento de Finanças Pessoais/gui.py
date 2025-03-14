import tkinter as tk
from tkinter import messagebox
from database import create_connection, insert_transaction, fetch_transactions
from reports import generate_report

class FinanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Finanças Pessoais")

        self.conn = create_connection("finance.db")

        self.type_label = tk.Label(root, text="Tipo (Receita/Despesa):")
        self.type_label.grid(row=0, column=0)
        self.type_entry = tk.Entry(root)
        self.type_entry.grid(row=0, column=1)

        self.category_label = tk.Label(root, text="Categoria:")
        self.category_label.grid(row=1, column=0)
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=1, column=1)

        self.amount_label = tk.Label(root, text="Valor:")
        self.amount_label.grid(row=2, column=0)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=2, column=1)

        self.date_label = tk.Label(root, text="Data (YYYY-MM-DD):")
        self.date_label.grid(row=3, column=0)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=3, column=1)

        self.add_button = tk.Button(root, text="Adicionar Transação", command=self.add_transaction)
        self.add_button.grid(row=4, column=0, columnspan=2)

        self.report_button = tk.Button(root, text="Gerar Relatório", command=self.generate_report)
        self.report_button.grid(row=5, column=0, columnspan=2)

    def add_transaction(self):
        type_ = self.type_entry.get()
        category = self.category_entry.get()
        amount = self.amount_entry.get()
        date = self.date_entry.get()

        if type_ and category and amount and date:
            transaction = (type_, category, float(amount), date)
            insert_transaction(self.conn, transaction)
            messagebox.showinfo("Sucesso", "Transação adicionada com sucesso!")
        else:
            messagebox.showwarning("Erro", "Todos os campos são obrigatórios!")

    def generate_report(self):
        transactions = fetch_transactions(self.conn)
        generate_report(transactions)

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceApp(root)
    root.mainloop()