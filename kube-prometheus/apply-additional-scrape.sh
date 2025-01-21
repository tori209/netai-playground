SECRET_NAME="additional-scrape-configs"
INPUT_FILE="prometheus-additionalScrapeConfigs.yaml"
NAMESPACE="monitoring"

kubectl apply -n $NAMESPACE -f <(kubectl create secret generic $SECRET_NAME --from-file=$INPUT_FILE --dry-run=client -oyaml)

