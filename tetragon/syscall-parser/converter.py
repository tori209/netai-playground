#! /usr/bin/env python3

import os
import sys
import json

import syscall_name

log_dir = None
log_name = None
pwd_dir = None

def __conv_init():
    log_dir = os.environ.get("LOG_DIR_PATH")
    if log_dir is None:
        log_dir = "/var/run/cilium/tetragon"
    log_name = os.environ.get("LOG_FILE_NAME")
    if log_name is None:
        log_name = "tetragon.log"
    pwd_dir = os.environ.get("PWD_DIR_PATH")
    if pwd_dir is None:
        pwd_dir = os.getcwd()

def __conv_wait():
    file_path = os.path.join(log_dir, log_name);

def convert():
    __conv_init()
    __conv_wait()


while True:
    try:
        data = sys.stdin.readline()
        if data == "":
            break;
        data = json.loads(data)['process_tracepoint']
        syscall_id = syscall_id2name[int(data['args'][0]['long_arg'])]
        pid = data['process']['pid']
        uid = data['process']['uid']
        ppid = data['parent']['pid']
        p_bin = data['process']['binary']

        if pid not in pid2bin:
            pid2bin[pid] = [p_bin]
        elif pid2bin[pid][-1] != p_bin:
            pid2bin[pid].append(p_bin)

        if ppid not in pp2p:
            pp2p[ppid] = set()
        pp2p[ppid].add(pid)

        if pid not in syscall_seq:
            syscall_seq[pid] = []
        syscall_seq[pid].append(syscall_id)

        print(f"Now: {cnt} / Syscall ID: {syscall_id} / PID: {pid} / PPID: {ppid} / Who: {uid}")
    except KeyError:
        print(f"Now: {cnt} / SKIP")
    finally:
        cnt+=1

for key in syscall_seq.keys():
    syscall_seq[key] = "|".join(syscall_seq[key])

print(pid2bin)
print(pp2p)
print(syscall_seq)
