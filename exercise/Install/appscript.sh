#!/bin/bash

# Set the namespace for the deployment
NAMESPACE="my-app"

# Create a Kind cluster
kind create cluster --name my-cluster

# Install the kube-prometheus-stack chart to deploy Prometheus
kubectl create namespace monitoring
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus prometheus-community/kube-prometheus-stack -n monitoring

# Build and package the application Helm chart
cd ../Helm
helm package .

# Install the application Helm chart
cd ..
helm install my-app app/my-app-0.1.0.tgz -n $NAMESPACE