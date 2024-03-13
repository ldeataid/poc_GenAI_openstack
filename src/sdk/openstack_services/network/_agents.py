import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Agents:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch network agents")
        return self.sdk_conn.network.agents()

    
    def show(self, agent_id):
        if not agent_id:
            raise AttributeError("Required attribute 'agent_id' was not defined")

        LOG.debug(f"Trying to find '{agent_id}' network agent")
        return self.sdk_conn.network.get_agent(agent_id)
