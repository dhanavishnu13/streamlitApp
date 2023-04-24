import streamlit as st
from PIL import Image
import pytesseract
import cv2

def text_detection(img):
  res = Image.open(img)
  res = np.array(res)
  overlay = Image.open(img)
  overlay = np.array(overlay)
  with st.spinner('Processing Text Detection'):
    boxes = pytesseract.image_to_data(res)
    for i,b in enumerate(boxes.splitlines()): 
      if i!=0:
        b = b.split()
        if len(b)==12:
          x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
          cv2.rectangle(overlay,(x-5,y-5),(w+x+5,h+y+5),(185,237,221),-1) 
          #res = cv2.putText(res,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(185,237,221),2)
  new = cv2.addWeighted(overlay, 0.4, res, 1 - 0.4, 0)
  st.subheader("Text Detection")
  st.image(new)

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
