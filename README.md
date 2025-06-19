#   Human-Centric Learning Analytics

This project explores how data and AI can be used to enhance human learning, focusing on analytics that respect individual learners' contexts, behaviors, and goals.

## Project Overview

We aim to build a human-centric learning analytics platform that enables:

-  Personalized tracking of learning progress
-  Context-aware insights (e.g., attention span, engagement)
-  Ethical use of AI to support—not replace—human judgment

## 🧱 Project Structure

```bash
.
├── dashboards/ # Power BI or Streamlit dashboards for educators
├── data/ # Raw, cleaned, and processed datasets
├── dbt/ # Data transformation scripts with dbt
├── docs/ # Documentation and design notes
├── notebooks/ # Jupyter notebooks (EDA, modeling, etc.)
├── src/ # Source code (ETL, ML, APIs, etc.)
├── tests/ # Unit and integration tests
└── README.md
```

## 📦 Tech Stack

- **Python** (Pandas, scikit-learn, etc.)
- **Jupyter** for interactive exploration
- **DBT** for data transformation
- **Streamlit / Power BI** for dashboards
- **Git + GitHub** for version control

## 📊 Features (WIP)

- [ ] Automated data pipeline
- [ ] Learner profiling (unsupervised ML)
- [ ] Engagement prediction
- [ ] Interactive dashboard with insights

## 📁 How to Run

1. Clone this repo:

```bash

   git clone https://github.com/LynaBouikni/human-centric-learning-analytics.git
   cd human-centric-learning-analytics

```
2. Create a virtual environment:
```bash

   conda create -n hcla python=3.10
   conda activate hcla
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Launch Jupyter:

```bash
jupyter lab
```

🙋‍♀️ Author
Lyna Bouikni
AI & Cognitive Science | ENS, Dauphine, Mines Paris
LinkedIn | GitHub

📜 License
MIT License – see the LICENSE file for details.
