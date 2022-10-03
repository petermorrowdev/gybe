set -e

# Install deps
pip install datamodel-code-generator

# Clean up old kubernetes code
rm -rf gybe/kubernetes

# Generate pydantic models from Kubernetes OpenAPI 
datamodel-codegen --input kubernetes/api/openapi-spec/v3/ --input-file-type=jsonschema --output=gybe/kubernetes
