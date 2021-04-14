

class DB:
    _instance = None

    @staticmethod
    def get_instance():
        if DB._instance is None:
            raise RuntimeError(f"You must initialize the {__class__} singleton first.")
        return DB._instance

    def __init__(self):
        # Set _instance at the end of this method
        DB._instance = self

    def close(self):
        pass  # Clean methods (db connection)
