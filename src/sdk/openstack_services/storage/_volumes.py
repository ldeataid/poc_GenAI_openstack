import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Volumes:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch volumes")
        response = self.sdk_conn.block_storage.volumes()
        return json.dumps(list(response))


    def show(self, volume_id):
        if not volume_id:
            raise AttributeError("Required attribute 'volume_id' was not defined")

        LOG.debug(f"Trying to find '{volume_id}' volume")
        response = self.sdk_conn.block_storage.find_volume(volume_id)
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
