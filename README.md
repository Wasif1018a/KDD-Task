# 🧠 PubMed Article Summarizer

A lightweight Flask-based web application for summarizing PubMed articles using a pre-trained **T5 model** from Hugging Face.
Upload a CSV file of articles, and the app generates concise summaries viewable in your browser.

---

## 📂 Repository Contents

| File                                           | Description                                                                                |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Documentation.docx**                         | Project documentation and development notes.                                               |
| **Flask_Main.py**                              | Main Flask backend handling uploads, running the summarization model, and serving results. |
| **Flask_UI.html**                              | Frontend HTML template for uploading files and displaying summarized articles.             |
| **Hugging_Face_Data_Preprocessing_And_Summarization.py**    | Notebook/script for Hugging Face data preprocessing and model fine-tuning.    |
| **README.md**                                  | This file. Project overview, setup instructions, and usage details.                        |

---

## ✨ Features

* **CSV Upload** – Upload PubMed articles in CSV format.
* **Summarization** – Summarizes each article using a fine-tuned T5 model.
* **Web UI** – Simple HTML interface built with Flask templates.
* **Preprocessing Script** – Hugging Face preprocessing pipeline for preparing data.

---

## ⚙️ Installation

### Prerequisites

* Python 3.x
* Flask
* Transformers (Hugging Face)
* NLTK

Install dependencies:

```bash
pip install -r requirements.txt
```

Download NLTK resources:

```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

---

## 🚀 Running the App

1. Clone the repository:

```bash
git clone https://github.com/your/repo.git
cd your-repo
```

2. Run the Flask backend:

```bash
python Flask_Main.py
```

3. Open your browser at:

```
http://127.0.0.1:5000/
```

4. Upload your CSV file (must contain an **`article`** column).
5. View original and summarized articles in the table shown on the page.

---

## 📝 Usage Notes

* **Model Fine-Tuning** – If you haven’t fine-tuned T5 yet, use the provided Hugging Face preprocessing script to prepare your dataset. Save the fine-tuned weights in a directory accessible to the Flask app.
* **Security** – For production, secure file uploads and run behind HTTPS.
* **Performance** – Large CSVs may require batch processing.

---

## 🧑‍💻 Authors

* **Wasif Mehboob**

---

## 🙏 Acknowledgments

* Hugging Face for the **Transformers** library and pre-trained models.
* Flask for providing a lightweight Python web framework.

---
