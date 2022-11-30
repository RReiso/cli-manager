class MenuItem:

    @classmethod
    def description(cls):
        raise NotImplementedError("'description' method is not implemented")

    def run(self):
        raise NotImplementedError("'run' method is not implemented")
