set -e

# Wipe existing kubernetes code
rm -rf gybe/kubernetes

# Generate pydantic models from Kubernetes OpenAPI 
datamodel-codegen --input kubernetes/api/openapi-spec/v3/ --input-file-type=openapi --output=gybe/kubernetes
