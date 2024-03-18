import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Backups:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch backups")
        response = self.sdk_conn.block_storage.backups()
        return json.dumps(list(response))


    def show(self, backup_id):
        if not backup_id:
            raise AttributeError("Required attribute 'backup_id' was not defined")

        LOG.debug(f"Trying to find '{backup_id}' backup")
        response = self.sdk_conn.block_storage.find_backup(backup_id)
        if response is None:
            raise Exception("Backup not found!")

        return json.dumps(response)
