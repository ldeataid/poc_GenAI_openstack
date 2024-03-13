import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class AvailabilityZones:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn

    
    def list(self):
        LOG.debug(f"Trying to fetch availability zones")
        return self.sdk_conn.compute.availability_zones()
