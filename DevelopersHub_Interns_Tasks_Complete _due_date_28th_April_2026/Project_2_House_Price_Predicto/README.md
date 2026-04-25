<!DOCTYPE html>
<html>
<body>
<div style="font-family: 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%); color: #eef2ff; border-radius: 24px;">

<!-- HEADER SECTION -->
<div style="text-align: center; padding: 2rem 1rem 1rem 1rem;">
    <h1 style="font-size: 3rem; font-weight: 800; background: linear-gradient(135deg, #FF6B6B, #FFD93D); -webkit-background-clip: text; background-clip: text; color: transparent; margin: 0;">🏠 Multimodal House Price Predictor</h1>
    <p style="font-size: 1.2rem; color: #a0a8c0; margin-top: 0.5rem;">ResNet50 • Feature Fusion • Deep Learning • 535 Properties • 2140 Images</p>
    <div style="margin-top: 1.5rem;">
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">🖼️ ResNet50</span>
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">🔀 Feature Fusion</span>
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">📊 Tabular Data</span>
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">⚡ Streamlit</span>
        <span style="background: #2a2f45; padding: 6px 14px; border-radius: 40px; font-size: 0.8rem;">🏆 MAE $171k</span>
    </div>
</div>

<hr style="border-color: #2a2f45; margin: 20px 0;">

<!-- OVERVIEW -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📌 Project Overview</h2>
    <p>This project implements a <strong>Multimodal Machine Learning System</strong> that predicts house prices by combining:</p>
    <ul>
        <li>🖼️ <strong>Visual Features</strong> – Extracted from property images using <strong>ResNet50</strong> (pretrained on ImageNet)</li>
        <li>📊 <strong>Tabular Data</strong> – Bedrooms, bathrooms, area, and zipcode information</li>
        <li>🔀 <strong>Fusion Architecture</strong> – Concatenating both modalities for enhanced predictions</li>
    </ul>
    <p>The fine‑tuned multimodal model is deployed via an interactive <strong>Streamlit</strong> web app for real‑time house price estimation.</p>
</div>

<!-- DATASET -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📚 Dataset Statistics</h2>
    <ul>
        <li><strong>Total Houses:</strong> 535</li>
        <li><strong>Total Images:</strong> 2,140 (4 per house: bedroom, bathroom, kitchen, frontal)</li>
        <li><strong>Tabular Features:</strong> Bedrooms, Bathrooms, Area, Zipcode</li>
        <li><strong>Price Range:</strong> $22,000 – $5,858,000</li>
        <li><strong>Mean Price:</strong> $589,363</li>
        <li><strong>Median Price:</strong> $529,000</li>
        <li><strong>Unique Zipcodes:</strong> 49</li>
    </ul>
</div>

<!-- FEATURE CORRELATION -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📈 Feature Correlation with Price</h2>
    <table style="width:100%; border-collapse: collapse; color: #ddd;">
        <tr style="background: #0b0f1c;">
            <th style="padding: 10px; text-align: left;">Feature</th>
            <th style="padding: 10px; text-align: left;">Correlation</th>
            <th style="padding: 10px; text-align: left;">Strength</th>
        </tr>
        <tr><td style="padding: 8px; border-bottom:1px solid #2a2f45;">Area</td>
            <td style="padding: 8px; border-bottom:1px solid #2a2f45;">0.492</td>
            <td style="padding: 8px; border-bottom:1px solid #2a2f45;">🟢 Strongest</td>
        </tr>
        <tr><td style="padding: 8px; border-bottom:1px solid #2a2f45;">Bathrooms</td>
            <td style="padding: 8px; border-bottom:1px solid #2a2f45;">0.452</td>
            <td style="padding: 8px; border-bottom:1px solid #2a2f45;">🟢 Strong</td>
        </tr>
        <tr><td style="padding: 8px; border-bottom:1px solid #2a2f45;">Bedrooms</td>
            <td style="padding: 8px; border-bottom:1px solid #2a2f45;">0.399</td>
            <td style="padding: 8px; border-bottom:1px solid #2a2f45;">🟡 Moderate</td>
        </tr>
        <tr><td style="padding: 8px;">Zipcode</td>
            <td style="padding: 8px;">0.070</td>
            <td style="padding: 8px;">🔴 Weak (target encoded)</td>
        </tr>
    </table>
