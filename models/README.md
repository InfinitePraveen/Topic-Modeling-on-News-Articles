# Topic Modeling on News Articles

An end-to-end **Unsupervised Natural Language Processing (NLP)** project that uses **Latent Dirichlet Allocation (LDA)** with **Gensim** to discover hidden topics across a large collection of news articles.

The project is designed as an interview-ready Data Science portfolio project. It combines exploratory analysis and topic modeling in Jupyter notebooks with a **Flask web application** that allows users to submit new news text and see the topics identified by the trained LDA model.

---

## Project Overview

**Project Name:** Topic Modeling on News Articles

**Domain:** Natural Language Processing / Unsupervised Machine Learning

**Primary Technique:** Latent Dirichlet Allocation (LDA)

**Library:** Gensim

**Dataset:** AG News

**Web Framework:** Flask

**Python Version:** **3.12.x recommended**

### Skills Demonstrated

* Natural Language Processing
* Text preprocessing
* Tokenization
* Stopword removal
* Exploratory Data Analysis
* Bag-of-Words
* Topic Modeling
* Latent Dirichlet Allocation
* Gensim
* Coherence Score
* Unsupervised Learning
* Model Persistence
* Flask
* Basic Model Deployment

---

## Project Objective

The goal of this project is to discover hidden thematic structures within a large collection of news documents without using the article categories as training labels.

For example, after training LDA, the model may discover topics related to:

```text
Topic 1 → Technology
Topic 2 → Sports
Topic 3 → Business
Topic 4 → World News
```

The topic names are assigned by interpreting the important words produced by the model. LDA itself does not know these human-readable category names.

---

# Dataset

This project uses the **AG News dataset**, a publicly available news classification dataset.

The dataset contains news articles from four reference categories:

1. World
2. Sports
3. Business
4. Sci/Tech

The dataset is downloaded automatically using the Hugging Face `datasets` library.

### Important

The category labels are **not used to train the LDA model**.

They are used only for:

* Exploratory Data Analysis
* Understanding the dataset
* Optional interpretation of discovered topics

This keeps the main modeling task **unsupervised**.

---

# Project Workflow

```text
                 AG News Dataset
                       │
                       ▼
              Data Collection
                       │
                       ▼
              Data Exploration
                       │
                       ▼
             Text Preprocessing
                       │
                       ▼
              Tokenization
                       │
                       ▼
          Stopword & Vocabulary
               Filtering
                       │
                       ▼
             Gensim Dictionary
                       │
                       ▼
              Bag-of-Words
                       │
                       ▼
              LDA Training
                       │
                       ▼
         Coherence Score Analysis
                       │
                       ▼
           Topic Interpretation
                       │
                       ▼
              Save LDA Model
                       │
                       ▼
              Flask Web App
                       │
                       ▼
             New Article Input
                       │
                       ▼
           Topic Probability
                 Distribution
```

---

# Repository Structure

```text
topic-modeling-news-articles/
│
├── app/
│   ├── app.py
│   ├── topic_model.py
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       └── style.css
│
├── data/
│   └── README.md
│
├── models/
│   └── README.md
│
├── notebooks/
│   ├── 01_data_collection_preprocessing.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   ├── 03_lda_topic_modeling.ipynb
│   └── 04_topic_analysis.ipynb
│
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── requirements.txt
└── run_app.bat
```

---

# Python Version

## Recommended Python Version

This project is developed and tested with:

```text
Python 3.12.x
```

Python **3.12 (64-bit)** is recommended for the smoothest installation of the project's scientific Python and Gensim dependencies on Windows.

Check your Python version:

```bash
python --version
```

or:

```bash
py --version
```

Expected output:

```text
Python 3.12.x
```

> **Note:** If you are using a newer Python version and Gensim attempts to compile from source, using Python 3.12 in a fresh virtual environment is recommended.

---

# Installation

There are two recommended ways to create the virtual environment.

## Method 1 — Python `venv`

### 1. Clone the repository

```bash
git clone https://github.com/InfinitePraveen/topic-modeling-news-articles.git
```

Move into the project:

```bash
cd topic-modeling-news-articles
```

### 2. Create a Python 3.12 virtual environment

Windows:

```bash
py -3.12 -m venv .venv
```

macOS/Linux:

```bash
python3.12 -m venv .venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Windows CMD:

```cmd
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 4. Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Method 2 — `virtualenv`

