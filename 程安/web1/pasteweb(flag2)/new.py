
import sys
try:
    # python 2.x
    import urllib2
    import urlparse
    import Queue
except Exception as e:
    # python 3.x
    import urllib.request as urllib2
    import urllib.parse as urlparse
    import queue as Queue

import os
import zlib
import threading
import re
import time
from lib.parser import parse
import ssl
for entry in parse('index'):
    if "sha1" in entry.keys():
        entry_name = entry["name"].strip()

        print('[+] %s' % entry['name'] ,entry['sha1'])
            # except Exception as e:
                # pass
