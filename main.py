import os
import subprocess
import datetime
from dotenv import load_dotenv


load_dotenv()

def backup_azure_postgres(host, db_name, user, password, backup_dir="backups"):

    # create backup folder if not exists
    os.makedirs(backup_dir, exist_ok=True)

    # create filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"{backup_dir}/{db_name}_{timestamp}.backup"

    # set password env variable so pg_dump won't ask for password
    os.environ['PGPASSWORD'] = password

    # build the pg_dump command
    command = [
        "pg_dump",
        "-h", host,
        "-U", user,
        "-d", db_name,
        "-F", "c",       # custom format
        "-f", backup_file
    ]

    try:
        print("Running backup...")
        subprocess.run(command, check=True)
        print(f"Backup successful! File created: {backup_file}")
    
    except subprocess.CalledProcessError:
        print("Backup failed! Check connection or credentials.")
    
    finally:
        # remove password from environment
        del os.environ['PGPASSWORD']

    return backup_file


# --------- USAGE -----------

backup_azure_postgres(
    host=os.getenv("DB_HOST"),
    db_name=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    backup_dir=os.getenv("BACKUP_DIR")
)
