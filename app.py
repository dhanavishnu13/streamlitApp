import streamlit as st
#title 
st.title('Text Detection & Layout Analysis')
#uploading file
file = st.file_uploader(label='Upload your document here',type=['png','jpg','jpeg','pdf'])
button = st.button('Confirm')
if button and file is not None:
    if file.type=="image/png" or file.type=="image/jpg" or file.type=="image/jpeg":
      parserIMG(file)
      text_detection(file)
    elif file.type == "application/pdf":
      parserPDF(file)
