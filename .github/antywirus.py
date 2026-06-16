import customtkinter as ctk
import subprocess
import sys
import os

# Ustawienia wyglądu
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("500x400")
app.title("Mój Antywirus 2026 - Security Shield")

def start_monitor():
    # Pobieramy ścieżkę do folderu z programem
    base_path = os.path.dirname(os.path.abspath(__file__))
    monitor_path = os.path.join(base_path, "monitor.py")
    
    # Uruchamiamy monitor w tle
    subprocess.Popen([sys.executable, monitor_path])
    status_label.configure(text="STATUS: OCHRONA AKTYWNA", text_color="#2CC985")
    log_textbox.insert("0.0", ">>> System monitorowania uruchomiony...\n")

# Funkcja do sprawdzania logów w czasie rzeczywistym
def check_logs():
    if os.path.exists("log.txt"):
        with open("log.txt", "r") as f:
            content = f.read()
            log_textbox.delete("0.0", "end")
            log_textbox.insert("0.0", content)
    app.after(1000, check_logs)

# Layout UI
header = ctk.CTkLabel(app, text="SYSTEM ZABEZPIECZEŃ", font=("Segoe UI", 24, "bold"))
header.pack(pady=20)

status_label = ctk.CTkLabel(app, text="STATUS: CZEKA NA START", font=("Segoe UI", 14), text_color="gray")
status_label.pack(pady=5)

# Pole logów
log_textbox = ctk.CTkTextbox(app, width=400, height=150)
log_textbox.pack(pady=20)

btn = ctk.CTkButton(app, text="URUCHOM OCHRONĘ", font=("Segoe UI", 12, "bold"), command=start_monitor)
btn.pack(pady=10)

# Uruchamiamy sprawdzanie logów
check_logs()

app.mainloop()
