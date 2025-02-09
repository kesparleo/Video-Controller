import os
import subprocess

def find_video(video_name, search_path="D:\\"):
    """Procura um vídeo pelo nome em todas as pastas do disco D:"""
    for root, _, files in os.walk(search_path):
        for file in files:
            if video_name.lower() in file.lower():
                return os.path.join(root, file)
    return None

def open_vlc(video_path, speed=1.5):
    """Abre o VLC com o vídeo na velocidade desejada."""
    vlc_path = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"  # Ajuste se necessário
    subprocess.run([vlc_path, "--rate", str(speed), video_path])

if __name__ == "__main__":
    video_name = input("Digite o nome do vídeo: ")
    video_path = find_video(video_name)
    
    if video_path:
        print(f"Abrindo: {video_path}")
        open_vlc(video_path, speed=1.5)  # Altere a velocidade aqui se quiser
    else:
        print("Vídeo não encontrado.")
