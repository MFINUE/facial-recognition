class PathDoesNotExistError(Exception):

    def __init__(self, path) -> None:
        self.path = path
        self.message = f"\"{path}\" is not a valid path."
        super().__init__(self.message)
    