"""
Simple tool that checks the checksum of a file against a provided checksum
If the checksum is valid it will return:
    "SUCCESS! The checksums match each other"
Else it will return:
    "ERROR! THE CHECKSUMS DO NOT MATCH EACH OTHER!"

In either way it will display the generated checksum and the used method!

Syntax for calling:
python3 check_the_sum.py <path-to-file> <used-checksum> <expexted-checksum>
"""

import subprocess
import sys

try:
    file = sys.argv[1]
    checksum = sys.argv[2]
    shouldSum = sys.argv[3]

except IndexError:
    print('Error please call the program with these arguments:')
    print('python3 check_the_sum.py <path-to-file> <used-checksum> <expexted-checksum>')
    sys.exit(1)

checkTheSum = subprocess.run(["openssl", "{}".format(checksum), "{}".format(file)],
stdout=subprocess.PIPE, check=True)

out = checkTheSum.stdout.decode('utf-8')
generatedCheckSum = out.split("=")[1].strip()
if generatedCheckSum == shouldSum.strip():
    print('SUCCESS! The checksums match each other')

else:
    print('ERROR! THE CHECKSUMS DO NOT MATCH EACH OTHER!')

print('used method: {}'.format(checksum))
print('system generated checksum: {}'.format(out))
print('expexted checksum: {}'.format(shouldSum))
