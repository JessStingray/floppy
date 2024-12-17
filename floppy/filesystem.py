import enum
import struct

class Filesystem(enum.Enum):
    FAT12   = 1
    FAT16   = 2 # Rare, but has happened
    CPM     = 3 # CP/M Filesystem
    UFS     = 4 # Apparently used by Sun?
    HFS     = 5 # Used by Macs. Unsupported until I can get my hands on one.
    AMIGA   = 6 # Also known as FFS.


class FAT12:
    def __init__(self, image):
        self._image = image
        self._read_filesystem()

    def _read_filesystem(self):
        self._read_bios_param_block()
        self._read_fat()
        self._read_disk_label()
        self._chdir_root()

    def read_bios_param_block(self):
        image = self._image
        # Check MBR first.
        mbr = self.read_sector(0)
        (
            bytes_per_sector,       # Most common is 512.
            sectors_per_cluster,    # Allowed values are 1-128, powers of 2.
            fat_start_sector,       # Technically, reserved logical sectors. Count before first FAT
            fat_count,              # Number of FATs.
            root_entries,           # Max root directory entries. Should be multiple of 16
            logical_sectors,        # Total logical sectors.
            descriptor,             # Media descriptor. Check Wikipedia for details
            sectors_per_fat,        # Logical sectors per FAT.
        ) = struct.unpack("<HBHBHHBH", mbr[0x0B:0x18])
        # H = unsigned short, B = unsigned char. Noting because I always bloody forget.


    def _read_fat(self):
        # TODO

    def _ref_disk_label(self):
        # TODO

    def _chdir_root(self):
        self._dir_cluster, self._dir_parents = 1, []

    def read(self, offset, length):
        return self._image.read(offset, length)

    def read_sector(self, sector_num):
        """ Reads 512-byte sector
        """
        return self.read(sector_num, 512)

