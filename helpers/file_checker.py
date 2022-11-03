import pathlib


def file_exists(filename):
    """
    Возвращает True, если файл есть в запускаемой директории
    """
    return pathlib.Path(filename).exists()
