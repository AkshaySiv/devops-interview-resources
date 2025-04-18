# AWS Interview Questions

This document contains AWS-related interview questions that I encountered during interviews.

### **Question 1**

Imagine a simple Python or Flask application representing a REST service. This service accesses S3, where 500,000 document fragments are stored. It receives a document bookmark as a path parameter, retrieves the corresponding fragments from S3, assembles them into a final JSON document, and returns it.

The service operates at S3's speed with minimal CPU overhead for document assembly. What are the possible deployment options for this service using AWS built-in services?

#### **Answer**

1. **AWS Lambda with API Gateway**: Use AWS Lambda to host the Python/Flask logic and API Gateway to expose the REST endpoint. This is cost-effective and scales automatically.

2. **Amazon ECS/Fargate**: Deploy the application in a containerized environment using ECS with Fargate for serverless container management.

3. **AWS Elastic Beanstalk**: Use Elastic Beanstalk to deploy and manage the Flask application with minimal operational overhead.

4. **Amazon EC2**: Deploy the application on EC2 instances for full control over the environment, though this requires more management effort.

5. **AWS App Runner**: Use App Runner for a fully managed service to deploy and scale the application without managing infrastructure.

### **Question 2**

What AWS resources are needed to host the application without using EC2 instances or ECS containers, ensuring high availability, scalability, and consistent results across North America and Europe?

#### **Answer**

1. **AWS Lambda**: Deploy the Python/Flask application as a serverless function. Configure memory, timeout, and concurrency limits to handle peak loads.

2. **Amazon API Gateway**: Expose the REST endpoints. Configure regional endpoints for North America and Europe, and enable caching for frequently accessed bookmarks.

3. **Amazon S3**: Store document fragments. Use S3 Transfer Acceleration for faster access across regions.

4. **Amazon CloudFront**: Distribute API responses globally with low latency. Configure caching policies to ensure consistent results.

5. **Amazon DynamoDB (Optional)**: Use DynamoDB for metadata storage or caching document assembly results for faster retrieval.

6. **AWS IAM**: Create roles and policies for Lambda to access S3 and other services securely. Use least privilege principles.

7. **Amazon Route 53**: Set up a global DNS with latency-based routing to direct users to the nearest API Gateway endpoint.

8. **AWS CloudWatch**: Monitor Lambda performance, API Gateway metrics, and S3 access logs. Set up alarms for anomalies.

#### **Configuration Details**
- **Lambda**: Enable provisioned concurrency for consistent performance.
- **API Gateway**: Enable throttling and request validation.
- **S3**: Use lifecycle policies to manage storage costs.
- **CloudFront**: Set TTL for caching based on document update frequency.
- **IAM**: Use managed policies for simplicity and security.

This setup ensures high availability, scalability, and consistent results across regions.

### **Question 3**

You have generated or been given AWS secrets or AWS access keys to use during your development, such as using the AWS CLI or testing your code that interacts with AWS services. How would you safely manage these AWS keys in your development environment?

#### **Answer**

1. **Environment Variables**: Store AWS access keys in environment variables to avoid hardcoding them in your application code. Use tools like `dotenv` to manage these variables in local development.

2. **AWS IAM Roles**: When running applications on AWS services like EC2, Lambda, or ECS, use IAM roles with temporary credentials instead of hardcoding access keys.

3. **AWS Secrets Manager**: Use AWS Secrets Manager to securely store and retrieve AWS access keys programmatically. This ensures keys are encrypted and access is controlled.

4. **AWS CLI Configuration**: Use the `aws configure` command to store access keys in the `~/.aws/credentials` file. Ensure the file has proper permissions to prevent unauthorized access.

5. **Version Control Exclusion**: Add sensitive files (e.g., `.env` or credentials files) to `.gitignore` to prevent accidental commits to version control systems like Git.

6. **Key Rotation**: Regularly rotate AWS access keys and remove unused keys to minimize security risks. Automate this process where possible.

7. **Access Control**: Apply the principle of least privilege by restricting IAM policies associated with the keys to only the permissions required for the task.

8. **Audit and Monitoring**: Enable AWS CloudTrail to monitor the usage of access keys and detect any unauthorized or suspicious activity.

By implementing these practices, you can ensure the secure management of AWS access keys in your development environment.
