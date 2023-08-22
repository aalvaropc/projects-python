import os
from pathlib import Path
from PIL import Image

def compress_image(image_path, target_path, qlt=50):
    """
    Comprime una imagen utilizando Pillow.

    Parameters:
        image_path (str): Ruta de la imagen original.
        target_path (str): Ruta de la imagen comprimida.
        quality (int, optional): Calidad de la compresión (0-100).

    Returns:
        None
    """

    path = Path(image_path)
    if not path.exists() or not path.is_dir():
        raise ValueError(f"{image_path} no es una ruta válida")

    target_path = Path(target_path)
    if not target_path.exists() or not target_path.is_dir():
        raise ValueError(f"{target_path} no es una ruta válida")

    for imagen in os.listdir(image_path):

        name, extesion = os.path.splitext(image_path + imagen)

        if extesion in [".jpg", ".png", "jpeg", "png"]:
            picture = Image.open(image_path + imagen)
            picture.save(image_path + "comp_" + imagen, optimize=True, quality=qlt)

if __name__ == "__main__":
    PATH = "/Users/ALVARO/Desktop/Proyectos/Automatización/downloads/"
    compress_image(PATH, PATH, 60)