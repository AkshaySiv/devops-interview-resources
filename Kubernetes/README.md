# Kubernetes Interview Questions

This document contains Kubernetes-related interview questions that I encountered during interviews.

-------------------------------------------------
### **Question**

Explain the entire flow when running `kubetl get pods` commands and architecture

How kubectl ensure authentication to cluster

How pods are getting scheduled to a worker node

-------------------------------------------------

### **Question 1** 

Write a Kubernetes Deployment manifest for an application named solution that meets the following requirements:

Deploy 3 replicas of the application.

The pods must be labeled with app: solution.

Use the container image hub.example.com/shop-backend:1.0.0.

Expose container port 3000.

Configure a liveness probe to check /healthz on port 3000 with an initial delay of 10 seconds.

Configure a readiness probe to check / on port 3000, with an initial delay of 10 seconds, a period of 1 second between checks, and a failure threshold of 2

### **Answer:**

```bash
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: solution
spec:
  replicas: 3
  selector:
    matchLabels:
      app: solution
  template:
    metadata:
      labels:
        app: solution
    spec:
      containers:
      - name: solution-container
        image: hub.example.com/shop-backend:1.0.0
        ports: 
        - containerPort: 3000
        livenessProbe:
          httpGet:
            path: /healthz
            port: 3000
          initialDelaySeconds: 10
        readinessProbe: 
          httpGet:
            path: /
            port: 3000
          initialDelaySeconds: 10
          periodSeconds: 1
          failureThreshold: 2
```


