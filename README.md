## **Client-App README**

```markdown
# FYP Client App

This repository contains the client-side application for the DevOps Capstone Project. 
It connects to the server application, retrieves the file, and verifies its integrity. Containerized with Docker and deployed on AWS EC2 using Terraform.

---

## **Prerequisites**

- Git
- Docker & Docker Compose
- Python 3.11+
- AWS CLI configured with access key and secret
- Terraform 1.0+ installed

---

## **Repository Structure**
client-app/
 ├── app/
 │ └── client.py
 ├── terraform/
 │ ├── main.tf
 │ ├── variables.tf
 │ ├── outputs.tf
 │ └── provider.tf
 ├── docker-compose.yml
 ├── Dockerfile
 ├── requirements.txt
 └── README.md

---

## **Terraform (Infrastructure as Code)**

1. Configure AWS credentials:

```bash
aws configure
Initialize Terraform:


cd terraform
terraform init
Apply Terraform to create EC2, VPC, security groups, and subnet:


terraform apply -var="key_name=<YOUR_KEY_PAIR_NAME>"
Outputs:


client_public_ip – Public IP of the client EC2


client_private_ip – Private IP of the client EC2


vpc_id – VPC ID


Ensure security group allows TCP port 5001 (or the port client runs on) and 22 (SSH).

Docker Setup
Build and run the container:


docker-compose up --build -d
Verify the container is running:


docker ps
Access the client application:


http://<CLIENT_PUBLIC_IP>:5001
Expected output:
{"message": "Client app works. FYP ended."}

CI/CD Pipeline
The client repo is connected to GitHub Actions.
Any push to main branch will:
Build Docker image
Push it to Docker Hub
Pull the image on EC2 via self-hosted runner
Redeploy container
Send Slack notification
Monitoring (Optional)
Since the client EC2 is in the same VPC as server EC2, you can monitor metrics from the server Grafana instance.

Troubleshooting
Docker permission issues: Use sudo docker ... if permission denied.
Client not reachable: Check security groups for port 5000.
Terraform errors: Verify AWS credentials and correct key pair name.


