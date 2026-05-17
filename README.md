# 📰 Fake News Detector using Machine Learning

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikit-learn)
![NLP](https://img.shields.io/badge/NLP-NLTK-green)
![Internship](https://img.shields.io/badge/Internship-Pinnacle%20Labs-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

> 🏢 **Internship Project** — Developed as part of the **Data Science Internship** at [Pinnacle Labs](https://pinnaclelabs.tech/internship/)

A machine learning web application that classifies news articles as **Real** or **Fake** using NLP, TF-IDF vectorization, and a trained classifier — built with Python & Streamlit.

---

## 🏢 About the Internship

This project was built as a task assigned during the **Data Science Internship** at **Pinnacle Labs**.

| Detail | Info |
|---|---|
| 🏛️ Organization | [Pinnacle Labs](https://pinnaclelabs.tech/internship/) |
| 💼 Domain | Data Science |
| 📌 Project | Fake News Detector |
| 🛠️ Tech Used | Python, NLP, Machine Learning, Streamlit |

Pinnacle Labs offers internship programs across domains like Data Science, AI, Python Development, Web Development, and more — providing students hands-on real-world project experience.

---

## 📌 Table of Contents

- [What Does It Do?](#-what-does-it-do)
- [Who Uses It?](#-who-uses-it)
- [Real-World Impact](#-real-world-impact)
- [Project Structure](#-project-structure)
- [Dataset](#-dataset)
- [Tech Stack](#-tech-stack)
- [How It Works](#-how-it-works)
- [Installation & Setup](#-installation--setup)
- [Screenshots](#-screenshots)
- [Challenges Faced & Solutions](#-challenges-faced--solutions)
- [Future Improvements](#-future-improvements)

---

## 🤔 What Does It Do?

The **Fake News Detector** is an NLP-powered web application that analyzes a news headline or article excerpt and predicts whether it is **Real News ✅** or **Fake News ❌**.

Key capabilities:
- Accepts raw news text as input (headline or full article excerpt)
- Preprocesses the text using NLP techniques — stopword removal & Porter Stemming
- Transforms text into numerical features using **TF-IDF Vectorization**
- Classifies the news using a pre-trained **Machine Learning model**
- Displays the result instantly via a clean, interactive Streamlit web interface

---

## 👥 Who Uses It?

| User Group | Use Case |
|---|---|
| 🧑‍🎓 Students & Researchers | Learning NLP and ML classification pipelines |
| 📰 Journalists & Fact-Checkers | Quick first-pass check on suspicious news |
| 🌐 General Public | Verify news before sharing on social media |
| 🏫 Educators | Demonstrate applied ML in the classroom |
| 🏢 Media & Tech Companies | Prototype for automated content moderation |

---

## 🌍 Real-World Impact

Misinformation and fake news is one of the most critical challenges of the digital age. This project addresses that directly:

- **Reducing Misinformation Spread** — Helps users identify potentially fabricated stories before sharing, cutting down viral spread of false information across social media.
- **Supporting Fact-Checkers** — Acts as an automated first-pass filter so human fact-checkers can prioritize the most suspicious content, saving time and effort.
- **Protecting Democracy** — Political fake news influences elections and public opinion. A detection tool empowers voters to make more informed decisions.
- **Improving Media Literacy** — Helps users understand *why* certain writing patterns are linked to fake news, building critical digital literacy skills.
- **Foundation for Production Systems** — Serves as a proof-of-concept that can be scaled into larger content moderation pipelines for social media platforms and news aggregators.

---

## 📁 Project Structure

```
fake-news-detector/
│
├── app.py                  # Streamlit web application (main entry point)
├── fake_news.ipynb         # Jupyter Notebook — EDA, model training & evaluation
│
├── model.pkl               # Trained ML classifier (serialized with joblib)
├── vector.pkl              # Fitted TF-IDF Vectorizer (serialized with joblib)
│
├── True.csv                # Dataset: Real verified news articles
├── Fake.csv                # Dataset: Fabricated / fake news articles
│
└── README.md               # Project documentation
```

---

## 📊 Dataset

This project uses the **Fake News Detection Dataset** from Kaggle.

🔗 **Dataset Link:** [https://www.kaggle.com/code/therealsampat/fake-news-detection/input](https://www.kaggle.com/code/therealsampat/fake-news-detection/input)

| File | Description | Records (approx.) |
|---|---|---|
| `True.csv` | Real, verified news articles | ~21,417 |
| `Fake.csv` | Fabricated / fake news articles | ~23,481 |

**Columns used:** `title`, `text`, `subject`, `date`

Both files were merged and labeled (`1 = Real`, `0 = Fake`) to create the final training dataset used to train the ML model.

---

## 🛠 Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.8+ | Core programming language |
| Streamlit | Interactive web application frontend |
| scikit-learn | ML model training & TF-IDF vectorization |
| NLTK | NLP preprocessing (stopwords, Porter Stemming) |
| pandas | Data loading and manipulation |
| joblib | Model serialization (saving/loading `.pkl` files) |
| Jupyter Notebook | EDA, model training & evaluation |

---

## ⚙️ How It Works

```
User Input (raw news text)
        │
        ▼
  ┌──────────────────────────────────┐
  │        Text Preprocessing        │
  │  1. Remove non-alphabetic chars  │
  │  2. Lowercase all words          │
  │  3. Remove English stopwords     │
  │  4. Apply Porter Stemming        │
  └──────────────────────────────────┘
        │
        ▼
  TF-IDF Vectorization  ← vector.pkl
        │
        ▼
  ML Model Prediction   ← model.pkl
        │
        ▼
  ✅ Real News  OR  ❌ Fake News
```

---

## 💻 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/fake-news-detector.git
cd fake-news-detector
```

### 2. Install dependencies
```bash
pip install streamlit scikit-learn nltk pandas joblib
```

### 3. Run the app
```bash
python -m streamlit run app.py
```

### 4. Open in browser
```
Local URL:    http://localhost:8501
Network URL:  http://192.168.x.x:8501
```
<img width="1288" height="945" alt="image" src="https://github.com/user-attachments/assets/8d5dbc04-46b3-4fbe-a69e-161e72454057" />

---

> ⚠️ **Note:** Ensure `model.pkl` and `vector.pkl` are present in the same directory as `app.py` before running.

---

## 📸 Screenshots

### ✅ Real News Detected
![Real News](<img width="1444" height="840" alt="image" src="https://github.com/user-attachments/assets/220e1174-ab5d-43a0-aad9-f993a464840b" />
)

### ❌ Fake News Detected
![Fake News](<img width="1439" height="840" alt="image" src="https://github.com/user-attachments/assets/6488640d-6262-4b84-a59f-28d82f6afbf0" />
)

---

## 🧗 Challenges Faced & Solutions

### Challenge 1 — Text Preprocessing Mismatch
**Problem:** The model was trained with specific preprocessing steps (stemming + stopword removal). If the preprocessing in `app.py` didn't *exactly* match the training notebook's pipeline, the model received unexpected input and produced wrong predictions.

**Solution:** Carefully replicated the exact same `preprocess()` function from the training notebook into `app.py`. Added a comment — *"must match train_model.py exactly"* — to prevent future accidental changes to the pipeline.

---

### Challenge 2 — Saving & Loading the Vectorizer
**Problem:** Initially only the ML model was saved. At inference time, the app crashed because the model expected the same TF-IDF vocabulary it was trained on — which wasn't available without the saved vectorizer.

**Solution:** Saved both `model.pkl` and `vector.pkl` separately using `joblib.dump()` after training. Both are loaded together in the app using `@st.cache_resource` for efficiency.

---

### Challenge 3 — Slow App Startup on Every Interaction
**Problem:** Streamlit reruns the entire script on every user interaction. Without caching, the model and vectorizer were reloaded from disk on *every* button click, causing noticeable lag.

**Solution:** Wrapped the `load_model()` function with Streamlit's `@st.cache_resource` decorator, ensuring the model is loaded only *once* per session and kept in memory for all subsequent interactions.

---

### Challenge 4 — Unreliable Predictions on Very Short Input
**Problem:** When users entered only 1–3 words, the TF-IDF vector was extremely sparse, leading to inconsistent or unreliable predictions from the model.

**Solution:** Added input validation in the UI using `if not input_text.strip()` to warn users to enter meaningful text. The model performs best with full sentences or article paragraphs.

---

### Challenge 5 — Class Imbalance in Training Data
**Problem:** The dataset had a slight imbalance between the number of fake (~23K) and real (~21K) news samples, which risked biasing the model toward the majority class.

**Solution:** Evaluated the model on both accuracy and a confusion matrix in the Jupyter notebook to confirm balanced performance across both classes before saving and deploying the model.

---

## 🔮 Future Improvements

- [ ] Display confidence score / prediction probability alongside the result
- [ ] Support article URL input — auto-scrape and analyze the content
- [ ] Add multilingual news detection support
- [ ] Experiment with deep learning models (LSTM, BERT, RoBERTa)
- [ ] Deploy publicly on Streamlit Cloud or Hugging Face Spaces
- [ ] Add a feedback button so users can report incorrect predictions

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Made with ❤️ as part of the **Data Science Internship at [Pinnacle Labs](https://pinnaclelabs.tech/internship/)**

**[OJAS PAUL]**

---

> ⭐ If you found this project helpful, please give it a star on GitHub!
