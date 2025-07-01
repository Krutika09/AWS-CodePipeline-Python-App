
# 🚀 AWS CodePipeline for Python App (Push to DockerHub)

This project demonstrates how to build a Python app using AWS CodeBuild and push the Docker image to DockerHub **securely using AWS SSM Parameter Store** — without hardcoding credentials.

---

## 📂 Repository

GitHub Repo:  
[https://github.com/Krutika09/AWS-CodePipeline-Python-App.git](https://github.com/Krutika09/AWS-CodePipeline-Python-App.git)

---

## 🧱 CodeBuild Project Setup

### 1️⃣ Create CodeBuild Project

- **Project Name**: `AWS-CI-Python-App`
- **Source Provider**: GitHub
- **Repository**: Your GitHub account
- **Git Repo URL**:  
  `https://github.com/Krutika09/AWS-CodePipeline-Python-App.git`

---

### 2️⃣ Environment Configuration

- **Provisioning Model**: On-demand
- **Environment Image**: Managed image
- **Compute Type**: EC2
- **Operating System**: Ubuntu
- **Runtime**: Standard
- **Image Version**: Always use the latest image
- **Service Role**: Create a new role (AWS will generate one automatically)

---

### 3️⃣ Buildspec Configuration

- Under **Buildspec**, click on **"Switch to editor"**
- Paste your build commands in YAML format

---

## 🔐 Secure DockerHub Credentials Using AWS SSM

Avoid hardcoding DockerHub credentials in your source code.

### 👣 Steps:

1. Go to **AWS Systems Manager → Parameter Store**
2. Create the following parameters:
   - `/pyapp/docker-credential/username`
   - `/pyapp/docker-credential/password`
   - `/pyapp/docker-registry/docker_url`
3. Set them as **SecureString**

---

## ❌ Common Error

```

AccessDeniedException: User ... is not authorized to perform: ssm\:GetParameters on resource ...

````

This happens because **CodeBuild role** doesn't have permission to read parameters.

---

## ✅ Solution: Attach IAM Role with SSM Access

### Step-by-step:

1. Go to **IAM → Roles**
2. Create new role or edit existing:
   - **Trusted Entity**: AWS Service
   - **Use Case**: CodeBuild
   - **Policy**: Attach `AmazonSSMFullAccess` policy (or create custom least-privilege policy)
3. Role Name: `AWS-CI-Python-Proj`
4. Attach the role to your CodeBuild project manually if needed

---

## ✅ Custom Inline Policy (Recommended)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ssm:GetParameters",
      "Resource": "arn:aws:ssm:us-west-2:050752610886:parameter/pyapp/docker-credential/*"
    }
  ]
}
````

---

## 📦 Build Process Summary

1. Clone source code from GitHub
2. Build Docker image from `Dockerfile`
3. Fetch DockerHub credentials from Parameter Store
4. Authenticate Docker CLI to DockerHub
5. Push the image to DockerHub

---

## ✅ Status

* [x] GitHub Repo Connected
* [x] SSM Parameters Created
* [x] IAM Role with Proper Access
* [ ] Build Successful

















