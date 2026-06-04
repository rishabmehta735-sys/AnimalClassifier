import streamlit as st

st.title("Image Classifier")

st.text("This is an image classifier neural network model which can read an image and will tell whether" \
"" \
" its a Cat,Dog or a Horse. Probabilities will get displayed. ",width="stretch",text_alignment="justify",)


def handleChange():
    file = st.session_state.file_uploader_key
    print("IMAGE", file)

file = st.file_uploader(
    "upload file",
    type=["image/png", "image/jpeg"],  # must be a list
    accept_multiple_files=False,
    key="file_uploader_key",           # key needed to access via session_state
    on_change=handleChange,            # just pass function reference, no ()
    disabled=False,
    label_visibility="visible"
)

# print(file)