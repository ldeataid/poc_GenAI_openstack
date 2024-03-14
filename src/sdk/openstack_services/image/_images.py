import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Images:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch images")
        response = self.sdk_conn.image.images()
        return json.dumps(list(response))

    
    def show(self, image_id):
        if not image_id:
            raise AttributeError("Required attribute 'image_id' was not defined")

        LOG.debug(f"Trying to find '{image_id}' image")
        response = self.sdk_conn.image.find_image(image_id)
        return json.dumps(response)
