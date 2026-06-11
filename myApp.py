import streamlit as st
from predictImage import predict

st.set_page_config(page_title="Image Classifier", layout="centered")

st.title("Image Classifier")
st.write("Upload an image and the model will predict whether it's a cat, dog, or horse.")

if 'probabilities' not in st.session_state:
    st.session_state.probabilities = []

def handleChange():
    file = st.session_state.file_uploader_key
    if file is not None:
        st.session_state.probabilities = predict(file)

st.file_uploader(
    "Upload a PNG or JPEG image",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=False,
    key="file_uploader_key",
    on_change=handleChange,
)

if st.session_state.probabilities:
    names = ['Cat', 'Dog', 'Horse']
    colors = ['#534AB7', '#1D9E75', '#D85A30']

    winner = names[max(range(3), key=lambda i: st.session_state.probabilities[i])]

    st.markdown(f"### Prediction: **{winner}**")
    st.caption("Confidence breakdown")

    for name, prob, color in zip(names, st.session_state.probabilities, colors):
        pct = prob * 100
        try:
            st.markdown(f"""
            <div style="margin-bottom:14px">
                <div style="display:flex; justify-content:space-between; font-size:14px; margin-bottom:4px">
                    <span>{name}</span>
                    <span style="font-weight:500">{pct:.1f}%</span>
                </div>
                <div style="background:#f0f0f0; border-radius:99px; height:10px; overflow:hidden">
                    <div style="width:{pct}%; background:{color}; height:100%; border-radius:99px; transition:width 0.5s ease"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            print("Error occurred",e)
            st.text(f"Error occurred :{e}")
