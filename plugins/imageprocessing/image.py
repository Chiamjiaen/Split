try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os
import time
from . import nanonets
pytesseract.pytesseract.tesseract_cmd = "tesseract"
os.environ["TESSDATA_PREFIX"] = os.getcwd() + "/tessdata/"

# downloads the image into a file
def imageHandler(update, context):
  # if conditional at the start to check for integer
  print("image upload start")
  file = update.message.photo[-1].get_file()
  if update.message.caption is None:
    photocaption = "1"
  else:
    photocaption = update.message.caption
  persons = nanonets.parseAmount(photocaption)
  print(persons)
  # print ("file_id: " + str(update.message.photo.file_id))
  file.download('images/image.jpg')
  print("Image loaded successfully!\n")
  total_amt = nanonets.nanonetOcr()
  # get user input integer
  individual_amt = total_amt/persons
  indiv_amt_str = "each person pays $" + str(individual_amt)
  print(indiv_amt_str)
  update.message.reply_text(indiv_amt_str)
  # imageProcessing()

# processes image
def imageProcessing():
  print(pytesseract.get_languages(config=''))
  tic = time.perf_counter()
  print(pytesseract.image_to_string(Image.open('images/image.jpg'), lang='eng'))  
  toc = time.perf_counter()
  print(f"OCR took {toc - tic:0.4f} seconds")