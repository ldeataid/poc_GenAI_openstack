from openstack.connection import Connection

from ._images import Images


class ImageService:
    """The image service (Glance)"""
    
    def __init__(self, conn: Connection):
        sdk_conn = conn

        self.images = Images(sdk_conn)
