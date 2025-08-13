from load_image import ft_load
import numpy as np


def zoom(path: str) -> list:
    """"Zoom in a given image"""
    arr = ft_load(path)
    print(arr)
    new_arr = arr[0:400, 400:800]
    gray = np.dot(new_arr[..., :3], [-0.07474739, -3.05366278,  3.89713981])
    gray_wrapped = gray[..., np.newaxis]

    print(f"New shape after slicing: {gray_wrapped.shape} or {gray.shape}")
    print(gray_wrapped)
    

def main():
    """Entry point of the program"""
    zoom("../animal.jpeg")


if __name__ == "__main__":
    main()