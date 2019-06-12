# tavern_utils.py

import shutil

def save_response(response):
    with open('BC620 Core Stack_2.0.9.bin', 'wb')as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    