</div>

<!-- MODEL ARCHITECTURES - VISUAL VERSION -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">🧠 Model Architectures</h2>
        <div style="background: #0b0f1c; border-radius: 16px; padding: 1.2rem; margin-bottom: 20px; border-left: 4px solid #4CAF50;">
        <h3 style="color: #4CAF50; margin-top: 0; margin-bottom: 15px;">📊 1️⃣ Tabular Only Model</h3>
        <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 8px; margin: 15px 0;">
            <span style="background: #1e2338; padding: 5px 12px; border-radius: 20px; font-size: 0.75rem;">Input (4)</span>
            <span style="color: #FFD93D;">→</span>
            <span style="background: #1e2338; padding: 5px 12px; border-radius: 20px; font-size: 0.75rem;">Dense(256)</span>
            <span style="color: #FFD93D;">→</span>
            <span style="background: #1e2338; padding: 5px 12px; border-radius: 20px; font-size: 0.75rem;">BN</span>
            <span style="color: #FFD93D;">→</span>
            <span style="background: #1e2338; padding: 5px 12px; border-radius: 20px; font-size: 0.75rem;">Dropout(0.3)</span>
            <span style="color: #FFD93D;">→</span>
            <span style="background: #1e2338; padding: 5px 12px; border-radius: 20px; font-size: 0.75rem;">Dense(128)</span>
            <span style="color: #FFD93D;">→</span>
            <span style="background: #1e2338; padding: 5px 12px; border-radius: 20px; font-size: 0.75rem;">BN</span>
            <span style="color: #FFD93D;">→</span>
            <span style="background: #1e2338; padding: 5px 12px; border-radius: 20px; font-size: 0.75rem;">Dropout(0.2)</span>
            <span style="color: #FFD93D;">→</span>
            <span style="background: #1e2338; padding: 5px 12px; border-radius: 20px; font-size: 0.75rem;">Dense(64)</span>
            <span style="color: #FFD93D;">→</span>
            <span style="background: #4CAF50; padding: 5px 12px; border-radius: 20px; font-size: 0.75rem; color: white;">Dense(1)</span>
        </div>
        <div style="display: flex; gap: 20px; margin-top: 10px;">
            <div><strong>📦 Parameters:</strong> 44,033</div>
            <div><strong>🎯 Best Val MAE:</strong> 0.3219 (log scale)</div>
        </div>
    </div>
    <div style="background: #0b0f1c; border-radius: 16px; padding: 1.2rem; margin-bottom: 20px; border-left: 4px solid #FF9800;">
        <h3 style="color: #FF9800; margin-top: 0; margin-bottom: 15px;">🖼️ 2️⃣ Image Only Model</h3>
        <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 8px; margin: 15px 0;">
            <span style="background: #1e2338; padding: 5px 12px; border-radius: 20px; font-size: 0.75rem;">Input (2048)</span>
            <span style="color: #FFD93D;">→</span>
            <span style="background: #1e2338; padding: 5px 12px; border-radius: 20px; font-size: 0.75rem;">Dense(256)</span>
            <span style="color: #FFD93D;">→</span>
            <span style="background: #1e2338; padding: 5px 12px; border-radius: 20px; font-size: 0.75rem;">BN</span>
            <span style="color: #FFD93D;">→</span>
            <span style="background: #1e2338; padding: 5px 12px; border-radius: 20px; font-size: 0.75rem;">Dropout(0.4)</span>
            <span style="color: #FFD93D;">→</span>
            <span style="background: #1e2338; padding: 5px 12px; border-radius: 20px; font-size: 0.75rem;">Dense(128)</span>
            <span style="color: #FFD93D;">→</span>
            <span style="background: #1e2338; padding: 5px 12px; border-radius: 20px; font-size: 0.75rem;">BN</span>
            <span style="color: #FFD93D;">→</span>
            <span style="background: #1e2338; padding: 5px 12px; border-radius: 20px; font-size: 0.75rem;">Dropout(0.3)</span>
            <span style="color: #FFD93D;">→</span>
            <span style="background: #1e2338; padding: 5px 12px; border-radius: 20px; font-size: 0.75rem;">Dense(64)</span>
            <span style="color: #FFD93D;">→</span>
            <span style="background: #FF9800; padding: 5px 12px; border-radius: 20px; font-size: 0.75rem; color: white;">Dense(1)</span>
        </div>
        <div style="display: flex; gap: 20px; margin-top: 10px;">
            <div><strong>📦 Parameters:</strong> 567,297</div>
            <div><strong>🎯 Best Val MAE:</strong> 0.5928 (log scale)</div>
        </div>
    </div>    <!-- Fusion Model Card -->
    <div style="background: #0b0f1c; border-radius: 16px; padding: 1.2rem; margin-bottom: 10px; border-left: 4px solid #FFD93D;">
        <h3 style="color: #FFD93D; margin-top: 0; margin-bottom: 15px;">🔀 3️⃣ Fusion Model (Best Performer)</h3>
        <div style="margin-bottom: 15px;">
            <div style="color: #4CAF50; margin-bottom: 8px;">📊 Tabular Branch:</div>
            <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 6px; margin-left: 15px;">
                <span style="background: #1e2338; padding: 4px 10px; border-radius: 16px; font-size: 0.7rem;">Input(4)</span>
                <span style="color: #FFD93D;">→</span>
                <span style="background: #1e2338; padding: 4px 10px; border-radius: 16px; font-size: 0.7rem;">Dense(256)</span>
                <span style="color: #FFD93D;">→</span>
                <span style="background: #1e2338; padding: 4px 10px; border-radius: 16px; font-size: 0.7rem;">BN+Drop(0.3)</span>
                <span style="color: #FFD93D;">→</span>
                <span style="background: #1e2338; padding: 4px 10px; border-radius: 16px; font-size: 0.7rem;">Dense(128)</span>
                <span style="color: #FFD93D;">→</span>
                <span style="background: #1e2338; padding: 4px 10px; border-radius: 16px; font-size: 0.7rem;">BN+Drop(0.2)</span>
                <span style="color: #FFD93D;">→</span>
                <span style="background: #1e2338; padding: 4px 10px; border-radius: 16px; font-size: 0.7rem;">Dense(64)</span>
            </div>
        </div>
        <div style="margin-bottom: 15px;">
            <div style="color: #FF9800; margin-bottom: 8px;">🖼️ Image Branch:</div>
            <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 6px; margin-left: 15px;">
                <span style="background: #1e2338; padding: 4px 10px; border-radius: 16px; font-size: 0.7rem;">Input(2048)</span>
                <span style="color: #FFD93D;">→</span>
                <span style="background: #1e2338; padding: 4px 10px; border-radius: 16px; font-size: 0.7rem;">Dense(512)</span>
                <span style="color: #FFD93D;">→</span>
                <span style="background: #1e2338; padding: 4px 10px; border-radius: 16px; font-size: 0.7rem;">BN+Drop(0.4)</span>
                <span style="color: #FFD93D;">→</span>
                <span style="background: #1e2338; padding: 4px 10px; border-radius: 16px; font-size: 0.7rem;">Dense(128)</span>
                <span style="color: #FFD93D;">→</span>
                <span style="background: #1e2338; padding: 4px 10px; border-radius: 16px; font-size: 0.7rem;">BN+Drop(0.3)</span>
                <span style="color: #FFD93D;">→</span>
                <span style="background: #1e2338; padding: 4px 10px; border-radius: 16px; font-size: 0.7rem;">Dense(64)</span>
            </div>
        </div>
        <div style="margin-bottom: 15px;">
            <div style="color: #FFD93D; margin-bottom: 8px;">🔀 Fusion Layers:</div>
            <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 6px; margin-left: 15px;">
                <span style="background: #1e2338; padding: 4px 10px; border-radius: 16px; font-size: 0.7rem;">Concat(64+64)</span>
                <span style="color: #FFD93D;">→</span>
                <span style="background: #1e2338; padding: 4px 10px; border-radius: 16px; font-size: 0.7rem;">Dense(128)</span>
                <span style="color: #FFD93D;">→</span>
                <span style="background: #1e2338; padding: 4px 10px; border-radius: 16px; font-size: 0.7rem;">BN+Drop(0.3)</span>
                <span style="color: #FFD93D;">→</span>
                <span style="background: #1e2338; padding: 4px 10px; border-radius: 16px; font-size: 0.7rem;">Dense(64)</span>
                <span style="color: #FFD93D;">→</span>
                <span style="background: #1e2338; padding: 4px 10px; border-radius: 16px; font-size: 0.7rem;">BN+Drop(0.2)</span>
                <span style="color: #FFD93D;">→</span>
                <span style="background: #1e2338; padding: 4px 10px; border-radius: 16px; font-size: 0.7rem;">Dense(32)</span>
                <span style="color: #FFD93D;">→</span>
                <span style="background: #FFD93D; padding: 4px 10px; border-radius: 16px; font-size: 0.7rem; color: #0b0f1c; font-weight: bold;">Dense(1)</span>
            </div>
        </div>
        <div style="display: flex; gap: 20px; margin-top: 15px;">
            <div><strong>📦 Parameters:</strong> 1,197,185</div>
            <div><strong>🎯 Best Val MAE:</strong> 0.2990 (log scale)</div>
            <div><strong>🏆 Status:</strong> Best Performer</div>
        </div>
    </div>
