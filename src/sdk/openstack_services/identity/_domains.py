import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Domains:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch domains")
        return self.sdk_conn.identity.domains()

    
    def show(self, domain_id):
        if not domain_id:
            raise AttributeError("Required attribute 'domain_id' was not defined")

        LOG.debug(f"Trying to find '{domain_id}' domain")
        return self.sdk_conn.identity.find_domain(domain_id)
