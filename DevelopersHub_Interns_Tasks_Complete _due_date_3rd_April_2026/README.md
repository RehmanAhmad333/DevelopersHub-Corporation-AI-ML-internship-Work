<!DOCTYPE html>
<html>
<body>
<div style="font-family: 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%); color: #eef2ff; border-radius: 24px;">

<!-- HEADER -->
<div style="text-align: center; padding: 2rem 1rem 1rem 1rem;">
    <h1 style="font-size: 2.8rem; font-weight: 800; background: linear-gradient(135deg, #ff7e5e, #feb47b); -webkit-background-clip: text; background-clip: text; color: transparent; margin: 0;">📊 AI/ML Internship Tasks</h1>
    <p style="font-size: 1.2rem; color: #a0a8c0;">DevelopersHub Corporation – Completed by <strong>Rehman Ahmad Cheema</strong></p>
    <p style="font-size: 0.9rem;">Due: 3rd April, 2026 | ✅ 4 tasks completed (3 required + 1 extra)</p>
    <div style="margin-top: 1.5rem;">
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">🐍 Python</span>
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">📈 Pandas/Seaborn</span>
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">🤖 Scikit‑learn</span>
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">💬 LangChain + Groq</span>
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">🎨 Streamlit</span>
    </div>
</div>

<hr style="border-color: #2a2f45; margin: 20px 0;">

<!-- QUICK OVERVIEW -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #feb47b; margin-top: 0;">📌 Submission Overview</h2>
    <p>I successfully completed <strong>4 tasks</strong> (3 required + 1 additional) for the AI/ML Engineering Internship. Each task includes:</p>
    <ul>
        <li>✅ Jupyter Notebook with full code & explanations</li>
        <li>✅ Clean, modular, commented code</li>
        <li>✅ Data preprocessing & visualisation</li>
        <li>✅ Model training & evaluation</li>
        <li>✅ Summary of results and insights</li>
    </ul>
    <p>Below is a quick snapshot of every completed task. Click the links to see detailed README files.</p>
</div>

<!-- TASK 1 -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0; border-left: 5px solid #4CAF50;">
    <h2 style="color: #4CAF50; margin-top: 0;">🌼 Task 1 – Iris Dataset Exploration & Visualization</h2>
    <table style="width:100%; border-collapse: collapse;">
        <tr><td style="padding: 5px 0;"><strong>Objective</strong></td><td>Load, inspect, and visualise the Iris dataset to understand distributions and relationships.</td></tr>
        <tr><td style="padding: 5px 0;"><strong>Dataset</strong></td><td>Iris (150 samples, 4 numeric features, 3 species)</td></tr>
        <tr><td style="padding: 5px 0;"><strong>Tools</strong></td><td>pandas, matplotlib, seaborn</td></tr>
        <tr><td style="padding: 5px 0;"><strong>Key Steps</strong></td><td>.info(), .describe(), scatter plot, histograms, box plots, pair plot.</td></tr>
        <tr><td style="padding: 5px 0;"><strong>Insights</strong></td><td>Petal measurements clearly separate species; SepalWidth has mild outliers; no missing values.</td></tr>
    </table>
    <p style="margin-top: 10px;">📄 <a href="DevelopersHub_Interns_Tasks_Complete _due_date_3rd_April_2026\Task_1\README.md" style="color: #4CAF50;">Detailed README (Task 1)</a> – <em>copy provided separately</em></p>
</div>

<!-- TASK 2 -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0; border-left: 5px solid #2196F3;">
    <h2 style="color: #2196F3; margin-top: 0;">📈 Task 2 – Stock Price Prediction (Next Day Close)</h2>
    <table style="width:100%; border-collapse: collapse;">
        <tr><td style="padding: 5px 0;"><strong>Objective</strong></td><td>Predict Apple’s next-day closing price using Open, High, Low, Volume.</td></tr>
        <tr><td style="padding: 5px 0;"><strong>Data</strong></td><td>yfinance (AAPL, 2018–2024, 1509 rows)</td></tr>
        <tr><td style="padding: 5px 0;"><strong>Models</strong></td><td>Linear Regression, Random Forest Regressor</td></tr>
        <tr><td style="padding: 5px 0;"><strong>Evaluation</strong></td><td>R² score, actual vs predicted scatter plot</td></tr>
        <tr><td style="padding: 5px 0;"><strong>Results</strong></td><td>Test R² = 0.99977 for both models (very high due to correlated features).</td></tr>
    </table>
    <p style="margin-top: 10px;">📄 <a href="DevelopersHub_Interns_Tasks_Complete _due_date_3rd_April_2026\Task_2\README.md" style="color: #2196F3;">Detailed README (Task 2)</a></p>
