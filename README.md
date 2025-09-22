Absolutely! Based on the detailed project flow you provided, here’s a **professional, recruiter-friendly README** for your GitHub repo. I’ve structured it to be clear, comprehensive, and impressive, highlighting technical skills, project workflow, and deployment pipeline.

---

# Vehicle Insurance Prediction & Deployment Project 🚗💡

**Author:** Sanvith
**Tech Stack:** Python, FastAPI, MongoDB, AWS (S3, EC2, ECR), Docker, CI/CD, Data Engineering, MLOps

---

## Project Overview

This project is a **full-stack MLOps pipeline** for predicting vehicle insurance, including data ingestion, validation, transformation, model training, evaluation, deployment, and CI/CD integration. The project emphasizes production-ready practices, including:

* Modular and scalable project structure
* Logging, exception handling, and configuration management
* Cloud-based data storage and model management (MongoDB Atlas & AWS S3)
* Dockerized application with automated CI/CD pipeline on GitHub Actions
* Deployment on AWS EC2 with a web application interface

---

## Table of Contents

1. [Project Structure](#project-structure)
2. [Setup & Installation](#setup--installation)
3. [MongoDB Integration](#mongodb-integration)
4. [Data Processing Pipeline](#data-processing-pipeline)
5. [AWS & Cloud Integration](#aws--cloud-integration)
6. [Model Evaluation & Deployment](#model-evaluation--deployment)
7. [CI/CD & Docker Setup](#cicd--docker-setup)
8. [Launching the Application](#launching-the-application)
9. [Contributing](#contributing)
10. [License](#license)

---

## Project Structure

```text
vehicle-insurance-prediction/
│
├── src/                       # Source code
│   ├── components/            # Pipeline components (data_ingestion, transformation, trainer, evaluator)
│   ├── configuration/         # MongoDB & AWS configuration
│   ├── entity/                # Data & artifact classes, estimator classes
│   ├── utils/                 # Logger, exceptions, helper functions
│   └── aws_storage/           # AWS S3 integration
│
├── notebook/                  # EDA, feature engineering, and MongoDB demos
├── static/                    # Frontend static files
├── template/                  # HTML templates for web app
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker image definition
├── dockerignore               # Docker ignore file
├── pyproject.toml             # Local package setup
├── setup.py                   # Project installation setup
└── README.md                  # Project documentation
```

---

## Setup & Installation

### 1. Create Project Template

```bash
python template.py
```

### 2. Install Local Packages

Update `setup.py` and `pyproject.toml` to import local packages. Refer to `crashcourse.txt` for guidance.

### 3. Create Virtual Environment

```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
pip list
```

---

## MongoDB Integration

1. Sign up for **MongoDB Atlas** and create a cluster (M0 free tier).
2. Create a database user and allow access from all IPs (`0.0.0.0/0`).
3. Get your **connection string** and save it as an environment variable:

**Bash:**

```bash
export MONGODB_URL="mongodb+srv://<username>:<password>@cluster.mongodb.net/dbname"
```

**PowerShell:**

```powershell
$env:MONGODB_URL="mongodb+srv://<username>:<password>@cluster.mongodb.net/dbname"
```

4. Push dataset from `notebook/mongoDB_demo.ipynb` to MongoDB and verify in Atlas.

---

## Data Processing Pipeline

The pipeline is divided into modular components:

1. **Data Ingestion**: Fetches data from MongoDB, converts to Pandas DataFrame, and stores artifacts.
2. **Data Validation**: Validates schema, checks missing values, and ensures dataset integrity (`config/schema.yaml`).
3. **Data Transformation**: Feature engineering and transformation using `estimator.py`.
4. **Model Training**: Train models, store metrics, and save artifacts.
5. **Model Evaluation**: Evaluate models against previous versions using threshold scoring (`MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE`).
6. **Prediction Pipeline**: Combine all components into an inference-ready pipeline.

---

## AWS & Cloud Integration

* AWS Services Used: **S3**, **EC2**, **ECR**
* Steps:

  1. Create IAM users for S3 and CI/CD access.
  2. Set environment variables for AWS credentials.
  3. Configure S3 bucket for model storage (`MODEL_BUCKET_NAME` = `my-model-mlopsproj`).
  4. Implement S3 utilities in `src/aws_storage` for model pull/push.
  5. Launch EC2 instance with Docker installed for deployment.

---

## Model Evaluation & Deployment

* **Model Evaluation** compares new vs old models and decides if the new model should be pushed to production.
* **Model Pusher** uploads the trained model to **AWS S3**.
* Prediction API built using **FastAPI** (`app.py`), serving endpoints for:

  * `/predict` : Make predictions
  * `/training` : Trigger model training

---

## CI/CD & Docker Setup

* Dockerize the application:

```bash
docker build -t vehicleproj .
docker run -d -p 5080:5000 vehicleproj
```

* GitHub Actions pipeline automates:

  * Docker image build
  * Push to **AWS ECR**
  * Deployment on **EC2 self-hosted runner**

* Required GitHub secrets:

  * `AWS_ACCESS_KEY_ID`
  * `AWS_SECRET_ACCESS_KEY`
  * `AWS_DEFAULT_REGION`
  * `ECR_REPO`

---

## Launching the Application

1. Open EC2 instance in the browser and ensure port 5080 is open in Security Groups.
2. Access app:

```
http://<EC2_PUBLIC_IP>:5080
```

3. Use `/training` to train models or `/predict` to get predictions.

---

## Contributing

Contributions are welcome! Please follow the below steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature-name`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License.

---


