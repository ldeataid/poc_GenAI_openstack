import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Snapshots:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch snapshots")
        response = self.sdk_conn.block_storage.snapshots()
        return json.dumps(list(response))


    def show(self, snapshot_id):
        if not snapshot_id:
            raise AttributeError("Required attribute 'snapshot_id' was not defined")

        LOG.debug(f"Trying to find '{snapshot_id}' snapshot")
        response = self.sdk_conn.block_storage.find_snapshot(snapshot_id)
        if response is None:
            raise Exception("Snapshot not found!")

        return json.dumps(response)


    def show_metadata(self, snapshot_id):
        if not snapshot_id:
            raise AttributeError("Required attribute 'snapshot_id' was not defined")

        LOG.debug(f"Trying to find '{snapshot_id}' snapshot's metadata")
        response = self.sdk_conn.block_storage.get_snapshot_metadata(snapshot_id)
        if response is None:
            raise Exception("Snapshot not found!")

        return json.dumps(response)