If you prefer the `virtualenv` package:

### 1. Install virtualenv

```bash
python -m pip install virtualenv
```

### 2. Create the environment

Windows:

```bash
python -m virtualenv .venv
```

macOS/Linux:

```bash
python3 -m virtualenv .venv
```

### 3. Activate it

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Windows CMD:

```cmd
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 4. Verify Python

```bash
python --version
```

Make sure it reports:

```text
Python 3.12.x
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Installation with uv

This project can also be installed using **uv**.

First install Python 3.12 through uv:

```bash
uv python install 3.12
```

Create the environment:

```bash
uv venv --python 3.12
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Then install the dependencies:

```bash
uv pip install -r requirements.txt
```

## Installing Gensim with uv on Windows

If `uv` attempts to build Gensim from source and produces an error similar to:

```text
Microsoft Visual C++ 14.0 or greater is required
```

install the pre-built Gensim wheel instead:

```bash
uv pip install --only-binary=:all: gensim==4.4.0
```

Then verify the installation:

```bash
python -c "import gensim; print(gensim.__version__)"
```

Expected:

```text
4.4.0
```

After Gensim is successfully installed, install the remaining dependencies:

```bash
uv pip install pandas numpy scipy matplotlib seaborn nltk datasets jupyter Flask gunicorn
```

---

# Running the Project

After activating the virtual environment, start Jupyter:

```bash
jupyter notebook
```

Run the notebooks in the following order.

### Notebook 01

```text
01_data_collection_preprocessing.ipynb
```

This notebook:

* Downloads AG News
* Inspects the dataset
* Combines article title and description
* Cleans the text
* Tokenizes documents
* Removes stopwords
* Saves the preprocessed data

---

### Notebook 02

```text
02_exploratory_analysis.ipynb
```

This notebook explores:

* Document length
* Vocabulary size
* Most frequent words
* Category distributions
* Corpus characteristics

---

### Notebook 03

```text
03_lda_topic_modeling.ipynb
```

This is the main modeling notebook.

It:

* Creates the Gensim Dictionary
* Creates the Bag-of-Words corpus
* Tests different numbers of topics
* Calculates coherence scores
* Trains the final LDA model
* Displays important words for each topic
* Saves the trained model

Generated files:

```text
models/
├── lda_model.gensim
└── news_dictionary.gensim
```

---

### Notebook 04

```text
04_topic_analysis.ipynb
```

This notebook:

* Inspects discovered topics
* Calculates dominant topics
* Visualizes topic distribution
* Examines document-topic mixtures
* Tests the model on unseen news text

---

# Running the Flask Web Application

Make sure Notebook 03 has successfully generated:

```text
models/lda_model.gensim
models/news_dictionary.gensim
```

Then run:

```bash
python app/app.py
```

You should see something similar to:

```text
* Running on http://127.0.0.1:5000
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# Web Application

The Flask application provides a simple interface where a user can paste a news article.

```text
┌──────────────────────────────────────────────┐
│              NEWS TOPIC EXPLORER             │
│                                              │
│  Paste a news article                        │
│  ┌────────────────────────────────────────┐  │
│  │                                        │  │
│  │  News article text...                  │  │
│  │                                        │  │
│  └────────────────────────────────────────┘  │
│                                              │
│           [ Discover Topics → ]              │
│                                              │
│  Topic 1                         61.42%       │
│  ───────────────────────────────             │
│  company · market · business · ...           │
│                                              │
│  Topic 4                         22.15%       │
│  ─────────────────────                       │
│  technology · software · chip · ...          │
└──────────────────────────────────────────────┘
```

The application uses the same preprocessing and Gensim dictionary used during model training.

---

# How LDA Works

Latent Dirichlet Allocation assumes that:

```text
Document = mixture of topics
Topic    = mixture of words
```

For example:

```text
Article
│
├── Technology → 70%
├── Business   → 20%
├── World      → 7%
└── Sports     → 3%
```

This probability distribution is what the Flask application displays.

---

# Choosing the Number of Topics

The project evaluates several candidate topic counts:

```python
[4, 6, 8, 10, 12]
```

For each candidate, the project calculates the `C_v` coherence score.

The final number of topics should be selected using:

1. Coherence score
2. Topic interpretability
3. Important topic words
4. Example documents

A model with a slightly lower coherence score may sometimes be more useful if its topics are substantially easier to interpret.

---

# Why Gensim?

