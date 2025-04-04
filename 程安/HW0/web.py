a = 1 // 1 ; b = '''
var fs = require('fs')
fs.readFile('/flag', function (error, data) {
  if (error) {
      console.log('fail')
      return
  }
  process.stdout.write(data.toString())
})
/* 
'''
import os
f = open('/flag','r')
ff=f.read()
print(ff,end='')
# */
