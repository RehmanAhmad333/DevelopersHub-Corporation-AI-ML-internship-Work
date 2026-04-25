<!DOCTYPE html>
<html>
<body>
<div style="font-family: 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%); color: #eef2ff; border-radius: 24px;">

<!-- HEADER SECTION -->
<div style="text-align: center; padding: 2rem 1rem 1rem 1rem;">
    <h1 style="font-size: 3rem; font-weight: 800; background: linear-gradient(135deg, #FF6B6B, #FFD93D); -webkit-background-clip: text; background-clip: text; color: transparent; margin: 0;">📰 News Topic Classifier</h1>
    <p style="font-size: 1.2rem; color: #a0a8c0; margin-top: 0.5rem;">BERT Fine‑Tuning • Transformers • Streamlit • 92% Accuracy</p>
    <div style="margin-top: 1.5rem;">
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">🧠 BERT</span>
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">🤗 Transformers</span>
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">📊 AG News</span>
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">⚡ Streamlit</span>
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">🏆 F1‑Score 0.917</span>
    </div>
</div>

<hr style="border-color: #2a2f45; margin: 20px 0;">

<!-- OVERVIEW -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📌 Project Overview</h2>
    <p>This project fine‑tunes a <strong>BERT‑base‑uncased</strong> transformer model on the <strong>AG News dataset</strong> (subsampled) to classify news headlines into four categories: <strong>World, Sports, Business, Sci/Tech</strong>. The fine‑tuned model is then deployed via an interactive <strong>Streamlit</strong> web app for real‑time classification.</p>
</div>

<!-- DATASET -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📚 Dataset</h2>
    <ul>
        <li><strong>Source:</strong> <code>SUBHANmm/Smaller_AG_News_Dataset</code> (Hugging Face)</li>
        <li><strong>Training samples:</strong> 5,900</li>
        <li><strong>Test samples:</strong> 4,000</li>
        <li><strong>Labels:</strong> 0 = World, 1 = Sports, 2 = Business, 3 = Sci/Tech</li>
    </ul>
</div>

<!-- MODEL TRAINING -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">🧪 Model Training</h2>
    <ul>
        <li><strong>Base Model:</strong> <code>bert-base-uncased</code></li>
        <li><strong>Tokenizer:</strong> BERT tokenizer with <code>max_length=128</code>, padding & truncation</li>
        <li><strong>Training Arguments:</strong>
            <ul>
                <li>Epochs: 3</li>
                <li>Batch size: 16</li>
                <li>Learning rate: 5e-5</li>
                <li>Weight decay: 0.01</li>
                <li>Warmup steps: 500</li>
            </ul>
        </li>
        <li><strong>Framework:</strong> Hugging Face <code>Trainer</code> API</li>
    </ul>
</div>

<!-- RESULTS -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📊 Evaluation Results</h2>
    <table style="width:100%; border-collapse: collapse; color: #ddd;">
        <tr style="background: #0b0f1c;">
            <th style="padding: 10px; text-align: left;">Epoch</th>
            <th style="padding: 10px; text-align: left;">Training Loss</th>
            <th style="padding: 10px; text-align: left;">Validation Loss</th>
            <th style="padding: 10px; text-align: left;">Accuracy</th>
            <th style="padding: 10px; text-align: left;">F1 Score</th>
        </tr>
        <tr><td style="padding: 8px; border-bottom:1px solid #2a2f45;">1</td><td>—</td><td>0.344</td><td>0.893</td><td>0.893</td></tr>
        <tr><td style="padding: 8px; border-bottom:1px solid #2a2f45;">2</td><td>0.539</td><td>0.323</td><td>0.908</td><td>0.909</td></tr>
        <tr><td style="padding: 8px;">3</td><td>0.128</td><td>0.385</td><td><strong>0.917</strong></td><td><strong>0.917</strong></td></tr>
    </table>
    <p style="margin-top: 15px;">✅ <strong>Final Accuracy: 91.73%</strong> &nbsp;|&nbsp; ✅ <strong>Weighted F1‑Score: 0.917</strong></p>
</div>

<!-- DEPLOYMENT -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">🚀 Deployment – Streamlit App</h2>
    <p>The fine‑tuned model is saved locally (<code>./my_model</code>) and loaded into a <strong>Streamlit</strong> web app. The app provides:</p>
    <ul>
        <li>Clean, modern UI with glass‑morphism effect</li>
        <li>Input field for news headline</li>
        <li>Real‑time BERT inference</li>
        <li>Prediction of one of four topics</li>
        <li>Fully responsive (mobile/desktop)</li>
    </ul>
    <p><strong>Live Demo (Streamlit Cloud):</strong> <em>(add your deployed link here)</em></p>