</div>

<!-- TASK 3 -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0; border-left: 5px solid #e74c3c;">
    <h2 style="color: #e74c3c; margin-top: 0;">❤️ Task 3 – Heart Disease Prediction (Classification)</h2>
    <table style="width:100%; border-collapse: collapse;">
        <tr><td style="padding: 5px 0;"><strong>Objective</strong></td><td>Predict heart disease risk using clinical health data.</td></tr>
        <tr><td style="padding: 5px 0;"><strong>Dataset</strong></td><td>UCI Heart Disease (Kaggle) – 918 samples, 11 features.</td></tr>
        <tr><td style="padding: 5px 0;"><strong>Model</strong></td><td>Decision Tree (tuned with GridSearchCV)</td></tr>
        <tr><td style="padding: 5px 0;"><strong>Evaluation</strong></td><td>Accuracy, ROC‑AUC, confusion matrix, classification report.</td></tr>
        <tr><td style="padding: 5px 0;"><strong>Results</strong></td><td>Test accuracy 85.87%, ROC‑AUC = 0.894. Important features: ST_Slope, ChestPainType, ExerciseAngina.</td></tr>
    </table>
    <p style="margin-top: 10px;">📄 <a href="DevelopersHub_Interns_Tasks_Complete _due_date_3rd_April_2026\Task_3\README.md" style="color: #e74c3c;">Detailed README (Task 3)</a></p>
</div>

<!-- TASK 4/5 – MEDIBOT (RAG + LLM) -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0; border-left: 5px solid #9b59b6;">
    <h2 style="color: #9b59b6; margin-top: 0;">💬 Task 4/5 – General Health Chatbot (MediBot – RAG + LLM)</h2>
    <table style="width:100%; border-collapse: collapse;">
        <tr><td style="padding: 5px 0;"><strong>Objective</strong></td><td>Build a medical chatbot using Retrieval‑Augmented Generation (RAG) with a medical PDF knowledge base.</td></tr>
        <tr><td style="padding: 5px 0;"><strong>Tech Stack</strong></td><td>LangChain, FAISS, HuggingFace embeddings, Groq LLM (Llama‑3.1‑8B), Streamlit.</td></tr>
        <tr><td style="padding: 5px 0;"><strong>Features</strong></td><td>Conversational memory, emergency detection, non‑medical query rejection, suggestion pills, clear chat.</td></tr>
        <tr><td style="padding: 5px 0;"><strong>Results</strong></td><td>Fully functional web app that answers health questions accurately using the Gale Encyclopedia of Medicine.</td></tr>
    </table>
    <p style="margin-top: 10px;">📄 <a href="DevelopersHub_Interns_Tasks_Complete _due_date_3rd_April_2026\AI_Medical_Chatbot\README.md" style="color: #9b59b6;">Detailed MediBot README (attached below)</a></p>
</div>

<!-- SUMMARY TABLE -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #feb47b;">📊 Completed Tasks Summary</h2>
    <table style="width:100%; border-collapse: collapse; text-align: center;">
        <tr style="background: #2a2f45;">
            <th style="padding: 10px;">Task</th><th style="padding: 10px;">Domain</th><th style="padding: 10px;">Model(s)</th><th style="padding: 10px;">Key Metric</th>
        </tr>
        <tr><td style="padding: 8px; border-bottom: 1px solid #2a2f45;">Task 1</td><td>EDA & Visualisation</td><td>-</td><td>Insights from plots</td></tr>
        <tr><td style="padding: 8px; border-bottom: 1px solid #2a2f45;">Task 2</td><td>Time Series Regression</td><td>Linear Regression, Random Forest</td><td>R² = 0.9998</td></tr>
        <tr><td style="padding: 8px; border-bottom: 1px solid #2a2f45;">Task 3</td><td>Binary Classification</td><td>Decision Tree (tuned)</td><td>Accuracy 85.87%, AUC 0.894</td></tr>
        <tr><td style="padding: 8px;">MediBot (Task 4/5)</td><td>RAG + LLM Chatbot</td><td>Llama‑3.1‑8B + FAISS</td><td>Relevant, safe responses</td></tr>
    </table>
