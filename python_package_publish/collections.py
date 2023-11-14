from collections.abc import Generator


def chunk(data: list, size: int) -> Generator[list, None, None]:
    for i in range(0, len(data), size):
        yield data[i : i + size]
