import os

def delete_user_files(username):
    # Command Injection
    os.popen(f"rm -rf /var/users/{username}").read()

def backup_db(db_name):
    # Command Injection
    os.popen("mysqldump -u root " + db_name).read()
