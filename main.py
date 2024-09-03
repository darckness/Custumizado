import customtkinter as ctk
import tkinter as tk
from screen.config import open_new_window

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Janela principal
root = ctk.CTk()
root.title("LinuxNetMaster")
root.geometry("1020x480")
root.configure(bg='#b3e9f3')

# Não deixa redimensionar a tela
root.resizable(False, False)

# Função para criar um card individual com entrada de dados
def create_card(parent, title, mac, status, fw_version):
    card = ctk.CTkFrame(parent, width=150, height=200, fg_color="#00bcd4", corner_radius=15)
    
    title_label = ctk.CTkLabel(card, text=title, font=("Arial", 12), width=150, height=30, fg_color="white", corner_radius=15)
    title_label.pack(pady=12)
    title_label.pack(padx=14)
    
    # Entradas de dados
    mac_entry = ctk.CTkEntry(card, placeholder_text=mac)
    mac_entry.pack(pady=5)
    
    status_label = ctk.CTkLabel(card, text=f"Status da associação\n{status}", font=("Arial", 12), text_color="black", justify="center")
    status_label.pack(pady=5)
    
    fw_label = ctk.CTkLabel(card, text=f"Versão de FW\n{fw_version}", font=("Arial", 12), text_color="black", justify="center")
    fw_label.pack(pady=5)

    return card, mac_entry

# Container para os cards
container = ctk.CTkFrame(root, fg_color="#b3e9f3")
container.pack(pady=20)

# Criando e posicionando os cards individualmente
entries = []
cards = []

for i in range(10):
    card, entry = create_card(container, f"Produto {i+1}", "MAC", "Confirmado", "1.25.5")
    entries.append(entry)
    cards.append(card)
    row, col = divmod(i, 5)
    card.grid(row=row, column=col, padx=10, pady=10)

# Função para tratar os dados inseridos
def handle_data():
    for i, entry in enumerate(entries):
        print(f"Card {i+1} - MAC: {entry.get()}")

button_frame = ctk.CTkFrame(root, fg_color="#b3e9f3")
button_frame.pack(pady=10)

# Botão para tratar os dados
buttonStart = ctk.CTkButton(button_frame, text="Tratar Dados", command=handle_data)
buttonStart.pack(side="left", padx=10)

# Botão de configuração
buttonConfig = ctk.CTkButton(button_frame, text="Config", command=open_new_window)
buttonConfig.pack(side="left", padx=10)

# Rodar a aplicação
root.mainloop()
