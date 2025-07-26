import pandas as pd
import streamlit as st
from openai import OpenAI

df = pd.read_csv("C:/Users/Vivek/Mobile Recommendation/flipkart_mobile_dataset1.csv")
df['Prices'] = df['Prices'].str.replace('₹', '').str.replace(',', '').astype(int)

st.title("Best Phone Recommendation")
st.markdown("Get the best phone based on your priorities")

budget = st.slider("Select your budget (₹)", 5000, 200000, 20000, 1000)
priority = st.selectbox("What is your top priority?", ["Camera", "Battery", "Performance", "Overall"])

filtered_df = df[df['Prices'] <= budget]


if priority != "Overall" and priority in df.columns:
    filtered_df = filtered_df.sort_values(by=priority, ascending=False)
else:
    filtered_df = filtered_df.sort_values(by="Prices", ascending=False)

results = filtered_df.head(10)

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)


@st.cache_data(show_spinner=True)
def get_openrouter_explanation(description):
    prompt = f"Explain why this phone is a good choice:\n\n{description}"
    try:
        response = client.chat.completions.create(
            model="google/gemma-3n-e4b-it:free",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ OpenRouter error: {e}"
    

for idx, row in results.iterrows():
    st.subheader(row['Product Name'])
    st.write(f"**Price:** ₹{row['Prices']}")
    st.write(f"Description: {row['Description']}")
    st.write(f"[View on Flipkart]({row['Link']})")
    explanation = get_openrouter_explanation(row['Description'])
    st.success(f"💬 Why this phone? {explanation}")
    st.markdown("---")
