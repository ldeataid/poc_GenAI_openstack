import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Snapshots:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch snapshots")
        all_projects = True if self.sdk_conn.auth["username"] == "admin" else False
        response = self.sdk_conn.block_storage.snapshots(all_projects=all_projects)
        return json.dumps(list(response))


    def show(self, snapshot_id):
        if not snapshot_id:
            raise AttributeError("Required attribute 'snapshot_id' was not defined")

        LOG.debug(f"Trying to find '{snapshot_id}' snapshot")
        all_projects = True if self.sdk_conn.auth["username"] == "admin" else False
        response = self.sdk_conn.block_storage.find_snapshot(snapshot_id, all_projects=all_projects)
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
