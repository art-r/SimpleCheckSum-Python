import subprocess
import sys

try:
    file = sys.argv[1]
    checksum = sys.argv[2]
    shouldSum = sys.argv[3]

except IndexError:
    print('Error please call program with these arguments: Check-The-Sum.py <path-to-file> <used-checksum> <expexted-checksum>')
    sys.exit(1)

#realCheckSum = subprocess.Popen('openssl {usedChecksum} {file}'.format(usedChecksum = checksum, file=file), shell=True)
checkTheSum = subprocess.run(["openssl", "{}".format(checksum), "{}".format(file)], stdout=subprocess.PIPE)
out = checkTheSum.stdout.decode('utf-8')
generatedCheckSum = out.split("=")[1].strip()
if (generatedCheckSum == shouldSum.strip()):
    print('SUCCESS! The checksums match each other')

else:
    print('ERROR! THE CHECKSUMS DO NOT MATCH EACH OTHER!')

print('used method: {}'.format(checksum))
print('system generated checksum: {}'.format(out))
print('expexted checksum: {}'.format(shouldSum))
