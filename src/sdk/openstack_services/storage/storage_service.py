from openstack.connection import Connection

from ._backend_pools import BackendPools
from ._backups import Backups
from ._services import Services
from ._snapshots import Snapshots
from ._volumes import Volumes


class StorageService:
    """The block storage service (Cinder)"""
    
    def __init__(self, conn: Connection):
        sdk_conn = conn

        self.backend_pools = BackendPools(sdk_conn)
        self.backups = Backups(sdk_conn)
        self.services = Services(sdk_conn)
        self.snapshots = Snapshots(sdk_conn)
        self.volumes = Volumes(sdk_conn)
