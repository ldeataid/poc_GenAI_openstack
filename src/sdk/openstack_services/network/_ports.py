import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Ports:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch ports")
        response = self.sdk_conn.network.ports()
        return json.dumps(list(response))

    
    def show(self, port_id):
        if not port_id:
            raise AttributeError("Required attribute 'port_id' was not defined")

        LOG.debug(f"Trying to find '{port_id}' port")
        response = self.sdk_conn.network.find_port(port_id)
        return json.dumps(response)
