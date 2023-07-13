import os
import shutil
import urllib
import uuid

from dotenv import load_dotenv
from core.doc_service import DocService

load_dotenv()

HOME = os.path.dirname(os.path.abspath(__file__))

if os.path.exists(os.path.join(HOME, "chroma_storage")):
    shutil.rmtree(os.path.join(HOME, "chroma_storage"))

os.makedirs(os.path.join(HOME, "chroma_storage"), exist_ok=True)

uuid_memory = str(uuid.uuid4())
temp_save_directory = os.path.join(HOME, 'dataset')

filename = "example_cv_file.docx"  # add the file name here
data_path = os.path.join(temp_save_directory, filename)

cht_mdl = DocService(data_path, persist_directory=os.path.join(HOME, "chroma_storage", uuid_memory))
cht_mdl.fetch_document()
cht_mdl.create_vector_index()

while True:
    query = input("input the text here: ")
    output = cht_mdl.query_document(prompt=query)
    print(output)
