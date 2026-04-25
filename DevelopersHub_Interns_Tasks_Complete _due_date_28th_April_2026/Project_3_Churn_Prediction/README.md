<!DOCTYPE html>
<html>
<body>
<div style="font-family: 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%); color: #eef2ff; border-radius: 24px;">

<!-- HEADER SECTION -->
<div style="text-align: center; padding: 2rem 1rem 1rem 1rem;">
    <h1 style="font-size: 3rem; font-weight: 800; background: linear-gradient(135deg, #FF6B6B, #FFD93D); -webkit-background-clip: text; background-clip: text; color: transparent; margin: 0;">📞 Customer Churn Prediction</h1>
    <p style="font-size: 1.2rem; color: #a0a8c0; margin-top: 0.5rem;">End-to-End ML Pipeline • Scikit-learn • GridSearchCV • Production Ready</p>
    <div style="margin-top: 1.5rem;">
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">🐍 Scikit-learn</span>
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">⚙️ Pipeline API</span>
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">🔍 GridSearchCV</span>
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">📊 Telco Dataset</span>
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">🏆 Recall 0.82</span>
    </div>
</div>

<hr style="border-color: #2a2f45; margin: 20px 0;">

<!-- OVERVIEW -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📌 Project Overview</h2>
    <p>This project builds a <strong>production-ready machine learning pipeline</strong> to predict customer churn for a telecommunications company. Using the <strong>Telco Customer Churn dataset</strong>, the pipeline identifies customers likely to leave the service, enabling proactive retention strategies.</p>
    <p>The solution implements a complete <strong>Scikit-learn Pipeline</strong> with preprocessing, hyperparameter tuning using <strong>GridSearchCV</strong>, and model export using <strong>joblib</strong> for production deployment.</p>
</div>

<!-- DATASET -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📚 Dataset Overview</h2>
    <ul>
        <li><strong>Source:</strong> Telco Customer Churn Dataset</li>
        <li><strong>Total Records:</strong> 7,043 customers</li>
        <li><strong>Features:</strong> 21 columns (demographic, account, service information)</li>
        <li><strong>Target:</strong> Churn (Yes/No)</li>
        <li><strong>Churn Rate:</strong> 26.6% (1,869 churned customers)</li>
    </ul>
</div>

<!-- DATA PREPROCESSING -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">🔄 Data Preprocessing</h2>
    <ul>
        <li><strong>Data Type Conversion:</strong> Converted <code>TotalCharges</code> from object to numeric</li>
        <li><strong>Missing Values:</strong> Removed 11 records with missing TotalCharges values</li>
        <li><strong>Feature Selection:</strong> Selected 10 most important features based on EDA</li>
        <li><strong>Train-Test Split:</strong> 80% train, 20% test with stratification</li>
    </ul>
</div>

<!-- FEATURE SELECTION -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">🎯 Selected Features</h2>
    <h3>📊 Numerical Features (3):</h3>
    <ul>
        <li>tenure</li>
        <li>MonthlyCharges</li>
        <li>TotalCharges</li>
    </ul>
    <h3>🏷️ Categorical Features (6):</h3>
    <ul>
        <li>Contract</li>
        <li>PaymentMethod</li>
        <li>InternetService</li>
        <li>OnlineSecurity</li>
        <li>TechSupport</li>
        <li>PaperlessBilling</li>
    </ul>
    <h3>➕ Additional Feature (1):</h3>
    <ul>
        <li>SeniorCitizen</li>
    </ul>
</div>

<!-- EDA INSIGHTS -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📈 Exploratory Data Analysis Insights</h2>
    <ul>
        <li>🔴 <strong>Imbalanced Dataset:</strong> 73.4% No Churn, 26.6% Churn</li>
        <li>📉 <strong>Tenure:</strong> Customers with lower tenure are more likely to churn</li>
        <li>💰 <strong>MonthlyCharges:</strong> Higher monthly charges correlate with higher churn</li>
        <li>📞 <strong>Contract Type:</strong> Month-to-month contracts have highest churn rate</li>
        <li>🔧 <strong>Services:</strong> Lack of OnlineSecurity and TechSupport increases churn</li>
    </ul>
