import base64
s = b'RElSQwAAAAIAAAAHY4+IKypTZpljj4grKdlUmQABAwUAcgqqAACBpAAAA+gAAAPoAAABl7HVLzuQJ5pvrlkZUDCUNEfHyJd6AAxkb3dubG9hZC5waHAAAAAAAABjj5q/KONcbGOPmr8n7zhsAAEDBQByCqwAAIGkAAAD6AAAA+gAABHiLft/l1Q0t4azBQalN/wxjUlPN0wAC2VkaXRjc3MucGhwAAAAAAAAAGOPmqcMhC/VY4+apwuQC9UAAQMFAHIKzgAAgaQAAAPoAAAD6AAAEQ4ZCS7Twqx4R1mWi6FgnDZIvDZThQAMZWRpdGh0bWwucGhwAAAAAAAAY4+dzAwJzpZjj53MCxWqlwABAwUAcgrQAACBpAAAA+gAAAPoAAAMJEaCwHVXYf9ORyTflJXxUSEr688BAAlpbmRleC5waHAAY4+J8iOmPdFjj4nyIrIZ0gABAwUAcgqGAACBpAAAA+gAAAPoAAHbILZuItbUoqW5sXymYWVIXPLIz4AlAA1sZXNzYy5pbmMucGhwAAAAAABjj4JuBGtgRGOPgm4DdzxFAAEDBQByCpUAAIGkAAAD6AAAA+gAAAC2YbcDopfITZKf9+IwBLmnMcD7jeYACXNoYXJlLnBocABjj4RIEcUplmOPhEgQ0QWWAAEDBQByCpIAAIGkAAAD6AAAA+gAAALBo2DQ0G69LFLB2nGtw7bpX8g4hpoACHZpZXcucGhwAABUUkVFAAAAGQA3IDAK/Ni51SqCvD3GFL+4BZjDSDmEzpmd92XetgTTPICpTjDJrNiOoEfVXQ=='
# s = 'Hello World'

bytes_decode = base64.b64decode(s)
# ss = bytes_decode.decode("utf-8")

print(bytes_decode)
path = 'index'
f = open(path, 'wb')
f.write(bytes_decode)
f.close()
