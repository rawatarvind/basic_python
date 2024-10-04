import os

def append_to_sudoers(username):
    # The commands to be appended in the sudoers file.
    sudoer_entries = [ 
        f"{username} ALL=NOPASSWD: /usr/bin/systemctl restart *\n",
        f"{username} ALL=NOPASSWD: /usr/bin/systemctl start onedrive@alex.service\n",
        f"{username} ALL=NOPASSWD: /usr/bin/systemctl stop onedrive@alex.service\n",
        f"{username} ALL=NOPASSWD: /usr/bin/mount *\n",
        f"{username} ALL=NOPASSWD: /usr/bin/umount *\n",
        f"{username} ALL=NOPASSWD: /usr/bin/tail *\n",
        f"{username} ALL=NOPASSWD: /usr/bin/less *\n",
        f"{username} ALL=NOPASSWD: /usr/bin/sh *\n",
    ]
    
    sudoers_file = "/etc/sudoers"

    try:
        # Check if the script is run as root
        if os.geteuid() != 0:
            raise PermissionError("Script must run as root user.")

        # Read the current content of the sudoers file
        with open(sudoers_file, 'r') as f:
            sudoers_content = f.read()

        # Check for entries that already exist
        existing_entries = []
        for entry in sudoer_entries:
            if entry in sudoers_content:
                print(f"The entry '{entry.strip()}' already exists in sudoers.")
                existing_entries.append(entry)
        
        # Append only the new entries
        new_entries = [entry for entry in sudoer_entries if entry not in existing_entries]
        if new_entries:
            with open(sudoers_file, 'a') as file:
                file.writelines(new_entries)
                for entry in new_entries:
                    print(f"Added entry: {entry.strip()}")
        else:
            print("No new entries to add.")

    except PermissionError as e:
        print(f"Permission denied: {e}")
    except IOError as e:
        print(f"IO error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Ask for the username to add to the sudoers.
    username = input("Enter the username: ")
    append_to_sudoers(username)
