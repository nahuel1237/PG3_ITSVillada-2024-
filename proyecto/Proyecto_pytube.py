import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QInputDialog, QLabel, QLineEdit
from pytube import YouTube
import os


# Función para descargar el video
def download_video(url):
    yt = YouTube(url)
    yt.streams.first().download()
    return f"Video descargado exitosamente: {yt.title}"

# Función para obtener información del video
def get_video_info(url):
    yt = YouTube(url)
    return f"Título: {yt.title}\nAutor: {yt.author}\nDuración: {yt.length} segundos\nVistas: {yt.views}\nCalificación: {yt.rating}"

# Función para listar las corrientes disponibles
def list_streams(url):
    yt = YouTube(url)
    streams_info = "\n".join([str(stream) for stream in yt.streams.all()])
    return f"Corrientes disponibles:\n{streams_info}"

# Función para descargar una corriente específica por su itag
def download_specific_stream(url, itag):
    yt = YouTube(url)
    stream = yt.streams.get_by_itag(itag)
    stream.download()
    return "Corriente descargada exitosamente!"

# Función para descargar solo el audio
def download_audio(url):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    if audio_stream:
        audio_filename = "audio.mp4"
        audio_stream.download(filename=audio_filename)

        # Renombrar el archivo de audio a .mp3
        os.rename(audio_filename, "audio.mp3")

        return "Audio descargado exitosamente en formato MP3!"
    else:
        return "No se encontró ninguna corriente de audio disponible para este video."

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouTube Downloader")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.url_input = QLineEdit()
        layout.addWidget(self.url_input)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.btn_download = QPushButton("Descargar video")
        self.btn_download.clicked.connect(self.download_video)
        layout.addWidget(self.btn_download)

        self.btn_download_audio = QPushButton("Descargar solo audio")
        self.btn_download_audio.clicked.connect(self.download_audio)
        layout.addWidget(self.btn_download_audio)

        self.btn_info = QPushButton("Obtener información del video")
        self.btn_info.clicked.connect(self.get_video_info)
        layout.addWidget(self.btn_info)

        self.btn_list_streams = QPushButton("Listar corrientes disponibles")
        self.btn_list_streams.clicked.connect(self.list_streams)
        layout.addWidget(self.btn_list_streams)

        self.btn_download_specific = QPushButton("Descargar corriente específica")
        self.btn_download_specific.clicked.connect(self.download_specific_stream)
        layout.addWidget(self.btn_download_specific)

        self.btn_set_url = QPushButton("Establecer URL")
        self.btn_set_url.clicked.connect(self.set_url)
        layout.addWidget(self.btn_set_url)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.url = ""

    def download_video(self):
        url = self.url_input.text()
        if url:
            result = download_video(url)
            self.result_label.setText(result)
        else:
            self.result_label.setText("Por favor, ingrese una URL válida.")

    def download_audio(self):
        url = self.url_input.text()
        if url:
            result = download_audio(url)
            self.result_label.setText(result)
        else:
            self.result_label.setText("Por favor, ingrese una URL válida.")

    def get_video_info(self):
        url = self.url_input.text()
        if url:
            result = get_video_info(url)
            self.result_label.setText(result)
        else:
            self.result_label.setText("Por favor, ingrese una URL válida.")

    def list_streams(self):
        url = self.url_input.text()
        if url:
            result = list_streams(url)
            self.result_label.setText(result)
        else:
            self.result_label.setText("Por favor, ingrese una URL válida.")

    def download_specific_stream(self):
        url = self.url_input.text()
        itag, _ = QInputDialog.getText(self, "Ingrese el itag", "Itag de la corriente que desea descargar:")
        if url and itag:
            result = download_specific_stream(url, itag)
            self.result_label.setText(result)
        else:
            self.result_label.setText("Por favor, ingrese una URL válida.")

    def set_url(self):
        url, _ = QInputDialog.getText(self, "Ingrese la URL", "URL del video de YouTube:")
        if url:
            self.url = url
            self.url_input.setText(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())