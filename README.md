# SimpleCheckSum-Python
Simple python script that will check the given hash of a file against its system generated hash

Simply call the script via the commandline the following way:

```bash
python3 Check-The-Sum.py <path-to-file-that-should-be-checked> <checksumAlgorithm-to-use> <expected-checksum>
```

**Requirements:**
- openssl
- python3

**Output if the checksums match:**
SUCCESS! The checksums match each other
used method: <used-method>
system generated checksum: <checksum>
expected checksum: <expected-checksum>

**Output if the checksums dont match:**
ERROR! THE CHECKSUMS DO NOT MATCH EACH OTHER!
used method: <used-method>
system generated checksum: <checksum>
expected checksum: <expected-checksum>
