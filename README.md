# AuthManager

AuthManager is a CMD-based tool designed to efficiently extract, organize, and validate login credentials from text files. It scans directories for files containing email:password pairs, URLs, and Discord tokens, then sorts and checks the validity of accounts before organizing them into categorized files for easier management.

1. Clone
```sh
git clone https://github.com/Pr0ksy/AuthManager.git
cd AuthSorter
  ```
2. Install required dependencies:
```sh
pip install -r requirements.txt
  ```
3. Run the script:
```sh
python sorter.py
//
python checker.py
  ```

# Usage Sorter

1. Run sorter.py

2. Choose a directory containing the target files

3. Wait for the script to process and generate sorted files

4. Output files will be saved in the root folder where sorter.py is located


```sh
📂 Sorted
 ├── netflix.txt
 ├── spotify.txt
 ├── mozzartbet.txt
 ├── SortedDiscordTokens.txt
```



# Usage Checker

1. Run checker.py

2. Choose a directory containing the Sorted files

3. Wait for the script to process and check all files

4. Output files will be saved in the Checked folder in subfolders Valid/Invalid where checker.py is located

```sh
📂 Checked
 ├── 📂 Valid
 │   ├── Checked_netflix.txt
 │   ├── Checked_spotify.txt
 │   ├── Checked_mozzartbet.txt
 │   ├── Checked_DiscordTokens.txt
 │
 ├── 📂 Invalid
 │   ├── Checked_netflix.txt
 │   ├── Checked_spotify.txt
 │   ├── Checked_mozzartbet.txt
 │   ├── Checked_DiscordTokens.txt
```