</div>

<!-- PIPELINE ARCHITECTURE -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">🏗️ ML Pipeline Architecture</h2>
    <pre style="background: #0b0f1c; padding: 1rem; border-radius: 16px; overflow-x: auto; color: #b0c4de; font-size: 0.8rem;">
┌─────────────────────────────────────────────────────────────────────────┐
│                         INPUT RAW DATA                                  │
│                    (Customer Demographics + Services)                   │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      COLUMN TRANSFORMER                                 │
├────────────────────────────────┬────────────────────────────────────────┤
│  Numerical Features (3)        │  Categorical Features (7)              │
│  ┌─────────────────────┐       │  ┌──────────────────────────────┐     │
│  │   StandardScaler    │       │  │   OneHotEncoder (drop first) │     │
│  │   - tenure          │       │  │   - Contract                 │     │
│  │   - MonthlyCharges  │       │  │   - PaymentMethod            │     │
│  │   - TotalCharges    │       │  │   - InternetService          │     │
│  └─────────────────────┘       │  │   - OnlineSecurity           │     │
│                                │  │   - TechSupport              │     │
│                                │  │   - PaperlessBilling         │     │
│                                │  │   - SeniorCitizen            │     │
│                                │  └──────────────────────────────┘     │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      MODEL TRAINING                                     │
├────────────────────────────────┬────────────────────────────────────────┤
│  ┌─────────────────────┐       │  ┌──────────────────────────────┐     │
│  │  Random Forest      │       │  │  Logistic Regression         │     │
│  │  with GridSearchCV  │       │  │  with GridSearchCV           │     │
│  └─────────────────────┘       │  └──────────────────────────────┘     │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      BEST MODEL EXPORT                                  │
│                    (telco_churn_pipeline.joblib)                        │
└─────────────────────────────────────────────────────────────────────────┘
    </pre>
</div>

<!-- PREPROCESSOR DETAILS -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">⚙️ Preprocessor Configuration</h2>
    <pre style="background: #0b0f1c; padding: 1rem; border-radius: 16px; overflow-x: auto; color: #b0c4de; font-size: 0.8rem;"> ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['tenure', 'MonthlyCharges', 'TotalCharges']),
        ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), 
         ['Contract', 'PaymentMethod', 'InternetService', 'OnlineSecurity', 
          'TechSupport', 'PaperlessBilling', 'SeniorCitizen'])
    ]
)
    </pre>
</div>

<!-- MODEL TRAINING -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">🧪 Model Training & Hyperparameter Tuning</h2>
    <h3>🌲 Random Forest Classifier</h3>
    <pre style="background: #0b0f1c; padding: 0.8rem; border-radius: 12px; overflow-x: auto; font-size: 0.75rem;">
Parameters Tuned:
- n_estimators: [100, 200]
- max_depth: [None, 10, 20, 30]
- min_samples_split: [2, 5, 10]
- min_samples_leaf: [1, 2, 4]
- max_features: ['sqrt', 'log2']
- class_weight: [None, 'balanced']
    </pre>
    <h3>📊 Logistic Regression</h3>
    <pre style="background: #0b0f1c; padding: 0.8rem; border-radius: 12px; overflow-x: auto; font-size: 0.75rem;">
Parameters Tuned:
- C: [0.001, 0.01, 0.1, 1, 10]
- penalty: ['l1', 'l2']
- solver: ['liblinear']
- class_weight: [None, 'balanced']
- max_iter: [100, 200]
    </pre>
    <p><strong>Scoring Metric:</strong> F1-Score (balanced precision and recall)</p>
    <p><strong>Cross-Validation:</strong> 5-Fold Stratified CV</p>
