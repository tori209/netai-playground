#! /usr/bin/env bash

sudo apt-get update
sudo apt-get install -y ca-certificates curl gpg

# Include Kubernetes APT Repository
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.31/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
sudo chmod 644 /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.31/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo chmod 644 /etc/apt/sources.list.d/kubernetes.list

# Check `kubeadm` Package Info.

if [[ `sudo apt-cache policy kubeadm` == *"Unable to locate package"* ]]; then
	echo "[ERROR] Failed to add Kubernetes APT Repo." 1>&2
	exit 1;
fi

# Install Kubernetes w. Tools
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl

for PKG in kubelet kubeadm kubectl; do
	if [ `dpkg -l | grep $PKG | wc -l` -eq 0 ]; then
		echo "[ERROR] $PKG is not Installed. Try Again." 1>&2
		exit 1;
	fi
done

sudo apt-mark hold kubelet kubeadm kubectl

echo "[INFO] \`kubelet\` Version:"
kubelet --version

echo "[INFO] \`kubectl\` Version:"
kubectl version

echo "[INFO] \`kubeadm\` Version:"
kubeadm version

echo "[INFO] Trying to enable kubelet on Systemd..."
sudo systemctl daemon-reload
sudo systemctl restart kubelet
sudo systemctl enable --now kubelet.service

echo "Finished."