</div>

<!-- RESULTS -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📊 Evaluation Results</h2>
    <table style="width:100%; border-collapse: collapse; color: #ddd;">
        <tr style="background: #0b0f1c;">
            <th style="padding: 12px; text-align: left;">Model</th>
            <th style="padding: 12px; text-align: left;">MAE</th>
            <th style="padding: 12px; text-align: left;">RMSE</th>
            <th style="padding: 12px; text-align: left;">MAPE</th>
        </tr>
        <tr><td style="padding: 10px; border-bottom:1px solid #2a2f45;">Tabular Only</td>
            <td style="padding: 10px; border-bottom:1px solid #2a2f45;">$171,756</td>
            <td style="padding: 10px; border-bottom:1px solid #2a2f45;">$248,406</td>
            <td style="padding: 10px; border-bottom:1px solid #2a2f45;">33.4%</td>
        </tr>
        <tr><td style="padding: 10px; border-bottom:1px solid #2a2f45;">Image Only</td>
            <td style="padding: 10px; border-bottom:1px solid #2a2f45;">$428,926</td>
            <td style="padding: 10px; border-bottom:1px solid #2a2f45;">$953,258</td>
            <td style="padding: 10px; border-bottom:1px solid #2a2f45;">112.7%</td>
        </tr>
        <tr><td style="padding: 10px;">Fusion (Combined)</td>
            <td style="padding: 10px;">$201,821</td>
            <td style="padding: 10px;">$308,304</td>
            <td style="padding: 10px;"><strong>39.9%</strong></td>
        </tr>
    </table>
    <p style="margin-top: 15px;">✅ <strong>Tabular Model achieves best MAE ($171k)</strong> &nbsp;|&nbsp; ✅ <strong>Fusion proves multimodal concept</strong></p>