Gensim is particularly useful for this project because it provides:

* LDA implementation
* Dictionary creation
* Bag-of-Words representation
* Topic inspection
* Coherence evaluation
* Model persistence

---

# Why Flask?

Flask was selected because the project is intended to demonstrate how a Data Science/NLP notebook can be converted into a small usable application.

The Flask application provides:

```text
User Input
     ↓
Preprocessing
     ↓
Dictionary Conversion
     ↓
LDA Inference
     ↓
Topic Probabilities
     ↓
Web Interface
```

---

# Interview Questions You Should Be Ready For

### 1. What is Topic Modeling?

Topic modeling is an unsupervised NLP technique used to discover hidden thematic structures in a collection of documents.

### 2. What is LDA?

LDA stands for **Latent Dirichlet Allocation**. It is a probabilistic generative model that represents documents as mixtures of topics and topics as distributions over words.

### 3. Why is LDA unsupervised?

Because the model does not require predefined topic labels during training.

### 4. Why did you use AG News?

AG News is a well-known news corpus with diverse articles and broad reference categories, making it suitable for demonstrating topic discovery.

### 5. Why didn't you use the labels?

Using the labels to train the model would make the task supervised. The purpose of this project is topic discovery.

### 6. How did you choose the number of topics?

I compared multiple candidate topic counts using `C_v` coherence and then inspected the resulting topics for semantic interpretability.

### 7. What is a Bag-of-Words model?

It represents a document using word occurrence information while ignoring word order.

### 8. What are the limitations of LDA?

Important limitations include:

* It ignores word order.
* It requires choosing the number of topics.
* Results depend heavily on preprocessing.
* Topics can sometimes be difficult to interpret.
* Rare or overly common words can reduce topic quality.

### 9. How does your web app work?

The submitted article is cleaned using the same preprocessing logic used during training, converted using the saved Gensim dictionary, and passed to the saved LDA model to obtain a topic probability distribution.

### 10. How would you improve this project?

Possible improvements include:

* Bigram and trigram detection
* TF-IDF-based preprocessing experiments
* NMF comparison
* BERTopic comparison
* Transformer-based embeddings
* pyLDAvis visualization
* Better topic naming
* Larger news datasets
* Model monitoring

---

# Limitations

This project is primarily an educational and portfolio implementation.

LDA has several limitations:

* It does not understand word order.
* It does not understand context as modern transformer models do.
* Topic interpretation requires human judgment.
* The number of topics must be selected.
* Results can change with preprocessing and model parameters.

The Flask application is intended as a demonstration and is not configured as a production-scale NLP service.

---

# Future Improvements

Potential future versions could include:

* **NMF** topic modeling
* **BERTopic**
* Sentence embeddings
* Transformer-based topic representations
* Interactive topic visualization
* Topic naming
* Topic search
* Batch document analysis
* REST API
* Docker deployment
* Cloud deployment
* Model versioning

---

# Technologies Used

| Technology            | Purpose               |
| --------------------- | --------------------- |
| Python 3.12           | Programming language  |
| Pandas                | Data manipulation     |
| NumPy                 | Numerical computing   |
| Gensim                | LDA topic modeling    |
| SciPy                 | Scientific computing  |
| Matplotlib            | Visualization         |
| Seaborn               | Visualization         |
| Hugging Face Datasets | Dataset loading       |
| Jupyter Notebook      | Data Science workflow |
| Flask                 | Web application       |
| HTML                  | Web interface         |
| CSS                   | Web styling           |

---

# Author

## Praveen Kumar

### GitHub

https://github.com/InfinitePraveen

### LinkedIn

https://www.linkedin.com/in/infinitepraveen/

---

# Contributing

Contributions are welcome.

Please read:

```text
CONTRIBUTING.md
```

before submitting a pull request.

---

# License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

---

## Final Project Summary

This project demonstrates a complete Data Science workflow:

```text
Real Dataset
     ↓
Data Understanding
     ↓
Text Cleaning
     ↓
Exploratory Analysis
     ↓
Feature Representation
     ↓
Unsupervised Machine Learning
     ↓
LDA Topic Modeling
     ↓
Model Evaluation
     ↓
Topic Interpretation
     ↓
Model Persistence
     ↓
Flask Deployment
```

It is therefore suitable for demonstrating **NLP, unsupervised learning, Gensim, LDA, model evaluation, and basic deployment skills in Data Science interviews**.
