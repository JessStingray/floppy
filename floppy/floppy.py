import io

class Floppy:
    """
    Base class for a floppy image.

    Attributes:
        capacity - Capacity in kilobytes.
        size - Physcial size, e.g. 3.5 or 5.25. Could extend to 8
                inches in future, but it's incredibly unlikely I'm
                going to get hold of one of those for testing so it'd
                be "unsafe".
        bytes_per_sector - Probably 512.
    """

    def __init__(self, size=3.5, capacity=1440):
        """
        Base floppy image.
        """

        if size == 3.5:
            # Check capacity is sane first
            if capacity not in [360, 720, 1440]:
                raise ValueError("Invalid size for 3.5 inch disks")
        else:
            raise ValueError("Invalid size for floppy image - only 3.5 inch is supported for now")

        if size == 3.5 and capacity != 1440:
            raise NotImplementedError()

        self.size = size
        self.capacity = capacity * 1024 # Bytes rather than KB
        self.bytes_per_sector = 512
        self._data = bytearray(self.capacity) # Files will live here
        self.filesystem = None

    def open(self, file):
        self._data = bytearray(file.read())
        self.filesystem = self.detect_filesystem()

    def read(self, offset, length):
        return self._data[offset:offset + length]
