import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Regions:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch regions")
        response = self.sdk_conn.identity.regions()
        return json.dumps(list(response))


    def show(self, region_id):
        if not region_id:
            raise AttributeError("Required attribute 'region_id' was not defined")

        LOG.debug(f"Trying to find '{region_id}' region")
        response = self.sdk_conn.identity.find_region(region_id)
        if response is None:
            raise Exception("Region not found!")

        return json.dumps(response)
