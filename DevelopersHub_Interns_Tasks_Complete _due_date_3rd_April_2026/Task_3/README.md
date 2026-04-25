<!-- README.md for Task 3 -->
<h1 align="center">❤️ Heart Disease Prediction – Binary Classification</h1>

<p align="center">
  <img src="https://img.icons8.com/color/96/000000/heart-health.png"/>
  <br>
  <i>Predicting cardiovascular risk using clinical data</i>
</p>

<hr>

<h2>📌 Objective</h2>
<p>Build a classification model to predict whether a person is at risk of heart disease based on health indicators.</p>

<hr>

<h2>📂 Dataset</h2>
<ul>
  <li><strong>Source</strong>: UCI Heart Disease (Kaggle)</li>
  <li><strong>Samples</strong>: 918</li>
  <li><strong>Features</strong>: 11 clinical + target <code>HeartDisease</code> (0 = no, 1 = yes)</li>
</ul>

<table style="width:100%; border-collapse: collapse;">
  <tr style="background:#c0392b; color:white;"><th>Feature</th><th>Type</th><th>Description</th></tr>
  <tr><td>Age</td><td>int</td><td>Patient age</td></tr>
  <tr><td>Sex</td><td>categorical</td><td>M/F</td></tr>
  <tr><td>ChestPainType</td><td>categorical</td><td>ATA, NAP, ASY, TA</td></tr>
  <tr><td>RestingBP</td><td>int</td><td>Resting blood pressure (mm Hg)</td></tr>
  <tr><td>Cholesterol</td><td>int</td><td>Serum cholesterol (mg/dl)</td></tr>
  <tr><td>FastingBS</td><td>binary</td><td>Fasting blood sugar > 120 mg/dl</td></tr>
  <tr><td>RestingECG</td><td>categorical</td><td>Normal, ST, LVH</td></tr>
  <tr><td>MaxHR</td><td>int</td><td>Maximum heart rate achieved</td></tr>
  <tr><td>ExerciseAngina</td><td>binary</td><td>Angina induced by exercise</td></tr>
  <tr><td>Oldpeak</td><td>float</td><td>ST depression induced by exercise</td></tr>
  <tr><td>ST_Slope</td><td>categorical</td><td>Up, Flat, Down</td></tr>
</table>

<hr>

<h2>🧹 Data Cleaning</h2>
<ul>
  <li><code>RestingBP</code> had zero values → replaced with median (130).</li>
  <li><code>Cholesterol</code> had zero values → replaced with mean (198.8).</li>
  <li>No missing values otherwise.</li>
</ul>

<hr>

<h2>📊 Exploratory Data Analysis (EDA)</h2>
<h3>Key Visual Insights</h3>
<ul>
  <li>✅ Males have higher heart disease proportion.</li>
  <li>✅ ChestPainType = <strong>ASY</strong> is strongly associated with disease.</li>
  <li>✅ ExerciseAngina = <strong>Y</strong> increases risk.</li>
  <li>✅ ST_Slope = <strong>Flat</strong> more common in diseased patients.</li>
  <li>✅ Lower MaxHR and higher Oldpeak correlate with disease.</li>
</ul>



<hr>

<h2>🤖 Model Training</h2>
<ul>
  <li><strong>Algorithm</strong>: Decision Tree Classifier</li>
  <li><strong>Hyperparameter Tuning</strong>: GridSearchCV (5‑fold CV)</li>
  <li><strong>Best Parameters</strong>:
    <pre>ccp_alpha=0.001, criterion='gini', max_depth=4, max_features=None, splitter='random'</pre>
  </li>
</ul>

<hr>

<h2>📈 Evaluation Metrics</h2>

<table style="width:100%; text-align:center; border:1px solid #2c3e50;">
  <tr style="background:#2c3e50; color:white;"><th>Metric</th><th>Train</th><th>Test</th></tr>
  <tr><td>Accuracy</td><td>80.79%</td><td><strong>85.87%</strong></td></tr>
  <tr><td>ROC‑AUC</td><td>-</td><td><strong>0.894</strong></td></tr>
  <tr><td>Precision (class 1)</td><td>-</td><td>0.89</td></tr>
  <tr><td>Recall (class 1)</td><td>-</td><td>0.87</td></tr>
  <tr><td>F1‑score (class 1)</td><td>-</td><td>0.88</td></tr>
</table>

<h3>Confusion Matrix (Test)</h3>
<pre style="background:#eee; padding:10px;">
[[63 12]
 [14 95]]
</pre>

<h3>ROC Curve</h3>
<p align="center">
  <img src="image.png" alt="ROC curve" width="60%">
  <br>
  <em>AUC = 0.894 → Good discrimination ability</em>
</p>

<hr>

<h2>🧪 Feature Importance (from Decision Tree)</h2>
<p>Top features driving prediction:</p>
<ol>
  <li>ST_Slope</li>
  <li>ChestPainType</li>
  <li>ExerciseAngina</li>
  <li>MaxHR</li>
  <li>Oldpeak</li>
</ol>

<hr>

<h2>📦 Required Libraries</h2>
<pre style="background:#2d2d2d; color:#ccc; padding:10px; border-radius:6px;">
pandas, numpy, matplotlib, seaborn, scikit-learn
</pre>

<hr>

<h2>🏁 Conclusion</h2>
<p>✅ The optimised Decision Tree model generalises well (test accuracy ≈86%).<br>
✅ ROC‑AUC of 0.894 indicates strong separation between healthy and diseased individuals.<br>
✅ This model can serve as a screening tool for early heart disease risk assessment.</p>

<hr>

<h2>🚀 Future Improvements</h2>
<ul>
  <li>Try ensemble methods: Random Forest, XGBoost</li>
  <li>Use SHAP/LIME for explainability</li>
  <li>Deploy as a web app (Flask/Streamlit)</li>
</ul>

<hr>
<p align="center">Made with ❤️ for healthcare analytics</p>