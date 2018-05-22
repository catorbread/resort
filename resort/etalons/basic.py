import requests

import etalons.base


class BasicHTTPResponseEtalon(etalons.base.BaseEtalon):
    """Basic etalon, represents a requests.Response as json:
    ```
    {
      "headers": {"Header": "Value"
                  ...
                 },
      "body": ...
    }
    ```

    Args:
        entry (str): - spec entry.
        response (requests.Response, optional): Defaults to None.
    """
    _EXT = 'json'
    _STR = 'Response:\n{headers}\nBody:\n{body}'

    def __init__(self, entry: str, response: requests.Response=None):
        super().__init__(entry=entry, ext=BasicHTTPResponseEtalon._EXT)
        if response is not None:
            self._headers = response.headers
            self._body = response.text

    def restore_from_dict(self, etalon: dict):
        """TODO: Add the docstring

        Args:
          etalon: dict:

        Returns:

        """
        self._headers = etalon['headers']
        self._body = etalon['body']

    def dump(self):
        """TODO: Add the docstring

        Returns:
            [type]: [description]
        """
        return dict(headers=dict(self._headers),
                    body=self._body)
    
    def __str__(self):
        strargs = dict(headers="\n".join('{0}: {1}'.format(k, v)
                                         for k, v
                                         in self._headers.items()),
                       body=self._body)
        return BasicHTTPResponseEtalon._STR.format(strargs)
