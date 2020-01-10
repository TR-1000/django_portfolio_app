import os
from dotenv import load_dotenv
load_dotenv()

def email_address_processors(request):
    email_address = os.getenv('TO_EMAIL_ADDRESS')
    return {'email_address': email_address}
