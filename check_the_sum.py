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
    """
    The main function which will check the checksum
    Needs the absolute path to the file, the checksum method
    and the expected checksum
    """
    checksum_process = subprocess.run(["openssl", "{}".format(checksum), "{}".format(file)],
    stdout=subprocess.PIPE, check=True)

    out = checksum_process.stdout.decode('utf-8')
    generated_check_sum = out.split("=")[1].strip()

    if generated_check_sum == should_sum.strip():
        print('SUCCESS! The checksums match each other')
        return_val = 0
    else:
        print('ERROR! THE CHECKSUMS DO NOT MATCH EACH OTHER!')
        return_val = 1

    return return_val

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
