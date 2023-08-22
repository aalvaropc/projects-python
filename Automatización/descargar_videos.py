import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube

class DownloadYoutubeVideoGUI:
    def __init__(self, root):
        self.root = root
        root.title("Descarga videos de YouTube")

        # Crear widgets
        self.url_label = Label(root, text="URL del video:")
        self.url_entry = Entry(root)
        self.format_label = Label(root, text="Formato:")
        self.format_var = StringVar(root)
        self.format_option = OptionMenu(root, self.format_var, "mp4", "webm", "flv")
        self.resolution_label = Label(root, text="Resolución:")
        self.resolution_var = StringVar(root)
        self.resolution_option = OptionMenu(root, self.resolution_var, "240p", "360p", "480p", "720p", "1080p")
        self.folder_label = Label(root, text="Carpeta de destino:")
        self.folder_entry = Entry(root)
        self.folder_button = Button(root, text="Seleccionar carpeta", command=self.select_folder)
        self.download_button = Button(root, text="Descargar", command=self.download_video)

        # Colocar widgets
        self.url_label.grid(row=0, column=0, padx=5, pady=5)
        self.url_entry.grid(row=0, column=1, padx=5, pady=5, columnspan=2)
        self.format_label.grid(row=1, column=0, padx=5, pady=5)
        self.format_option.grid(row=1, column=1, padx=5, pady=5)
        self.resolution_label.grid(row=1, column=2, padx=5, pady=5)
        self.resolution_option.grid(row=1, column=3, padx=5, pady=5)
        self.folder_label.grid(row=2, column=0, padx=5, pady=5)
        self.folder_entry.grid(row=2, column=1, padx=5, pady=5)
        self.folder_button.grid(row=2, column=2, padx=5, pady=5)
        self.download_button.grid(row=3, column=1, pady=5)
        
    def select_folder(self):
        folder_path = filedialog.askdirectory()
        self.folder_entry.delete(0, END)
        self.folder_entry.insert(0, folder_path)

    def download_video(self):
        video_url = self.url_entry.get()
        video_format = self.format_var.get()
        video_resolution = self.resolution_var.get()
        folder_path = self.folder_entry.get()

        if video_url == "":
            messagebox.showerror("Error", "Por favor, ingresa la URL del video")
            return
        if folder_path == "":
            messagebox.showerror("Error", "Por favor, selecciona la carpeta de destino")
            return

        try:
            yt = YouTube(video_url)
        except:
            messagebox.showerror("Error", "No se pudo descargar el video, verifica la URL")
            return

        video = yt.streams.filter(file_extension=video_format, resolution=video_resolution).first()

        if video is None:
            messagebox.showerror("Error", "No se encontró una versión disponible del video con esas especificaciones")
            return

        video.download(folder_path)
        messagebox.showinfo("Completo", "Video descargado exitosamente")
            
if __name__ == "__main__":
    root = Tk()
    app = DownloadYoutubeVideoGUI(root)
    root.mainloop()