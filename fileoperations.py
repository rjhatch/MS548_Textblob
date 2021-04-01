import os


class FileOperations:
    def __init__(self, filepath):
        self._filepath = filepath

    def file_exists(self):
        return os.path.isfile(self._filepath)


class FileWrite(FileOperations):
    def __init__(self, filepath):
        super().__init__(filepath)

    def file_append(self, statement):
        try:
            txt_file = open(self._filepath, "a")
            txt_file.write(statement)
        finally:
            txt_file.close


class FileRead(FileOperations):
    def __init__(self, filepath):
        super().__init__(filepath)

    def file_read(self):
        try:
            txt_file = open(self._filepath, "r")
            return txt_file.read()
        finally:
            txt_file.close()