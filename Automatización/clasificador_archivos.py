import os
import shutil

def classify_files(src_folder, dst_folder_images, dst_folder_videos):
    """
    Clasifica los archivos de la carpeta src_folder en las carpetas dst_folder_images y dst_folder_videos
    según su extensión.

    Parameters:
        src_folder (str): Ruta de la carpeta de origen.
        dst_folder_images (str): Ruta de la carpeta de destino para imágenes.
        dst_folder_videos (str): Ruta de la carpeta de destino para videos.

    Returns:
        None
    """
    if not os.path.isdir(src_folder):
        raise ValueError(f"{src_folder} no es una ruta válida")

    if not os.path.isdir(dst_folder_images):
        os.makedirs(dst_folder_images)

    if not os.path.isdir(dst_folder_videos):
        os.makedirs(dst_folder_videos)

    for filename in os.listdir(src_folder):
        src_file = os.path.join(src_folder, filename)
        if os.path.isfile(src_file):
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
                dst_file = os.path.join(dst_folder_images, filename)
                shutil.move(src_file, dst_file)
            elif filename.endswith(".mp4") or filename.endswith(".avi") or filename.endswith(".mkv"):
                dst_file = os.path.join(dst_folder_videos, filename)
                shutil.move(src_file, dst_file)

if __name__ == "__main__":
    SRC_FOLDER = "/Users/ALVARO/Desktop/Proyectos/Automatización/downloads/"
    DST_FOLDER_IMAGES = "/Users/ALVARO/Desktop/Proyectos/Automatización/img/"
    DST_FOLDER_VIDEOS = "/Users/ALVARO/Desktop/Proyectos/Automatización/videos/"
    
    classify_files(SRC_FOLDER, DST_FOLDER_IMAGES, DST_FOLDER_VIDEOS)
