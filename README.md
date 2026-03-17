# 🚀 Serverless Performance Research

📄 **Research Paper:** [An Empirical Study of Serverless Performance](./research_paper.pdf)

---

## 📌 Overview
A comprehensive study of **serverless computing performance** using **Google Cloud Run**, focusing on latency, cold starts, container image size, concurrency, autoscaling, and regional impact.

This project benchmarks key performance characteristics through structured experiments:

- Cold Start Latency  
- Image Size vs Startup Time  
- Concurrency Impact on Latency  
- Autoscaling Behavior  
- Regional Latency Differences  

All experiments are reproducible using Python-based clients and containerized services.

---

## 🧱 Project Structure

    serverless-performance-research/
    │
    ├── experiments/
    │   ├── exp1_cold_start_latency/
    │   ├── exp2_image_size_vs_startup/
    │   ├── exp3_concurrency_latency/
    │   ├── exp4_autoscaling_saturation/
    │   ├── exp5_region_latency/
    │
    ├── README.md
    └── research_paper.pdf

---

## ⚙️ System Setup

- **Platform:** Google Cloud Run  
- **Language:** Python  
- **Framework:** Flask / FastAPI  
- **Load Testing:** Async Python (aiohttp / requests)  
- **Containerization:** Docker  

---

## 🚀 How to Run (IMPORTANT)

👉 **Run ALL commands from the ROOT directory (`serverless-performance-research/`)**

### Deploying Services
Each experiment contains an `app/` directory with Docker configuration and deployment setup.

---

### Running Client Benchmarks
Each experiment contains a `client/` directory with test scripts.

Run them from the root directory like this:

    python experiments/<experiment_name>/client/test.py

> ⚠️ Make sure to update the deployed service URL inside the test scripts before running  

---

## 📊 Experiments

---

### 🧪 Experiment 1: Cold Start Latency
Measures the response time of the first request after a service instance is created or scaled from zero.

---

### 🧪 Experiment 2: Image Size vs Startup Time
Analyzes how increasing container image size impacts service startup time and cold start latency.

---

### 🧪 Experiment 3: Concurrency vs Latency
Analyzes how increasing the number of concurrent requests impacts overall response latency.

---

### 🧪 Experiment 4: Autoscaling Saturation
Examines system behavior under heavy load and identifies saturation points where performance degrades.

---

### 🧪 Experiment 5: Regional Latency
Compares response times across different deployment regions to evaluate the impact of geographical distance.

---

## 🧠 Key Takeaways
- Cold starts introduce noticeable latency overhead  
- Larger container images increase startup time  
- Increasing concurrency leads to higher response times  
- Autoscaling can hit saturation under heavy load  
- Deployment region significantly affects performance  

---

## 🤝 Contributions
Contributions, improvements, and new experiments are welcome.

---

## 📜 License
MIT License