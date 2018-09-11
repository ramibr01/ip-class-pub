#!/usr/bin/env python3

import cgi
from datetime import datetime as dt


def isPrime(n: int) -> bool:
    '''Check if the number is prime'''
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

def getNPrimes(n):
    primesList = []
    currentNum = 2
    while len(primesList) != n:
        for i in range(2, currentNum // 2 + 1):
            if currentNum % i == 0:
                break
        else:
            primesList.append(currentNum)
        currentNum += 1
    return primesList

params = cgi.FieldStorage()
name = params['name'].value
n = int(params['n'].value)

print('Content-Type: text/html')
print()

print('<html>')
print('  <head>')
print('    <title>Hello CS330</title>')
print('    <script type="text/javascript" src="/prime.js"></script>')
print('  </head>')
print('  <body>')
print('<h1>Hello {}!</h1>'.format(name))
print('<p>Today is <em>{}</em></p>'.format(dt.now()))
if isPrime(n):
    print('Python says {} is prime'.format(n))
    print('<br>')
    print('<br>')
else:
    print('Python says {} is NOT prime'.format(n))
    print('<br>')
    print('<br>')
#print('<script>document.write(isPrime({}));</script>'.format(n))
#print('<script> if(isPrime({})) { document.write("JavaScript says {} is Prime"); } else { document.write("JavaScript says {} is NOT Prime"); } </script>')
print('<script> \
        if(isPrime({})) {{ \
            document.write("JavaScript says {} is Prime"); \
        }} else {{ \
            document.write("JavaScript says {} is NOT Prime"); \
        }} \
        </script>'.format(n,n,n))

#print('<script> if(isPrime({})) {{ document.write("JavaScript says", {}, "is Prime"); }} else {{ document.write("JavaScript says", {}, "is NOT Prime"); }} </script>'.format(n))

print('<br>')
print('<br>')
print('First {} prime numbers generated by Python: '.format(n) ,getNPrimes(n))
print('<br>')
print('<br>')
print('First {} prime numbers generated by JavaScript: '.format(n))
print('<script>document.write("[",getNPrimes({}),"]")</script>'.format(n))
print('  </body>')
print('</html>')