</div>

<!-- TRAINING DETAILS -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">⚙️ Training Details</h2>
    <ul>
        <li><strong>Phase 1 (Frozen CNN):</strong> 50 epochs, LR=0.001→0.0005, Best Val MAE=0.3510</li>
        <li><strong>Phase 2 (Fine-Tune):</strong> 40 epochs, LR=0.0001→2.5e-5, Best Val MAE=0.2990</li>
        <li><strong>Loss Function:</strong> Huber (delta=1.0) - Robust to outliers</li>
        <li><strong>Optimizer:</strong> Adam with gradient clipping (clipnorm=1.0)</li>
        <li><strong>Regularization:</strong> Dropout (0.2-0.5) + Batch Normalization</li>
    </ul>
</div>

<!-- DEPLOYMENT -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">🚀 Deployment – Streamlit App</h2>
    <p>The fine‑tuned fusion model is saved and loaded into a <strong>Streamlit</strong> web app. The app provides:</p>
    <ul>
        <li>📸 Image upload for bedroom, bathroom, kitchen, and frontal views</li>
        <li>📊 Interactive sliders for bedrooms, bathrooms, and area input</li>
        <li>🎯 Real‑time BERT inference for price prediction</li>
        <li>📈 Market analysis with price percentile and confidence intervals</li>
        <li>💡 Pro tips for best prediction accuracy</li>
        <li>🎨 Modern UI with glass‑morphism effect, fully responsive</li>
    </ul>
    <p><strong>Live Demo (Streamlit Cloud):</strong> <em>(add your deployed link here)</em></p>
