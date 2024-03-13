import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Snapshots:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch snapshots")
        return self.sdk_conn.block_storage.snapshots()

    
    def show(self, snapshot_id):
        if not snapshot_id:
            raise AttributeError("Required attribute 'snapshot_id' was not defined")

        LOG.debug(f"Trying to find '{snapshot_id}' snapshot")
        return self.sdk_conn.block_storage.find_snapshot(snapshot_id)


    def show_metadata(self, snapshot_id):
        if not snapshot_id:
            raise AttributeError("Required attribute 'snapshot_id' was not defined")

        LOG.debug(f"Trying to find '{snapshot_id}' snapshot's metadata")
        return self.sdk_conn.block_storage.get_snapshot_metadata(snapshot_id)
