import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

st.title("Sentiment Analyzer")
text = st.text_area("Enter some text")

if st.button("Analyze") and text:
    scores = sia.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        st.success("Positive 😊")
    elif compound <= -0.05:
        st.error("Negative 😞")
    else:
        st.info("Neutral 😐")

    st.write("Score:", compound)