</div>

<!-- TECH STACK -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">🛠️ Technologies Used</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px;">
        <div><strong>🐍 Python</strong><br>3.9+</div>
        <div><strong>🧠 TensorFlow</strong><br>2.13+</div>
        <div><strong>🖼️ ResNet50</strong><br>Feature Extraction</div>
        <div><strong>📊 Pandas/NumPy</strong><br>Data Processing</div>
        <div><strong>⚡ Streamlit</strong><br>Web Deployment</div>
        <div><strong>🔧 Scikit‑learn</strong><br>Preprocessing & Metrics</div>
    </div>
</div>

<!-- PROJECT STRUCTURE -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📁 Project Structure</h2>
    <pre style="background: #0b0f1c; padding: 1rem; border-radius: 16px; overflow-x: auto; color: #b0c4de;">
house-price-predictor/
├── dataset/
│   ├── HousesDataset/          # 2,140 images (4 per house)
│   └── HousesInfo.txt          # Tabular data (535 records)
├── models/
│   ├── model_tabular_final.keras     # Tabular only model
│   ├── model_fusion_final.keras      # Multimodal fusion model
│   └── scaler.pkl                    # StandardScaler for inference
├── app.py                      # Streamlit application
├── requirements.txt            # Dependencies
├── notebook.ipynb              # Training notebook
└── README.md                   # This file
    </pre>
</div>

<!-- HOW TO RUN -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">⚙️ How to Run Locally</h2>
    <ol style="line-height: 1.7;">
        <li><strong>Clone the repository</strong><br><code>git clone https://github.com/RehmanAhmad333/house-price-predictor.git</code><br><code>cd house-price-predictor</code></li>
        <li><strong>Create virtual environment</strong><br><code>python -m venv venv</code><br><code>venv\Scripts\activate</code> (Windows) / <code>source venv/bin/activate</code> (Mac/Linux)</li>
        <li><strong>Install dependencies</strong><br><code>pip install -r requirements.txt</code></li>
        <li><strong>Place model files</strong><br>Add <code>model_fusion_final.keras</code>, <code>model_tabular_final.keras</code>, and <code>housing_clean.csv</code> in root directory</li>
        <li><strong>Run Streamlit app</strong><br><code>streamlit run app.py</code></li>
        <li>Open your browser at <code>http://localhost:8501</code></li>
    </ol>
</div>

<!-- REQUIREMENTS.TXT -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">📦 requirements.txt</h2>
    <pre style="background: #0b0f1c; padding: 1rem; border-radius: 16px;">
streamlit==1.29.0
tensorflow-cpu==2.13.0
numpy==1.23.5
pandas==2.0.3
Pillow==10.0.0
scikit-learn==1.3.0
h5py==3.9.0
    </pre>
</div>

<!-- OPTIMIZATION TECHNIQUES -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">🔥 Optimization Techniques</h2>
    <ul>
        <li><strong>Feature Extraction Caching:</strong> ResNet50 features extracted once (5 min) vs every epoch (45 min) → 5x faster training</li>
        <li><strong>Two-Phase Training:</strong> Phase 1 frozen CNN, Phase 2 fine-tune last 20 layers</li>
        <li><strong>Target Encoding:</strong> Converted zipcodes to mean price per area (improved from 0.07 correlation)</li>
        <li><strong>Log Transformation:</strong> Normalized right-skewed price distribution</li>
        <li><strong>Huber Loss:</strong> Robust to outliers, combines MAE + MSE</li>
        <li><strong>Gradient Clipping:</strong> Prevents exploding gradients (clipnorm=1.0)</li>
    </ul>
