from utils import TaskStatus


class MenuItem:

    description = "No description set"

    def run(self) -> TaskStatus:
        raise NotImplementedError("'run' method is not implemented")
