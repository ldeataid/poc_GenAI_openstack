import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class ServerVolumeAttachments:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self, server_id):
        if not server_id:
            raise AttributeError("Required attribute 'server_id' was not defined") 

        LOG.debug("Trying to fetch volume attachments for server '{server_id}'")
        response = self.sdk_conn.compute.volume_attachments(server_id)
        return json.dumps(list(response))


    def show(self, server_id, volume_attachment_id):
        if not server_id:
            raise AttributeError("Required attribute 'server_id' was not defined")

        if not volume_attachment_id:
            raise AttributeError("Required attribute 'volume_attachment_id' was not defined")

        LOG.debug(f"Trying to find server '{server_id}' '{volume_attachment_id}' volume attachment")
        response = self.sdk_conn.compute.get_volume_attachment(server_id, volume_attachment_id)
        return json.dumps(response)