</div>

<!-- RESULTS -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📊 Model Performance Comparison</h2>
    <table style="width:100%; border-collapse: collapse; color: #ddd;">
        <tr style="background: #0b0f1c;">
            <th style="padding: 12px; text-align: left;">Metric</th>
            <th style="padding: 12px; text-align: left;">Random Forest</th>
            <th style="padding: 12px; text-align: left;">Logistic Regression</th>
        </tr>
        <tr><td style="padding: 10px; border-bottom:1px solid #2a2f45;">Train Accuracy</td>
            <td style="padding: 10px; border-bottom:1px solid #2a2f45;">82.4%</td>
            <td style="padding: 10px; border-bottom:1px solid #2a2f45;">74.1%</td>
        </tr>
        <tr><td style="padding: 10px; border-bottom:1px solid #2a2f45;">Test Accuracy</td>
            <td style="padding: 10px; border-bottom:1px solid #2a2f45;">76.9%</td>
            <td style="padding: 10px; border-bottom:1px solid #2a2f45;">75.3%</td>
        </tr>
        <tr><td style="padding: 10px; border-bottom:1px solid #2a2f45;">Precision (Churn)</td>
            <td style="padding: 10px; border-bottom:1px solid #2a2f45;">0.55</td>
            <td style="padding: 10px; border-bottom:1px solid #2a2f45;">0.52</td>
        </tr>
        <tr><td style="padding: 10px; border-bottom:1px solid #2a2f45;"><strong>Recall (Churn)</strong></td>
            <td style="padding: 10px; border-bottom:1px solid #2a2f45;">0.75</td>
            <td style="padding: 10px; border-bottom:1px solid #2a2f45;"><strong style="color: #4CAF50;">0.82</strong></td>
        </tr>
        <tr><td style="padding: 10px;">F1-Score (Churn)</td>
            <td style="padding: 10px;">0.63</td>
            <td style="padding: 10px;"><strong style="color: #4CAF50;">0.64</strong></td>
        </tr>
    </table>
</div>

<!-- CONFUSION MATRICES -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📉 Confusion Matrices</h2>
    <h3>Random Forest (Test Set)</h3>
    <pre style="background: #0b0f1c; padding: 0.8rem; border-radius: 12px; overflow-x: auto; font-size: 0.75rem;">
                 Predicted
              No    Yes
    Actual No  801   232
           Yes  93   281
    </pre>
    <h3>Logistic Regression (Test Set)</h3>
    <pre style="background: #0b0f1c; padding: 0.8rem; border-radius: 12px; overflow-x: auto; font-size: 0.75rem;">
                 Predicted
              No    Yes
    Actual No  755   278
           Yes  69   305
    </pre>
</div>

<!-- FINAL MODEL SELECTION -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">🏆 Final Model Selection: Logistic Regression</h2>
    <div style="background: #0b0f1c; border-radius: 16px; padding: 1rem; margin: 15px 0; border-left: 4px solid #4CAF50;">
        <h3 style="color: #4CAF50; margin-top: 0;">Why Logistic Regression?</h3>
        <ul>
            <li>✅ <strong>Higher Recall (0.82 vs 0.75):</strong> Catches 7% more churned customers</li>
            <li>✅ <strong>Better F1-Score (0.64 vs 0.63):</strong> Better balance of precision and recall</li>
            <li>✅ <strong>Business Impact:</strong> Missing a churning customer (False Negative) is more costly than false alarm</li>
            <li>✅ <strong>Simplicity:</strong> More interpretable and faster inference</li>
            <li>✅ <strong>No Overfitting:</strong> Train (74.1%) and Test (75.3%) accuracy closely aligned</li>
        </ul>
    </div>
    <div style="background: #0b0f1c; border-radius: 16px; padding: 1rem; margin: 15px 0; border-left: 4px solid #FF9800;">
        <h3 style="color: #FF9800; margin-top: 0;">Best Hyperparameters Found:</h3>
        <pre style="background: #1e2338; padding: 0.8rem; border-radius: 12px; overflow-x: auto; font-size: 0.75rem;">
{
    'classifier__C': 1,
    'classifier__class_weight': 'balanced',
    'classifier__max_iter': 100,
    'classifier__penalty': 'l2',
    'classifier__solver': 'liblinear'
}
        </pre>
    </div>
