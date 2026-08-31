from pathlib import Path
import re
import string

from gensim.corpora import Dictionary
from gensim.models import LdaModel

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"

STOPWORDS = set("a about above after again against all am an and any are as at be because been before being below between both but by can could did do does doing down during each few for from further had has have having he her here hers herself him himself his how i if in into is it its itself just me more most my myself no nor not of off on once only or other our ours ourselves out over own same she should so some such than that the their theirs them themselves then there these they this those through to too under until up very was we were what when where which while who whom why will with would you your yours yourself yourselves".split())


def clean_text(text: str):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", " ", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = re.findall(r"[a-z]{3,}", text)
    return [token for token in tokens if token not in STOPWORDS]


def load_model():
    model_path = MODEL_DIR / "lda_model.gensim"
    dictionary_path = MODEL_DIR / "news_dictionary.gensim"
    if not model_path.exists() or not dictionary_path.exists():
        raise FileNotFoundError("Model files are missing. Run notebook 03_lda_topic_modeling.ipynb first.")
    return LdaModel.load(str(model_path)), Dictionary.load(str(dictionary_path))


def infer_topics(text: str, top_n: int = 5):
    model, dictionary = load_model()
    bow = dictionary.doc2bow(clean_text(text))
    if not bow:
        return []
    distribution = model.get_document_topics(bow, minimum_probability=0)
    distribution.sort(key=lambda item: item[1], reverse=True)
    return [
        {
            "topic_id": int(topic_id) + 1,
            "probability": round(float(probability) * 100, 2),
            "keywords": [word for word, _ in model.show_topic(topic_id, topn=7)],
        }
        for topic_id, probability in distribution[:top_n]
    ]
