# Azure PostgreSQL Database Backup Tool

A Python script to automate backups of Azure PostgreSQL databases using `pg_dump`.

## Features

- 🔄 Automated PostgreSQL database backups
- 📦 Custom format backups for efficient storage and restoration
- 🔐 Secure credential management using `.env` file
- ⏰ Timestamped backup files
- 🛡️ Automatic cleanup of sensitive environment variables

## Prerequisites

- Python 3.x
- PostgreSQL client tools (`pg_dump`)
- Access to an Azure PostgreSQL database

## Installation

1. Clone this repository:
```bash
git clone https://github.com/akshay300799/db_backup.git
cd db_backup
```

2. Install required Python packages:
```bash
pip install python-dotenv
```

3. Install PostgreSQL client tools:
   - **Windows**: Download and install from [PostgreSQL official site](https://www.postgresql.org/download/windows/)
   - **Linux**: `sudo apt-get install postgresql-client`
   - **macOS**: `brew install postgresql`

## Configuration

1. Create a `.env` file in the project root:
```bash
DB_HOST=your-server.postgres.database.azure.com
DB_NAME=your-database-name
DB_USER=your-username
DB_PASSWORD=your-password
BACKUP_DIR=path/to/backup/directory
```

2. Update the values with your Azure PostgreSQL credentials

**Note**: The `.env` file is already added to `.gitignore` and will not be committed to version control.

## Usage

Run the backup script:
```bash
python main.py
```

The script will:
- Create a backup directory if it doesn't exist
- Generate a timestamped backup file (format: `{db_name}_{YYYYMMDD_HHMMSS}.backup`)
- Save the backup in the specified directory

## Backup File Format

Backups are created in PostgreSQL custom format (`-F c`), which provides:
- Compressed backup files
- Selective restoration capabilities
- Better performance for large databases

**Restore Database in pgAdmin — New Database**
Open pgAdmin 4
Connect to your PostgreSQL server
Right-click Databases → Create → Database
Name it (example: restore_test) → Save
Right-click the new database → Restore…
Format: Custom
Filename: choose the .backup file
(Optional) Under Restore Options, enable Clean before restore
Click Restore
Confirm tables/schemas after restore

**Restore Into an Existing Database**
Right-click the database → Restore…
Format: Custom
Select your .backup file
Go to Restore Options
Enable Clean before restore
Click Restore
