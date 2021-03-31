class FileOperations:
    def __int__(self, filepath):
        self._filepath = filepath


class FileWrite(FileOperations):
    def __int__(self, filepath):
        super().__int__(filepath)


class FileRead(FileOperations):
    def __int__(self, filepath):
        super().__int__(filepath)
