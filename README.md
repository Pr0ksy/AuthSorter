# AuthSorter

AuthSorter is a CMD-based tool designed to efficiently extract and organize login credentials from text files. It scans directories for specific files containing email:password pairs, URLs, and Discord tokens, then sorts them into categorized files for easier management.

1.
```sh
   git clone https://github.com/YourUsername/AuthSorter.git
   cd AuthSorter
  ```
2. Install required dependencies:
```sh
  pip install -r requirements.txt
  ```
3. Run the script:
```sh
   python sorter.py
  ```

# Usage

1. Run sorter.py

2. Choose a directory containing the target files

3. Wait for the script to process and generate sorted files

4. Output files will be saved in the root folder where sorter.py is located

```sh
📂 AuthSorter
 ├── sorter.py
 ├── spotify.txt
 ├── mozzartbet.txt
 ├── SortedDiscordTokens.txt
  ```
