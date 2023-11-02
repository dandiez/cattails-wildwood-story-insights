class UndefinedObj:
    """object to be used as a placeholder when None is a valid value."""

    def __repr__(self):
        return "<undefined>"


Undefined = UndefinedObj()


