import base64

a='wcvGwPzT7+LY9PPo6eLY7vTY6ejz2OH15uDu6+LY5un+6uj14qmpqfo='
b=list(base64.b64decode(a))
for i in range (len(b)):
    b[i] ^= 135

print(bytes(b))