from openstack.connection import Connection

from ._backend_pools import BackendPools
from ._backups import Backups
from ._services import Services
from ._snapshots import Snapshots
from ._volumes import Volumes


class StorageService:
    """The block storage service (Cinder)"""

    def __init__(self, conn: Connection):
        self.backend_pools = BackendPools(conn)
        self.backups = Backups(conn)
        self.services = Services(conn)
        self.snapshots = Snapshots(conn)
        self.volumes = Volumes(conn)