</div>

<!-- TECH STACK -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">🛠️ Technologies Used</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px;">
        <div><strong>🐍 Python</strong><br>3.10+</div>
        <div><strong>🤗 Transformers</strong><br>Fine‑tuning & inference</div>
        <div><strong>📊 Datasets</strong><br>AG News loading</div>
        <div><strong>🔥 PyTorch</strong><br>Backend framework</div>
        <div><strong>⚡ Streamlit</strong><br>Web deployment</div>
        <div><strong>📈 Scikit‑learn</strong><br>Metrics (Accuracy, F1)</div>
    </div>
</div>

<!-- PROJECT STRUCTURE -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📁 Project Structure</h2>
    <pre style="background: #0b0f1c; padding: 1rem; border-radius: 16px; overflow-x: auto; color: #b0c4de;">
news-topic-classifier/
├── my_model/                 # Fine‑tuned BERT model + tokenizer
│   ├── config.json
│   ├── model.safetensors
│   └── tokenizer files
├── streamlit.py              # Streamlit application
├── requirements.txt          # Dependencies
├── notebook.ipynb            # Training notebook 
└── README.md                 # This file
    </pre>
</div>

<!-- HOW TO RUN -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">⚙️ How to Run Locally</h2>
    <ol style="line-height: 1.7;">
        <li><strong>Clone the repository</strong><br><code>git clone https://github.com/RehmanAhmad333/news-topic-classifier.git</code><br><code>cd news-topic-classifier</code></li>
        <li><strong>Create virtual environment</strong><br><code>python -m venv venv</code><br><code>venv\Scripts\activate</code> (Windows) / <code>source venv/bin/activate</code> (Mac/Linux)</li>
        <li><strong>Install dependencies</strong><br><code>pip install -r requirements.txt</code></li>
        <li><strong>Run Streamlit app</strong><br><code>streamlit run app.py</code></li>
        <li>Open your browser at <code>http://localhost:8501</code></li>
    </ol>

<div style="text-align: center; margin: 20px 0;">
    <a href="https://news-topic-classifier-bert-mtwbtx6zcuj43aappshfnnh.streamlit.app" target="_blank" style="background: #FF6B6B; color: white; padding: 12px 28px; border-radius: 40px; text-decoration: none; font-weight: 600; display: inline-block;">🚀 Try Live Demo</a>
</div>

</div>



<!-- REQUIREMENTS.TXT -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📦 requirements.txt</h2>
    <pre style="background: #0b0f1c; padding: 1rem; border-radius: 16px;">
streamlit==1.35.0
transformers==4.53.1
torch==2.5.1
    </pre>
</div>

<!-- FUTURE IMPROVEMENTS -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">🔮 Future Improvements</h2>
    <ul>
        <li>Add confidence score visualisation (bar chart)</li>
        <li>Support for longer text inputs (increase max length)</li>
        <li>Deploy on Hugging Face Spaces with Gradio</li>
        <li>Add more categories (e.g., Health, Entertainment)</li>
    </ul>
</div>

<!-- CHALLENGES SOLVED -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">⚡ Challenges & Solutions</h2>
    <ul>
        <li><strong>Large model size for Streamlit Cloud</strong> – Used caching and limited thread count for efficient loading.</li>
        <li><strong>Tokenisation mismatch between training & inference</strong> – Ensured same max_length and truncation settings.</li>
        <li><strong>CSS overriding by Streamlit</strong> – Used highly specific selectors and system fonts for consistent appearance.</li>
    </ul>
</div>



<!-- AUTHOR & LINK -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0; text-align: center;">
    <h2 style="color: #FFD93D; margin-top: 0;">👤 Author</h2>
    <p><strong>Rehman Ahmad Cheema</strong><br>
    🔗 <a href="https://github.com/RehmanAhmad333" target="_blank" style="color: #FFD93D;">GitHub</a> • 
    💼 <a href="https://www.linkedin.com/in/rehman-ahmad-9a5b17384/" style="color: #FFD93D;">LinkedIn</a></p>
</div>


<!-- FOOTER -->
<div style="text-align: center; padding: 1rem 0; border-top: 1px solid #2a2f45; margin-top: 20px; color: #6f7a9e;">
    <p>Built with dedication by <strong>Rehman Ahmad Cheema</strong> – AI Developer Intern</p>
</div>

</div>
</body>
</html>