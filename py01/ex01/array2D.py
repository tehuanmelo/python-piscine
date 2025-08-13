import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    slice_me takes as parameters a 2D array, prints its shape,
    and returns a list truncated version of the array based
    on the provided start and end arguments.
    If error returns None
    """
    try:
        int(start)
        int(end)
        if not family:
            raise ValueError("Array cant be empty")
        elif not isinstance(family, list):
            raise TypeError("Array passed must be a list")
        elif not all([isinstance(row, list) for row in family]):
            raise TypeError("All sub arrays must be a list")
        elif len({len(row) for row in family}) != 1:
            raise ValueError("Sub arrays must have the same length")
        
        rows = len(family)

        start_index = start if start >= 0 else abs(start)
        end_index = end if end >= 0 else rows + end
        
        if not (0 <= start_index <= rows):
            raise ValueError("Start index out of range")
        if not (0 <= end_index <= rows):
            raise ValueError("End index out of range")
        if start_index >= end_index:
            raise ValueError("Start must be less than end")
        
        arr = np.array(family)
        new_arr = arr[start_index:end_index, :]
        print(f"My shape is : {arr.shape}")
        print(f"My new shape is : {new_arr.shape}")
        return new_arr.tolist()
    
    except Exception as e:
        print(f"Error: {e}")

def main():
    """Entry point of the program"""
    
    family = [[1.80, 78.4],
                [2.15, 102.7],
                [2.10, 98.5],
                [1.88, 75.2]]
    
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()