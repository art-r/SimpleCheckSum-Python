# SimpleCheckSum-Python
[![Pylint](https://github.com/art-r/SimpleCheckSum-Python/actions/workflows/pylint.yml/badge.svg?branch=main)](https://github.com/art-r/SimpleCheckSum-Python/actions/workflows/pylint.yml)
[![Build Status](https://app.travis-ci.com/art-r/SimpleCheckSum-Python.svg?branch=main)](https://app.travis-ci.com/art-r/SimpleCheckSum-Python)

Simple python script that will check the given hash of a file against its system generated hash

Simply call the script via the commandline the following way:

```bash
python3 Check-The-Sum.py <path-to-file-that-should-be-checked> <checksumAlgorithm-to-use> <expected-checksum>
```

**Requirements:**
- openssl
- python3 (supports python >= 3.5)

**Output if the checksums match:**
```bash
SUCCESS! The checksums match each other
used method: <used-method>
system generated checksum: <checksum>
expected checksum: <expected-checksum>
```

**Output if the checksums dont match:**
```bash
ERROR! THE CHECKSUMS DO NOT MATCH EACH OTHER!
used method: <used-method>
system generated checksum: <checksum>
expected checksum: <expected-checksum>
```
