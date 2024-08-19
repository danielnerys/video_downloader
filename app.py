import tkinter as tk
from tkinter import filedialog, messagebox

import yt_dlp


# Função para baixar o vídeo
def download_video():
    url = url_entry.get()
    save_path = path_entry.get()

    if url and save_path:
        ydl_opts = {
            "format": "best",  # Baixa na melhor qualidade disponível
            "outtmpl": save_path
            + "/%(title)s.%(ext)s",  # Salva o vídeo na pasta escolhida
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            messagebox.showinfo("Sucesso", "Download concluído!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
    else:
        messagebox.showwarning(
            "Atenção", "Por favor, insira um URL válido e escolha uma pasta."
        )


# Função para escolher a pasta de destino
def choose_directory():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, folder_selected)


# Configuração da janela principal
root = tk.Tk()
root.title("YouTube Video Downloader")

# URL Label e Entry
url_label = tk.Label(root, text="URL do Vídeo:")
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Path Label, Entry e Button
path_label = tk.Label(root, text="Salvar em:")
path_label.pack(pady=5)

path_entry = tk.Entry(root, width=50)
path_entry.pack(pady=5)

browse_button = tk.Button(root, text="Escolher Pasta", command=choose_directory)
browse_button.pack(pady=5)

# Botão de download
download_button = tk.Button(root, text="Baixar Vídeo", command=download_video)
download_button.pack(pady=20)

# Iniciar o loop da interface
root.mainloop()
