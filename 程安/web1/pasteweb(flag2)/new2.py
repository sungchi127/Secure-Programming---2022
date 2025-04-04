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
import base64
data=b"eAGlVm1z2zYM3tfkVyC8rLZvlWU77ZbFltMXu01vaZPZ6Xq7XE4ni7TFRRI1korjy+W/DySl2Hnp1m1fbJIAQeAB8ECzVMxgr9vZ/25wWCTFNoDvwxGTDLiClSglKBaLnMK749fvD+zvTRSmXX2W7oV6wuNfVmF7wXV4vPfist0WMhx1abjqlOG8m4/CKOyMolXYzcOUKYUPHN7iEwrXXOSh0pHUzVYfj/i8yZViurkbTsfT6YeTT+eNPMpY46LVukE5QMIiymSTHIs40nj7AHxGuU50lrbRMLFmAChnzqJ5aDcXSwggZ0sYRZqd8awS7i6YZvkVyohbkT7sZvSlOcA/YlzapTOMPMejYhGaFYt1kyRC6YDOgM6Me8FNZalJTk+mZ+8n42k4ekNat1AqJp+Sfp6OJ0ZeREothaRP6Zy+nk6/nExGqGfCcvAYYCa/jSfnjcn418/j6Vn4cXx2dDJqXEAQQMM834BnzzBvDkZzcN4wblQ4PhbWPiDIj4VxKSXLdagRtHUWME/RTDUNsN4QoTOQYhqzotkCD3iur6IUc+gef2gChtDtVOlEfNeZRhsqWuAzBv8vCcuBClN9ECPGMJciO7Qp+Uod1LnfyD7ArcENX5FMlal2WfyzZHLVJNPx8fjtmU1RGMWxKHP93O1qRODd5OSjyZFmSzarlRR8ORpPxvdVg8aNqZw6aFKbIBet2wa8/jS6947RduiQOjXk4rbRxxDA+osA72C95WUWSrFEpJ3/dRd8HbZjseA5vIt4yuh/Bsv45KCaMx0nxoU7D0xP2EbdNVrnnQvYwcJ7HM0/JvhNROEoii+Z3PnPjq5rx1U3Ol275fz893RxONze3h7sjE7env1+OgZDLMPtQf2H7DNEAAaa65QNT01lfGGzge/2RqJiyQsNSsYBSbQu1IHvxzRva0zJkuc0Vqodi4wMB75TtfZSnl9CItl8fanMi8uFUfVfbdz150Jm6lWn3Wt3fcqVdgftjOdtNE1AsjQgSq+QaRPGNLHm7d6sAGaCrhyVGjLli0QfYDt2rhIHmOFL9MzcdzdtOO4qMoppdFHqZrMVDKt2bUuWiStk1Oew1+l0KgJG3Q+5ZtIQgVHeJIE2HpbMFFgkFUO15mNp64fuc+OXs7fGauCblFrXTCQQp8igAZktvIWMVt7PnY6NGIOg/KqWzlN2DX+USvP5youRzrC8uWaZqjeJNy/TtLp5/y4C6y29897L7y8AX1EpThCv1+lAsfK6PSiuvX2gUhSeSiKKc0Yij1BGveu1OTSY9GpfNLvWXu86hbnItTcTKQV75AzvG/9tD2OgPQe7ydpmNJn29u9ctUJTE7X9heQUzI8Xi1R5XVhEhfcjgYzpRNDADigCHFfm1j07+EwazVham5qlIr58oIE6qojyWuWh65+rQYMJQ621/8ZNvMrzotRgR+aa+ECvChYQY4rUdu3TsLRpAQy4S6BIo5gliBdOVELAv2984FvXHxz+33Cwwe14/oZw7gi/Cme9r0vUoPl3IX1TRA5Bk77NniEVpvfPEk4pDlHbbQEZHAZPzev+4ZA8fHlWai3ucuxygUl4YWq+58p1mWADrRviJTZEVfngGsFLF/XKlTaSw6NaspVuackVCJaI7x7fTOTActz6ZIDEd1VvNzZ3SzSC3DDc3rJfs09+Vd59a7RaB4Ccv7VlW8wAW4nWtbjwJDY0khGSp8Ty81KEoloaiQneNoLZ/GSowXuBRCxSrOooZRLL2hJqQAqhuPtqnfNrRvugRYH0y7I+yIqKcY0wbaE/Rd0Md0xBhmMphRz4RaUxdAGyOBF2UiG1oX2G3wvrybiOtA9l/uDjekN4iBPJ2q1grMBjOeXzvoEIGckOw+2/AF0xpns="
data = base64.b64decode(data)
data = zlib.decompress(data)
data = re.sub(b'blob \d+\00', b'', data)
with open('object', 'wb') as f:
    f.write(data)