</div>

<!-- LINKS TO DETAILED READMES (placeholders) -->
<div style="background: #0b0f1c; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #00B4D8;">📁 Detailed README Files</h2>
    <p>Each task has its own dedicated README with full explanations, code snippets, and screenshots. Below are the links (or you can find them in the repository):</p>
    <ul>
        <li><strong>Task 1</strong> – <a href="DevelopersHub_Interns_Tasks_Complete _due_date_3rd_April_2026\Task_1\README.md" style="color: #4CAF50;">Iris Dataset Exploration</a></li>
        <li><strong>Task 2</strong> – <a href="DevelopersHub_Interns_Tasks_Complete _due_date_3rd_April_2026\Task_2\README.md" style="color: #2196F3;">Stock Price Prediction</a></li>
        <li><strong>Task 3</strong> – <a href="DevelopersHub_Interns_Tasks_Complete _due_date_3rd_April_2026\Task_3\README.md" style="color: #e74c3c;">Heart Disease Prediction</a></li>
        <li><strong>MediBot (Chatbot)</strong> – <a href="DevelopersHub_Interns_Tasks_Complete _due_date_3rd_April_2026\AI_Medical_Chatbot\README.md" style="color: #9b59b6;">RAG‑based Medical Assistant</a></li>
    </ul>
    <p><em>Note: The detailed READMEs are provided as separate files in this repository.</em></p>
</div>

<!-- SUBMISSION CHECKLIST -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #feb47b;">✅ Submission Checklist (per task)</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px,1fr)); gap: 0.5rem;">
        <div>✔ Jupyter Notebook with clear goal</div>
        <div>✔ Data loading & preprocessing</div>
        <div>✔ Visualisation & exploration</div>
        <div>✔ Model training & evaluation</div>
        <div>✔ Explanation of results</div>
        <div>✔ Clean, commented code</div>
        <div>✔ GitHub repo with README</div>
        <div>✔ Shared on Google Classroom</div>
    </div>
</div>

<!-- AUTHOR & FOOTER -->
<div style="display: flex; justify-content: space-between; flex-wrap: wrap; gap: 20px; background: #0b0f1c; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <div>
        <h3 style="color: #00B4D8; margin: 0 0 8px 0;">👤 Intern</h3>
        <p><strong>Rehman Ahmad Cheema</strong><br>
        🔗 <a href="https://github.com/RehmanAhmad333" style="color: #00B4D8;">GitHub</a> • 
        💼 <a href="https://www.linkedin.com/in/rehman-ahmad-9a5b17384/" style="color: #00B4D8;">LinkedIn</a>
        </p>
    </div>
    <div>
        <h3 style="color: #00B4D8; margin: 0 0 8px 0;">📅 Submission Date</h3>
        <p>3rd April, 2026</p>
    </div>
</div>

<div style="text-align: center; padding: 1rem 0; border-top: 1px solid #2a2f45; margin-top: 20px; color: #6f7a9e;">
    <p>Built with ❤️ by Rehman Ahmad Cheema | DevelopersHub Corporation AI/ML Internship</p>
</div>

 <strong>DevelopersHub-Corporation-AI-ML-internship-Work</strong>
 <br>
AI/ML Internship (6 Months) at DevelopersHub Corporation. Includes ML projects, data preprocessing, EDA, model building, and evaluation. Hands-on work with Python, NumPy, Pandas, and Scikit-learn, plus real-world problem solving and core algorithm implementations.

</div>
</body>
</html>

