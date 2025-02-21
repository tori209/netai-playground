## Why you should check this
- At Tetragon OSS 1.3, LSM Hook will be not working since tetragon agent cannot recognize "/sys/kernel/security/lsm".
- That's because lsm config file isn't shared with tetragon agent.
- Therefore, you should add additional Volume that containes 'lsm' file.

## How to do
- type 'kubectl -n kube-system edit ds/tetragon'.
- find ".spec.template.spec.containers.volumes", and add element.
  ```
- hostPath:
    path: /sys/kernel/security # where "lsm" file exists
    type: Directory
  name: kernel-security
  ```
- find definition of tetragon agent, which is the one of ".spec.template.spec.containers[]".
- add volumeMount like:
  ```
- mountPath: /sys/kernel/security
  name: kernel-security
  ```

