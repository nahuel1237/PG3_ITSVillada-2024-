
from pytube import YouTube

def show_menu():
    print("1. Descargar video")
    print("2. Obtener información del video")
    print("3. Listar corrientes disponibles")
    print("4. Descargar corriente específica")
    print("5. Salir")

def download_video(url):
    yt = YouTube(url)
    yt.streams.first().download()
    print("Video descargado exitosamente!")

def get_video_info(url):
    yt = YouTube(url)
    print("Título:", yt.title)
    print("Autor:", yt.author)
    print("Duración:", yt.length, "segundos")
    print("Vistas:", yt.views)
    print("Calificación:", yt.rating)

def list_streams(url):
    yt = YouTube(url)
    print("Corrientes disponibles:")
    for stream in yt.streams.all():
        print(stream)
def download_specific_stream(url, itag):
    yt = YouTube(url)
    stream = yt.streams.get_by_itag(itag)
    stream.download()
    print("Corriente descargada exitosamente!")

while True:
    show_menu()
    choice = input("Ingrese el número de la opción que desee: ")
 
    if choice == '1':
        url = input("Ingrese la URL del video de YouTube: ")
        download_video(url)
    elif choice == '2':
        url = input("Ingrese la URL del video de YouTube: ")
        get_video_info(url)
    elif choice == '3':
        url = input("Ingrese la URL del video de YouTube: ")
        list_streams(url)
    elif choice == '4':
        url = input("Ingrese la URL del video de YouTube: ")
        itag = input("Ingrese el itag de la corriente que desea descargar: ")
        download_specific_stream(url, itag)
    elif choice == '5':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número válido.")


