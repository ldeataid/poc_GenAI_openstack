import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Routers:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch routers")
        response = self.sdk_conn.network.routers()
        return json.dumps(list(response))

    
    def show(self, router_id):
        if not router_id:
            raise AttributeError("Required attribute 'router_id' was not defined")

        LOG.debug(f"Trying to find '{router_id}' router")
        response = self.sdk_conn.network.find_router(router_id)
        return json.dumps(response)
