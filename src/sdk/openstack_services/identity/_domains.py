import json
import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Domains:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch domains")
        response = self.sdk_conn.identity.domains()
        return json.dumps(list(response))

    
    def show(self, domain_id):
        if not domain_id:
            raise AttributeError("Required attribute 'domain_id' was not defined")

        LOG.debug(f"Trying to find '{domain_id}' domain")
        response = self.sdk_conn.identity.find_domain(domain_id)
        return json.dumps(response)
