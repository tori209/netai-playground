SECRET_NAME="additional-scrape-configs"
INPUT_FILE="prometheus-additionalScrapeConfigs.yaml"
SECRET_KEY_NAME="prometheus-additional.yaml"
NAMESPACE="monitoring"

kubectl apply -n $NAMESPACE -f <(kubectl create secret generic $SECRET_NAME --from-file=${SECRET_KEY_NAME}=${INPUT_FILE} --dry-run=client -oyaml)

