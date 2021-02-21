set -e

# Install deps
pip install openapi2jsonschema datamodel-code-generator

# Clean up old kubernetes code
rm -rf gybe/kubernetes

# Download k8s swagger
curl -O https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/swagger.json
# Convert Swagger to JSON Schema
openapi2jsonschema swagger.json --kubernetes
# Remove current gybe.kubernetes module
rm -rf gybe/kubernetes
# Generate pydantic models from JSON Schema
# Kubernetes does not support OpenAPI v3 yet - https://github.com/kubernetes/enhancements/pull/1263
datamodel-codegen --input schemas/_definitions.json --input-file-type=jsonschema --output=gybe/kubernetes
