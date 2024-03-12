import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Images:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn

    
    def list(self):
        LOG.debug("Trying to fetch images")
        return self.sdk_conn.compute.images()


    def show(self, image_id):
        if not image_id:
            raise AttributeError("Required attribute 'image_id' was not defined")

        LOG.debug(f"Trying to find '{image_id}' image")
        return self.sdk_conn.compute.find_image(image_id)


    def show_metadata(self, image_id):
        if not image_id:
            raise AttributeError("Required attribute 'image_id' was not defined")

        LOG.debug(f"Trying to find '{image_id}' image's metadata")
        return self.sdk_conn.compute.get_image_metadata(image_id)
