#! /usr/bin/env bash

# containerd binary installation
wget "https://github.com/containerd/containerd/releases/download/v1.7.23/containerd-1.7.23-linux-amd64.tar.gz"
tar Cxzvf /usr/local containerd-1.7.23-linux-amd64.tar.gz

# systemd setting
wget "https://raw.githubusercontent.com/containerd/containerd/main/containerd.service"
mkdir -p /usr/local/lib/systemd/system
mv containerd.service /usr/local/lib/systemd/system

sudo systemctl daemon-reload
sudo systemctl enable --now containerd

# runc installation
wget "https://github.com/opencontainers/runc/releases/download/v1.2.1/runc.amd64"
sudo install -m 755 runc.amd64 /usr/local/sbin/runc

# CNI Plugins Installation
mkdir -p /opt/cni/bin
wget "https://github.com/containernetworking/plugins/releases/download/v1.6.0/cni-plugins-linux-amd64-v1.6.0.tgz"
tar Cxzvf /opt/cni/bin cni-plugins-linux-amd64-v1.6.0.tgz

# Configuration Creation
sudo mkdir -p /etc/containerd
sudo bash -c "containerd config default > /etc/containerd/config.toml"
sudo sed -i '/SystemdCgroup/ s/false/true/' /etc/containerd/config.toml

sudo systemctl restart containerd

echo "containerd installation finished.\n\t\--configuration file at: '/etc/containerd/config.toml'"
