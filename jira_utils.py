# Utilities for interacting with Jira

import logging

from jira import JIRA

# create a connection object, jc
#jc = connect_jira("url", "username", "api token")


class JiraClient(object):
    """
    Client to connect to jira
    """

    def __init__(self, server, logger=None):
        self.server = server

    def login(self, user, password):
        print("Connecting to Jira server {}".format(self.server))

        try:
            self.jira = JIRA(
                options={"server": self.server, 'verify': False},
                basic_auth=(user, password)
            )
        except Exception as e:
            print("Failed to connect to JIRA.. Error {}".format(
                str(e)))
        else:
            return True

    def create_issue(self, issue):
        """
        issue requires
        {
          'project': ''
        }
        """
        pass
