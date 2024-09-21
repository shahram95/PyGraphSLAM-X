"""Something simple.

"""


class Simple(object):
    """A simple class

    """
    def __init__(self):
        self.data = 5

    def get_data(self):
        """Return ``self.data``.

        Returns
        -------
        int
            the current value of ``self.data``

        """
        return self.data

    def set_data(self, data):
        """Set ``self.data`` to ``data``.

        Parameters
        -------
        data : int
            the value that will be assigned to ``self.data``

        """
        self.data = data


def create_simple():
    """Create an instance of the `Simple` class."""
    return Simple()
