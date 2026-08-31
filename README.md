# Topic Modeling on News Articles

An interview-ready unsupervised NLP project using **Latent Dirichlet Allocation (LDA)** with **Gensim** to discover hidden topics in a large news corpus.

## What this project demonstrates

- Open-source AG News dataset
- Text cleaning and tokenization
- Exploratory data analysis
- Gensim Dictionary and Bag-of-Words
- LDA topic modeling
- Coherence-based topic-count selection
- Topic interpretation
- Document-topic probability distributions
- Saved model artifacts
- Flask web application for unseen articles

## Dataset

This project uses the **AG News** dataset via Hugging Face `datasets`. It contains news articles associated with four reference categories: World, Sports, Business, and Sci/Tech.

The labels are **not used to train LDA**. They are used only for exploration and interpretation so that the core modeling task remains unsupervised.

## Repository Structure

```text
topic-modeling-news-articles/
├── app/
│   ├── app.py
│   ├── topic_model.py
│   ├── templates/index.html
│   └── static/style.css
├── data/README.md
├── models/README.md
├── notebooks/
│   ├── 01_data_collection_preprocessing.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   ├── 03_lda_topic_modeling.ipynb
│   └── 04_topic_analysis.ipynb
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── requirements.txt
└── run_app.bat
```

## Workflow

```text
AG News → preprocessing → vocabulary filtering → Gensim BoW → LDA
        → coherence evaluation → topic interpretation → saved model
        → Flask → new article → topic probabilities
```

## Installation

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install packages:

```bash
pip install -r requirements.txt
```

## Run the notebooks

Start Jupyter:

```bash
jupyter notebook
```

Run in order:

1. `01_data_collection_preprocessing.ipynb`
2. `02_exploratory_analysis.ipynb`
3. `03_lda_topic_modeling.ipynb`
4. `04_topic_analysis.ipynb`

Notebook 03 creates:

```text
models/lda_model.gensim
models/news_dictionary.gensim
```

## Run the Flask application

From the project root:

```bash
python app/app.py
```

Open `http://127.0.0.1:5000` in your browser.

Paste a news article and the app will show the strongest topics and their keywords.

## Interview Talking Points

### Why LDA?

LDA is an unsupervised probabilistic model that represents documents as mixtures of topics and topics as mixtures of words. It is useful for discovering themes without manually labeling a corpus.

### Why Gensim?

Gensim provides practical implementations of topic modeling and convenient tools for dictionaries, Bag-of-Words corpora, topic inspection, and model persistence.

### How was the number of topics selected?

Several candidate topic counts are compared using `C_v` coherence. The score is treated as a guide and the resulting topic keywords are inspected manually for semantic quality.

### Why are AG News labels not used?

Using labels to train the model would turn this into a supervised classification problem. LDA is intentionally trained without them.

### What does the Flask app add?

It demonstrates deployment of the trained NLP pipeline: unseen text is cleaned, mapped into the saved vocabulary, and passed to the saved LDA model to obtain a topic mixture.

## Limitations

- LDA ignores word order.
- Results depend on preprocessing and topic count.
- Topic names require human interpretation.
- This Flask app is a portfolio demonstration, not a production-scale service.

## Future Improvements

- Add bigram/trigram detection.
- Compare LDA with NMF and BERTopic.
- Add pyLDAvis.
- Add model versioning.
- Use a larger corpus.
- Add automated topic summaries.

## Author

**Vivek Kumar Sahu**

GitHub: https://github.com/InfinitePraveen

LinkedIn: https://www.linkedin.com/in/infinitepraveen/

## License

MIT License.
