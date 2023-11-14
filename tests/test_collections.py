from python_package_publish.collections import chunk


def test_chunk() -> None:
    data = [1, 2, 3, 4, 5, 6, 7, 8]

    result = list(chunk(data, 3))

    assert result == [[1, 2, 3], [4, 5, 6], [7, 8]]
