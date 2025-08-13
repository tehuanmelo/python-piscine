def ft_tqdm(lst: range) -> None:
    """
    Custom implementation of a progress bar generator, similar to tqdm.

    Args:
        lst (range): The range or iterable to wrap and iterate through.

    Yields:
        int: Each item from the provided iterable, one at a time.

    Displays:
        A progress bar showing the percentage completed, a dynamic visual bar,
        and the current iteration count out of total.
    """
    try:
        total = len(lst)
        if total < 1:
            print("0it")
            return
        width = 50
        for i in range(total):
            percentage = int((i + 1) / total * 100)
            dashes = int(percentage / 100 * width)
            bar = "=" * dashes
            if dashes < width:
                bar += ">"
            print(f"{percentage:>3}%|[{bar:<{width}}]| {i+1}/{total}",
                  end="\r")
            yield i
        print()
    except Exception as e:
        print(f"Error: {e}")


def main():
    """
    Entry point of the program.
    """
    pass


if __name__ == "__main__":
    main()
