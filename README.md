# MLops Project

This repository contains the code and setup for a simplified MLops pipeline for a basic machine learning project. The goal is to demonstrate version control, automation, and monitoring for your machine learning model. 

## Project Overview
 

- **Step 1: Docker Containerization**
  - Built a Dockerfile for the  model and it's dependencies.

  - Built a Docker image from the Dockerfile:
   ` docker build -t rkvishnu77/mlops_modal . `

  - Pushing the Docker image to  the Dockerhub with 

   ` docker tag rkvishnu77/mlops_modal:latest rkvishnu77/mlops_modal `
   ` docker push rkvishnu77/mlops_modal:latest `


- **Step 2: Cloud Deployment**
  - Created an AWS EC2 instance to deploy the app on CLoud Server with docker
  - Provide the endpoint or URL where your model can be accessed (e.g., an AWS EC2 instance or an Azure App Service).

- **Step 4: Automated Testing**
  - Write unit tests for your machine learning code.
  - Set up a continuous integration (CI) pipeline using a service like Travis CI, GitLab CI, or CircleCI to run your tests automatically on every push.
  - Document the testing process and results in this README.md file.

- **Step 5: Monitoring and Logging** (Optional)
  - Implement Prometheus and Grafana for monitoring and visualizing the performance of your deployed model.
  - Document the monitoring setup in this README.md file.

## Getting Started

### Prerequisites

Before getting started, ensure that you have the following tools and services set up:

- Git
- Docker
- A cloud platform account (e.g., AWS, Azure, GCP)
- A CI/CD service account (e.g., Travis CI, GitLab CI, CircleCI)

### Running the Project

Follow these steps to set up and run the project:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/mlops-project.git
