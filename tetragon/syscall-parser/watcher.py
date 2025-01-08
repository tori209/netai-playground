#! /usr/bin/env python3

import os
import sys
import json
import subprocess
import signal

import syscall_name

def run():
    syscall_id2name = syscall_name.get_syscall_mapping("", False)

    command = ["tetra", "getevents", "-n", "playground", "-o", "json"]
    tetra_sub = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    try:
        for line in tetra_sub.stdout:
            data = json.loads(line)
            if 'process_tracepoint' not in data:
                continue
            node_name = data['node_name']
            time = data['time']

            data = data['process_tracepoint']
            syscall_id = syscall_id2name[int(data['args'][0]['long_arg'])]
            pid = data['process']['pid']
            ppid = data['parent']['pid']
            p_bin = data['process']['binary']
            namespace_name = data['process']['pod']['namespace']
            pod_name = data['process']['pod']['name']
            print(f"({time},{node_name},{namespace_name},{pod_name},{pid},{syscall_id},{ppid},{p_bin})")
    except KeyboardInterrupt:
        print("\033[31mKeyboardInterrupt. Stop.\033[0m", file=sys.stderr)
    except EOFError:
        print("\0ee[31mTetra CLI Terminated. Stop.\033[0m", file=sys.stderr)
    finally:
        tetra_sub.send_signal(signal.SIGINT)
        tetra_sub.wait()

if __name__ == "__main__":
    run()
