import streamlit as st
from transformers import BertTokenizer, BertForSequenceClassification
import torch

 
st.set_page_config(
    page_title="News Topic Classifier",
    page_icon="📰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

 
st.markdown("""
<style>
    /* Reset and base styles with system fonts */
    html, body, [class*="css"] {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #f5f7fc 0%, #eef2f9 100%);
    }
    
    /* Main container */
    div[data-testid="stAppViewContainer"] > div {
        background: rgba(255,255,255,0.85);
        backdrop-filter: blur(10px);
        border-radius: 32px;
        padding: 2rem 2rem 3rem 2rem !important;
        margin: 2rem auto !important;
        max-width: 800px;
        box-shadow: 0 20px 35px -10px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.5);
    }
    
    /* Headings */
    h1 {
        text-align: center;
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        font-size: clamp(2rem, 8vw, 2.8rem);
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    /* Subtitle */
    .stMarkdown p {
        text-align: center;
        color: #4a5568;
        font-size: clamp(0.9rem, 4vw, 1.1rem);
        margin-bottom: 2rem;
    }
    
    /* Input field */
    div[data-testid="stTextInput"] input {
        border-radius: 60px !important;
        border: 1px solid #cbd5e0 !important;
        padding: 12px 20px !important;
        font-size: 1rem !important;
        transition: all 0.2s !important;
    }
    
    div[data-testid="stTextInput"] input:focus {
        border-color: #2a5298 !important;
        box-shadow: 0 0 0 2px rgba(42,82,152,0.2) !important;
    }
    
    /* Button */
    div[data-testid="stButton"] button {
        background: linear-gradient(135deg, #1e3c72, #2a5298) !important;
        color: white !important;
        border: none !important;
        border-radius: 60px !important;
        padding: 0.6rem 1.8rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
        margin-top: 1rem !important;
    }
    
    div[data-testid="stButton"] button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        background: linear-gradient(135deg, #2a5298, #1e3c72) !important;
    }
    
    /* Success message */
    .stAlert {
        background: linear-gradient(135deg, #e8f0ff, #d9e6ff) !important;
        border-radius: 20px !important;
        padding: 1rem !important;
        text-align: center !important;
        margin-top: 1.5rem !important;
        border-left: 5px solid #2a5298 !important;
    }
    
    .stAlert p {
        margin: 0 !important;
        font-size: 1.2rem !important;
        font-weight: 500 !important;
        color: #1e3c72 !important;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        margin-top: 2rem;
        font-size: 0.75rem;
        color: #a0aec0;
    }
    
    /* Mobile adjustments */
    @media (max-width: 768px) {
        div[data-testid="stAppViewContainer"] > div {
            padding: 1.5rem 1.2rem 2rem 1.2rem !important;
            margin: 1rem !important;
        }
        div[data-testid="stButton"] button {
            padding: 0.5rem 1rem !important;
        }
        .stAlert p {
            font-size: 1rem !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# LOAD MODEL 
@st.cache_resource
def load_model():
    # Limit threads for better performance in Streamlit
    torch.set_num_threads(1)  # Here we set it to 1 to avoid potential issues with too many threads in Streamlit
    model = BertForSequenceClassification.from_pretrained("rehmanahmad/news-classifier-bert")
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    return model, tokenizer

model, tokenizer = load_model()

# CATEGORIES  
categories = ["World", "Sports", "Business", "Sci/Tech"]

# UI 
st.markdown("<h1>📰 News Topic Classifier</h1>", unsafe_allow_html=True)
st.markdown("<p>Write any news headline – AI guesses the topic</p>", unsafe_allow_html=True)

headline = st.text_input("", placeholder="e.g., NASA launches new Mars rover", label_visibility="collapsed")

if st.button("🔍 Classify!"):
    if headline.strip() == "":
        st.warning("Please enter a headline first.")
    else:
        # Tokenize
        inputs = tokenizer(
            headline,
            return_tensors='pt',
            padding=True,
            truncation=True,
            max_length=128
        )
        
        # Predict
        with torch.no_grad():
            outputs = model(**inputs)
        
        prediction = torch.argmax(outputs.logits, dim=1).item()
        topic = categories[prediction]
        

        # Show result
        st.success(f"🏷️ Predicted Topic: **{topic}**")

        # Calculate confidence
        probs = torch.softmax(outputs.logits, dim=1)[0]
        confidence = probs[prediction].item() * 100
        st.success(f"Topic: **{topic}** — Confidence: **{confidence:.1f}%**")

st.markdown("<div class='footer'>Built by <strong>Rehman Ahmad Cheema</strong> with 🤗 Transformers • BERT fine‑tuned on news dataset</div>", unsafe_allow_html=True)
