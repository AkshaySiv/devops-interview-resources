### **Question 1**  

Create a resource block in two different regions with the same provider (e.g., AWS), 

### **Answer (Brief):**

you can configure multiple provider aliases and use them in your resource blocks. Here's an example:

```hcl
# Define the default provider configuration
provider "aws" {
    region = "us-east-1"
}

# Define an additional provider configuration with an alias
provider "aws" {
    alias  = "us-west"
    region = "us-west-2"
}

# Resource in the default region (us-east-1)
resource "aws_instance" "example_east" {
    ami           = "ami-0c55b159cbfafe1f0"
    instance_type = "t2.micro"
}

# Resource in the aliased region (us-west-2)
resource "aws_instance" "example_west" {
    provider      = aws.us-west
    ami           = "ami-0c55b159cbfafe1f0"
    instance_type = "t2.micro"
}
```

In this example:
- The default provider is used for resources in `us-east-1`.
- The aliased provider (`aws.us-west`) is used for resources in `us-west-2`.
- Use the `provider` argument in the resource block to specify the provider alias.

### **Question 2**  

What is the use case of the `terraform show` command?

### **Answer (Brief):**

The `terraform show` command is used to display the state or plan file in a human-readable format. It helps you understand the current infrastructure state or the changes that will be applied.

#### Use Cases:
1. **Inspecting State**:  
    View the current state of your infrastructure to verify resources and their attributes.

    ```bash
    terraform show
    ```

2. **Reviewing Plan Output**:  
    Display the details of a saved plan file to understand the proposed changes.

    ```bash
    terraform show plan.out
    ```

3. **Debugging**:  
    Useful for debugging issues by examining the state or plan file in detail.

#### Example:
```bash
terraform plan -out=plan.out
terraform show plan.out
```

In this example:
- The `terraform plan` command generates a plan file (`plan.out`).
- The `terraform show` command displays the contents of the plan file in a readable format.