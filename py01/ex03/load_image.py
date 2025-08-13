from PIL import Image
import numpy as np
import os


def check_path(path: str) -> bool:
    """
    check_path checks if the path is valid
    and if the extension is jpg or jpeg
    """
    if not os.path.exists(path):
        raise ValueError("File not found")
    elif not path.lower().endswith((".jpg", ".jpeg")):
        raise ValueError("File not supported")
    return True

def ft_load(path: str) -> list:
    """"
    ft_load loads an image, prints its format, and its pixels
    content in RGB format.
    Returns a <class 'numpy.ndarray'> with pixels as rgb
    """
    try:
        check_path(path)
        img = Image.open(path)
        img = img.convert("RGB")
        arr = np.array(img)
        print(f"The shape of image is: {arr.shape}")
        return arr
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Entry point of the program"""
    print(ft_load("../landscape.jpg"))


if __name__ == "__main__":
    main()
