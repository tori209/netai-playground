### IMPORTANT
처음 Prometheus를 설치하면, etcd / scheduler / controller-manager의 Metric을 가져올 수 없음.
이는 metrics를 가져올 주소가 127.0.0.1:[port]로 지정되어 외부에서 수집할 수 없기 때문.
이 주소들을 0.0.0.0으로 수정하여 Prometheus가 가져올 수 있도록 수정해주어야 함.
Control Node의 Manifest(Default: /etc/kubernetes/manifests) 수정 필요.

kube-controller-manager.yaml --> Command Param. 중 --bind-address=0.0.0.0 으로 수정.
kube-etcd.yaml --> Command Param. 중 --listen-metrics-urls=http://0.0.0.0:2381로 수정.
kube-scheduler.yaml --> Command Param. 중 --bind-address=0.0.0.0 으로 수정

Reference: https://pythaac.tistory.com/457
