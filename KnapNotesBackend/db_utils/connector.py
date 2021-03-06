from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

LOGIN_DATA_FILE_NAME = "/home/liath/PycharmProjects/KnapNotesBackend/local_only_assets/db-auth-data"
DB_URL_FORMAT = "mysql+pymysql://{0}@localhost:3306/kndb?charset=utf8mb4"
ECHO = False

with open(LOGIN_DATA_FILE_NAME, "r") as file:
	login_data = file.read()
login_data = login_data.strip()

DB_ENGINE = create_engine(DB_URL_FORMAT.format(login_data), echo=ECHO)
SESSION_FACTORY = sessionmaker(bind=DB_ENGINE)


def create_session():
	return SESSION_FACTORY()