</div>

<!-- MODEL EXPORT -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📦 Model Export (Production Ready)</h2>
    <pre style="background: #0b0f1c; padding: 1rem; border-radius: 16px; overflow-x: auto; color: #b0c4de; font-size: 0.8rem;">
import joblib

# Export complete pipeline
joblib.dump(best_lr, 'telco_churn_pipeline.joblib')

# Load pipeline in production
loaded_pipeline = joblib.load('telco_churn_pipeline.joblib')

# Make predictions
predictions = loaded_pipeline.predict(new_customer_data)
    </pre>
    <p><strong>✅ Pipeline includes both preprocessing and model - ready for production!</strong></p>
</div>

<!-- PROJECT STRUCTURE -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📁 Project Structure</h2>
    <pre style="background: #0b0f1c; padding: 1rem; border-radius: 16px; overflow-x: auto; color: #b0c4de; font-size: 0.75rem;">
customer-churn-prediction/
│
├── dataset/
│   └── Telco_Cusomer_Churn.csv          # Raw dataset
│
├── Predicting customer churn.ipynb      # Complete training notebook
│
├── telco_churn_pipeline.joblib          # Exported production pipeline
│
├── requirements.txt                     # Python dependencies
│
└── README.md                            # Project documentation
    </pre>
</div>

<!-- HOW TO RUN -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">⚙️ How to Run Locally</h2>
    <ol style="line-height: 1.7;">
        <li><strong>Clone the repository</strong><br><code>git clone https://github.com/RehmanAhmad333/customer-churn-prediction.git</code><br><code>cd customer-churn-prediction</code></li>
        <li><strong>Create virtual environment</strong><br><code>python -m venv venv</code><br><code>venv\Scripts\activate</code> (Windows) / <code>source venv/bin/activate</code> (Mac/Linux)</li>
        <li><strong>Install dependencies</strong><br><code>pip install -r requirements.txt</code></li>
        <li><strong>Run Jupyter Notebook</strong><br><code>jupyter notebook "Predicting customer churn.ipynb"</code></li>
        <li><strong>Or load saved pipeline</strong><br><code>python -c "import joblib; model = joblib.load('telco_churn_pipeline.joblib')"</code></li>
    </ol>
</div>

<!-- REQUIREMENTS.TXT -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📦 requirements.txt</h2>
    <pre style="background: #0b0f1c; padding: 1rem; border-radius: 16px;">
pandas==2.0.3
numpy==1.24.3
scikit-learn==1.3.0
matplotlib==3.7.2
seaborn==0.12.2
joblib==1.3.2
jupyter==1.0.0
    </pre>
</div>

<!-- KEY FEATURES -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">🔥 Key Features Implemented</h2>
    <ul>
        <li>✅ <strong>End-to-End Pipeline:</strong> Complete preprocessing + model in single pipeline</li>
        <li>✅ <strong>ColumnTransformer:</strong> Different preprocessing for numerical and categorical features</li>
        <li>✅ <strong>StandardScaler:</strong> Normalization for numerical features</li>
        <li>✅ <strong>OneHotEncoder:</strong> Encoding for categorical features</li>
        <li>✅ <strong>GridSearchCV:</strong> Systematic hyperparameter tuning with cross-validation</li>
        <li>✅ <strong>Model Comparison:</strong> Random Forest vs Logistic Regression</li>
        <li>✅ <strong>Business-Focused Selection:</strong> Prioritized recall for churn detection</li>
        <li>✅ <strong>Production Export:</strong> Joblib serialization for deployment</li>
    </ul>
