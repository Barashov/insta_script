from dotenv import load_dotenv
import os


load_dotenv()

USER_ID = os.environ.get('USER_ID', 'ok')
