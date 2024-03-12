import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Regions:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch regions")
        return self.sdk_conn.identity.regions()

    
    def show(self, region_id):
        if not region_id:
            raise AttributeError("Required attribute 'region_id' was not defined")

        LOG.debug(f"Trying to find '{region_id}' region")
        return self.sdk_conn.identity.find_region(region_id)
