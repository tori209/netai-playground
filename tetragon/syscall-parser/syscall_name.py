#! /usr/bin/env python3

import os
import sys
import tempfile
import platform

__GLIBC_LOC = {
    "x86_64": "sysdeps/unix/sysv/linux/x86_64/64",
    "i386": "sysdeps/unix/sysv/linux/i386",
    "arm64": "sysdeps/unix/sysv/linux/aarch64",
    "arm32": "sysdeps/unix/sysv/linux/arm"
}

def get_syscall_mapping(prefix="sys_", uppercase = True):
    """
    Generate Mapping from Syscall_ID to Syscall_name
    prefix(str)
    uppercase(bool)
    """

    if type(prefix) != str:
        raise ValueError("prefix should be string")
    if type(uppercase) != bool:
        raise ValueError("uppercase should be bool")

    arch = platform.machine()
    glibcLocation = __GLIBC_LOC[arch]
    syscall_name = {}

    with tempfile.TemporaryDirectory(prefix="glibc_") as tempdir:
        os.system(f"git archive --remote=git://sourceware.org/git/glibc.git HEAD:{glibcLocation} -- arch-syscall.h | tar xv -C {tempdir} > /dev/null")
        with open(f"{tempdir}/arch-syscall.h", "r") as sys_header:
            while True:
                line = sys_header.readline()
                if line == "":
                    break;
                if (not line.startswith("#define")) or (line.find("__NR_") == -1):
                    continue;
                line = line[13:].split(' ')
                name = (prefix + line[0].strip()).lower()
                if uppercase:
                    name = name.upper()
                num = int(line[-1].strip())
                syscall_name[num] = name

    return syscall_name

if __name__ == "__main__":
    import json
    print(json.dumps(get_syscall_mapping(), sort_keys=True, indent=4))
