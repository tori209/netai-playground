#! /usr/bin/env bash

if [ $# -lt 2 ]; then
	echo "Usage: $0 <namespace> <env file>"
	exit;
fi

NAMESPACE=$1
FILE=$2

if [ ! -e $FILE ]; then
	echo "File Not Exist"
	exit -1;
fi

if [ `kubectl get ns | grep ${NAMESPACE} | wc -l` -eq 0 ]; then
	echo "No Namespace"
	exit -1;
fi

kubectl apply -f <(kubectl create secret generic env -n ${NAMESPACE} --from-env-file=${FILE} --dry-run=client -o yaml)
