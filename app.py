import streamlit as st
import joblib
v=joblib.load("vectorizer.jb")
model=joblib.load("lr_model.jb")
st.title("Fake News Detector")
st.write("Give a News Article to check if it's Fake or Real")
news=st.text_area("News Article :")
if st.button("Check News"):
    if news.strip():
        a=v.transform([news])
        predict=model.predict(a)
        if predict[0]==1:
            st.success("The News is Real!")
        else:
            st.error("This News is Fake")
    else:
        st.warning("Please provide an article to analyse.")

