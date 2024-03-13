import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Backups:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch backups")
        return self.sdk_conn.block_storage.backups()

    
    def show(self, backup_id):
        if not backup_id:
            raise AttributeError("Required attribute 'backup_id' was not defined")

        LOG.debug(f"Trying to find '{backup_id}' backup")
        return self.sdk_conn.block_storage.find_backup(backup_id)
