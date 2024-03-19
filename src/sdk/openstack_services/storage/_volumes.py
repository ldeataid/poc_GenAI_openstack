import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Volumes:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch volumes")
        all_projects = True if self.sdk_conn.auth["username"] == "admin" else False
        response = self.sdk_conn.block_storage.volumes(all_projects=all_projects)
        return json.dumps(list(response))


    def show(self, volume_id):
        if not volume_id:
            raise AttributeError("Required attribute 'volume_id' was not defined")

        LOG.debug(f"Trying to find '{volume_id}' volume")
        all_projects = True if self.sdk_conn.auth["username"] == "admin" else False
        response = self.sdk_conn.block_storage.find_volume(volume_id, all_projects=all_projects)
        if response is None:
            raise Exception("Volume not found!")

        return json.dumps(response)


    def show_metadata(self, volume_id):
        if not volume_id:
            raise AttributeError("Required attribute 'volume_id' was not defined")

        LOG.debug(f"Trying to find '{volume_id}' volume's metadata")
        response = self.sdk_conn.block_storage.get_volume_metadata(volume_id)
        if response is None:
            raise Exception("Volume not found!")

        return json.dumps(response)
