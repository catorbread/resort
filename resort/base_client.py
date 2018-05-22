import urllib.parse

import requests

from etalons import BasicHTTPResponseEtalon
from server_spec import ServerSpecReader


class BasicClient(object):
    """Establishes connection to the server with given url.
    With spec_file provided it can make snapshot for each
    entry described in the spec.

    Args:
        server_url (str)
        spec_file (str, optional): Defaults to None
    """

    def __init__(self, server_url: str, spec_file: str=None):
        self._server_url = server_url
        if spec_file is not None:
            self.server_spec = ServerSpecReader(spec_file=spec_file)

    def prepare(self):
        """Load a API Spec to the client's ServerSpecReader.

        Returns: self to create a prepared client:
        client = BasicClient().prepare()

        """
        self.server_spec.prepare()
        return self

    def snapshot_etalons(self, Etalon=BasicHTTPResponseEtalon):
        """Make etalon (a "snapshot") for each entry in the spec
        which was read from the spec_file.
        see: snapshot

        Args:
          Etalon: Constructor (Default value = BasicHTTPResponseEtalon)

        Returns: A generator of etalons

        """
        for method, each_entry in self.server_spec.paths_and_methods():
            yield self.snapshot(each_entry, method)

    def snapshot(self, entry: str, method: str, Etalon=BasicHTTPResponseEtalon):
        """Makes etalon, a "snapshot" of response from the server
        to request on the :entry: with the HTTP :method:

        Args:
          entry: str: part of the url that describes an API entry
          method: str: HTTP method: GET - supported, TODO: POST, PUT...
          Etalon: Constructor (Default value = BasicHTTPResponseEtalon)

        Returns:

        """
        url = urllib.parse.urljoin(self._server_url, entry)
        return Etalon(entry=entry,
                      response=requests.request(method, url))
