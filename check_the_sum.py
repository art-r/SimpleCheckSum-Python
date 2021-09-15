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

def check(file, checksum, should_sum):
    checkTheSum = subprocess.run(["openssl", "{}".format(checksum), "{}".format(file)],
    stdout=subprocess.PIPE, check=True)

    out = checkTheSum.stdout.decode('utf-8')
    generatedCheckSum = out.split("=")[1].strip()

    if generatedCheckSum == should_sum.strip():
        print('SUCCESS! The checksums match each other')
        return 1

    else:
        print('ERROR! THE CHECKSUMS DO NOT MATCH EACH OTHER!')
        return 0

    print('used method: {}'.format(checksum))
    print('system generated checksum: {}'.format(out))
    print('expexted checksum: {}'.format(should_sum))


if __name__ == "__main__":
    try:
        check(sys.argv[1], sys.argv[2], sys.argv[3])
    except IndexError:
        print('Error please call the program with these arguments:')
        print('python3 check_the_sum.py <path-to-file> <used-checksum> <expexted-checksum>')
        sys.exit(1)