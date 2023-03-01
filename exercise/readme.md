# Helm Chart README
This Helm chart deploys a Kubernetes Deployment for a containerized application. The chart creates a deployment with specified number of replicas and mounts a persistent volume claim for the container's uploads directory.

## Prerequisites
A running Kubernetes cluster
Helm 3.x installed on your machine

## Installation
Clone the repository and navigate to the chart directory
Customize the chart's values in values.yaml
Install the chart with the following command:
```bash
helm install <release-name> .
```

## Configuration
The following table lists the configurable parameters of the chart and their default values.

| Parameter  | Description | Description |
| ------------- | ------------- | ------------- |
| `replicaCount`  | 	Number of replicas to deploy  | `1`  |
| `image.repository` | Container image repository | `nginx` |
| `image.tag`  | Container image tag  | `latest` |
| `image.pullPolicy` | 	Image pull policy  | 	`IfNotPresent`  |
| `image.pullSecrets` | Name of the secret containing container registry credentials  | `[]` |
| `podAnnotations`  | Annotations to add to the pod  | `{}`  |
| `port` | Container port to expose | `80`|
| `resources` | Container port to expose | `80`|
| `Resource limits and requests for the container` | Container port to expose | `{}`|
| `nodeSelector	` | Node labels for pod assignment | `{}`|
| `tolerations` | List of node taints to tolerate | `[]`|
| `affinity	` | Affinity settings for pod scheduling | `{}`|
| `fullnameOverride` | Override the deployment name | `""`|
| `toleratserviceAccountName` | Name of the service account used by the pod | `default`|

## License

This chart is licensed under the MIT License.