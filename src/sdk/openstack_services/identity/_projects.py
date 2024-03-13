import logging
from openstack.connection import Connection


LOG = logging.getLogger("openstacksdk")


class Projects:
    def __init__(self, conn: Connection):
        self.sdk_conn = conn


    def list(self):
        LOG.debug("Trying to fetch projects")
        return self.sdk_conn.identity.projects()

    
    def show(self, project_id):
        if not project_id:
            raise AttributeError("Required attribute 'project_id' was not defined")

        LOG.debug(f"Trying to find '{project_id}' project")
        return self.sdk_conn.identity.find_project(project_id)
