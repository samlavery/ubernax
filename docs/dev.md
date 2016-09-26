# Development

# Requirements
* Python 3.5+
* Minikube

Create your own secrects directory, and in it a file named 'secrets.yaml'.  I'll try to keep this updated as the project evolves.

``apiVersion: v1
kind: Secret
metadata:
  name: pg-secrets
  namespace: dev
type: Opaque
data:
  password: some_base64_encoded_jibberish
  user: some_base64_encoded_jibberish 
  secret-key: some_base64_encoded_jibberish 
```

More to come, but we've gotten postgres to run under kubernetes and the start of a backend api layer to make use of it....