</div>

<!-- CHALLENGES SOLVED -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">⚡ Challenges & Solutions</h2>
    <ul>
        <li><strong>Small dataset (535 houses) causing overfitting</strong> – Aggressive dropout (0.3-0.5), batch normalization, two-phase training with early stopping</li>
        <li><strong>Images alone performing poorly (MAE $428k)</strong> – Fusion model combines tabular data with images for better context</li>
        <li><strong>Large model size for Streamlit Cloud</strong> – Used <code>tensorflow-cpu</code> instead of full TensorFlow, model caching with <code>@st.cache_resource</code></li>
        <li><strong>Skewed price distribution</strong> – Applied log transformation to normalize target variable</li>
        <li><strong>Zipcode correlation very weak (0.07)</strong> – Implemented target encoding (mean price per zipcode) to capture location value</li>
        <li><strong>White screen on Streamlit deployment</strong> – Fixed by clearing browser cache, using incognito mode, and proper CSS scoping</li>
    </ul>
</div>

<!-- KEY INSIGHTS -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">💡 Key Insights</h2>
    <ul>
        <li>📊 <strong>Tabular data alone (MAE $171k) outperforms fusion (MAE $202k)</strong> on small dataset – images add noise without sufficient data</li>
        <li>🖼️ <strong>Images alone are insufficient</strong> for price prediction (MAE $428k, MAPE 112%) – visual features too complex</li>
        <li>🔀 <strong>Fusion proves multimodal concept works</strong> – with more data (2000+ houses), fusion would likely outperform tabular</li>
        <li>📍 <strong>Target encoding improved zipcode relevance</strong> from 0.07 correlation to meaningful feature</li>
        <li>⚡ <strong>Feature extraction caching is critical</strong> – 5x speedup (45 min → 9 min total training)</li>
        <li>📈 <strong>Area is strongest predictor (0.49 correlation)</strong> – square footage dominates price</li>
    </ul>
</div>

<!-- FUTURE IMPROVEMENTS -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0;">
    <h2 style="color: #FFD93D; margin-top: 0;">🔮 Future Improvements</h2>
    <ul>
        <li>Fine-tune last 50 ResNet layers instead of 20 for better feature extraction</li>
        <li>Add data augmentation (rotation, flip, brightness) for image variety</li>
        <li>Implement attention mechanism for weighted feature fusion</li>
        <li>Add more tabular features (year built, lot size, garage, pool)</li>
        <li>Deploy as REST API with FastAPI for integration with other systems</li>
        <li>Add model explainability using SHAP or LIME</li>
        <li>Collect more data (target 2000+ houses) for better fusion performance</li>
        <li>Experiment with Vision Transformers (ViT) instead of ResNet50</li>
    </ul>
</div>

<!-- AUTHOR -->
<div style="background: #1e2338; border-radius: 24px; padding: 1.5rem; margin: 30px 0; text-align: center;">
    <h2 style="color: #FFD93D; margin-top: 0;">👤 Author</h2>
    <p><strong>Rehman Ahmad Cheema</strong><br>
    🔗 <a href="https://github.com/RehmanAhmad333" target="_blank" style="color: #FFD93D;">GitHub</a> • 
    💼 <a href="https://www.linkedin.com/in/rehman-ahmad-9a5b17384/" style="color: #FFD93D;">LinkedIn</a></p>
    <p style="margin-top: 10px;">AI/ML Engineer | Deep Learning Specialist | Multimodal AI Enthusiast</p>
</div>

<!-- FOOTER -->
<div style="text-align: center; padding: 1rem 0; border-top: 1px solid #2a2f45; margin-top: 20px; color: #6f7a9e;">
    <p>Built with dedication by <strong>Rehman Ahmad Cheema</strong> – AI Developer Intern</p>
    <p style="font-size: 0.8rem;">© 2024 Multimodal House Price Predictor | MIT License</p>
</div>

</div>
</body>
</html>