</div>

<!-- CHALLENGES SOLVED -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">⚡ Challenges & Solutions</h2>
    <ul>
        <li><strong>Imbalanced Dataset (73% No, 27% Yes):</strong> Used <code>class_weight='balanced'</code> and F1-score for evaluation</li>
        <li><strong>TotalCharges as String:</strong> Converted to numeric with <code>pd.to_numeric(..., errors='coerce')</code></li>
        <li><strong>Missing Values:</strong> Removed 11 records with missing TotalCharges</li>
        <li><strong>Categorical Encoding:</strong> Used <code>drop='first'</code> to avoid dummy variable trap</li>
        <li><strong>Overfitting Risk:</strong> Used cross-validation and early stopping via GridSearch</li>
    </ul>
</div>

<!-- BUSINESS IMPACT -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">💼 Business Impact</h2>
    <ul>
        <li>💰 <strong>Cost Savings:</strong> Identifying 82% of churning customers enables proactive retention</li>
        <li>📈 <strong>Customer Retention:</strong> Target at-risk customers with special offers</li>
        <li>🎯 <strong>Actionable Insights:</strong> Features like Contract type and MonthlyCharges guide business decisions</li>
        <li>🔄 <strong>Scalable Solution:</strong> Pipeline can be retrained with new data</li>
    </ul>
</div>

<!-- FUTURE IMPROVEMENTS -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">🔮 Future Improvements</h2>
    <ul>
        <li>Deploy as REST API using FastAPI or Flask</li>
        <li>Add feature importance analysis for interpretability</li>
        <li>Experiment with XGBoost and LightGBM</li>
        <li>Implement threshold tuning for optimal recall-precision tradeoff</li>
        <li>Create dashboard for real-time monitoring</li>
        <li>Add A/B testing framework for model validation</li>
        <li>Implement automated retraining pipeline</li>
    </ul>
</div>

<!-- CONCLUSION -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📝 Conclusion</h2>
    <p>This project successfully demonstrates an <strong>end-to-end production-ready ML pipeline</strong> for customer churn prediction. The pipeline is:</p>
    <ul>
        <li>✅ <strong>Reusable:</strong> Same pipeline works for training and prediction</li>
        <li>✅ <strong>Scalable:</strong> Can handle new data without code changes</li>
        <li>✅ <strong>Optimized:</strong> Hyperparameters tuned via GridSearchCV</li>
        <li>✅ <strong>Deployable:</strong> Exported with joblib for production use</li>
    </ul>
    <p><strong>Logistic Regression</strong> was selected as the final model due to its superior recall (0.82) and better alignment with business objectives of identifying customers at risk of churn.</p>
</div>

<!-- AUTHOR -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0; text-align: center;">
    <h2 style="color: #FFD93D; margin-top: 0;">👤 Author</h2>
    <p><strong>Rehman Ahmad Cheema</strong><br>
    🔗 <a href="https://github.com/RehmanAhmad333" target="_blank" style="color: #FFD93D;">GitHub</a> • 
    💼 <a href="https://www.linkedin.com/in/rehman-ahmad-9a5b17384/" style="color: #FFD93D;">LinkedIn</a></p>
    <p style="margin-top: 10px;">AI/ML Engineer | Data Science Specialist | Production ML Pipeline Expert</p>
</div>

<!-- FOOTER -->
<div style="text-align: center; padding: 1rem 0; border-top: 1px solid #2a2f45; margin-top: 20px; color: #6f7a9e;">
    <p>Built with dedication by <strong>Rehman Ahmad Cheema</strong> – AI Developer Intern</p>
    <p style="font-size: 0.8rem;">© 2024 Customer Churn Prediction | MIT License</p>
</div>

</div>
</body>
</html>