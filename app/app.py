from flask import Flask, render_template, request
from topic_model import infer_topics

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    article, topics, error = "", [], None
    if request.method == "POST":
        article = request.form.get("article", "").strip()
        if len(article) < 30:
            error = "Please enter at least 30 characters of news text."
        else:
            try:
                topics = infer_topics(article)
                if not topics:
                    error = "The article did not contain enough vocabulary known by the model."
            except FileNotFoundError as exc:
                error = str(exc)
            except Exception as exc:
                error = f"Unable to analyze the article: {exc}"
    return render_template("index.html", article=article, topics=topics, error=error)


if __name__ == "__main__":
    app.run(debug=True)
