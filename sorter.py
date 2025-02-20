import os
import re
import tkinter as tk
from tkinter import filedialog
from collections import defaultdict
import multiprocessing

EMAIL_PASS_REGEX = re.compile(r"USER:\s*(\S+)\s*PASS:\s*(\S+)")
URL_REGEX = re.compile(r"URL:\s*(https?://([\w\.-]+))")
DISCORD_TOKEN_REGEX = re.compile(r"([A-Za-z\d]{24}\.[A-Za-z\d]{6}\.[A-Za-z\d_-]{27})")

def select_folder(queue):
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory(title="Izaberi folder sa podacima")
    queue.put(folder_selected)

def process_files(folder):
    sorted_data = defaultdict(list)
    discord_tokens = []

    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)

            if file == "All Passwords.txt":
                with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                    lines = f.readlines()

                current_url = None
                for line in lines:
                    url_match = URL_REGEX.search(line)
                    pass_match = EMAIL_PASS_REGEX.search(line)

                    if url_match:
                        current_url = url_match.group(2).split(".")[-2]  # domen (npr. spotify)
                    if pass_match and current_url:
                        sorted_data[current_url].append(f"{pass_match.group(1)}:{pass_match.group(2)}")

            if file == "DiscordTokens.txt":
                with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                    for line in f:
                        match = DISCORD_TOKEN_REGEX.search(line)
                        if match:
                            discord_tokens.append(match.group(1))

    output_folder = os.path.join(os.getcwd(), "Sorted")
    os.makedirs(output_folder, exist_ok=True)

    for site, entries in sorted_data.items():
        output_file = os.path.join(output_folder, f"{site}.txt")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(entries))

    if discord_tokens:
        with open(os.path.join(output_folder, "SortedDiscordTokens.txt"), "w", encoding="utf-8") as f:
            f.write("\n".join(discord_tokens))

    print(f"\n✅ Sorting completed! Files are saved in: {output_folder}\n")

if __name__ == "__main__":
    print("By Pr0ksy")
    print(" ")
    print("Do you want to select a folder or enter the path manually?")
    print(" ")
    print("[1] Select a folder using File Explorer")
    print("[2] Enter the path manually")
    print(" ")
    choice = input("👉 Enter 1 or 2:").strip()

    if choice == "1":
        print("\n📂 Opening File Explorer, please select a folder...")

        queue = multiprocessing.Queue()
        process = multiprocessing.Process(target=select_folder, args=(queue,))
        process.start()
        process.join()

        folder_path = queue.get()
    elif choice == "2":
        folder_path = input("\n📌 Enter the path to the folder: ").strip()
    else:
        print("\n❌ Invalid input! Please restart the program.")
        exit()

    if folder_path and os.path.isdir(folder_path):
        print(f"\n✅ Selected folder: {folder_path}\n")
        process_files(folder_path)
    else:
        print("\n❌ Error: Folder does not exist. Try again.")
