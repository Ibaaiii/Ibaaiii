
import os
import requests
import re
import sys

# Configuration
HTB_API_TOKEN = os.environ.get('HTB_API_TOKEN')
HTB_USER_ID = os.environ.get('HTB_USER_ID') # You need to set this in repo secrets
README_PATH = '../README.md'

def get_htb_stats():
    if not HTB_API_TOKEN or not HTB_USER_ID:
        print("[-] HTB_API_TOKEN or HTB_USER_ID not set. Skipping API fetch.")
        return None

    headers = {'Authorization': f'Bearer {HTB_API_TOKEN}', 'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.hackthebox.com/api/v4/profile/member/{HTB_USER_ID}'
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get('profile', {})
    except Exception as e:
        print(f"[-] Error fetching HTB stats: {e}")
        return None

def update_readme(stats):
    if not stats:
        return

    with open(README_PATH, 'r') as f:
        content = f.read()

    # Data to inject
    rank = stats.get('rank', 'Unknown')
    system_owns = stats.get('system_owns', 0)
    user_owns = stats.get('user_owns', 0)
    points = stats.get('points', 0)

    # Regex patterns for replacement
    patterns = {
        r'(\*\*Rank:\*\* ).*': f'\\1{rank}',
        r'(\*\*System Owns:\*\* ).*': f'\\1{system_owns}',
        r'(\*\*User Owns:\*\* ).*': f'\\1{user_owns}',
        r'(\*\*Points:\*\* ).*': f'\\1{points}',
    }

    new_content = content
    for pattern, replacement in patterns.items():
        new_content = re.sub(pattern, replacement, new_content)

    if new_content != content:
        with open(README_PATH, 'w') as f:
            f.write(new_content)
        print("[+] README.md updated with new stats.")
    else:
        print("[*] No changes needed for README.md.")

if __name__ == "__main__":
    stats = get_htb_stats()
    if stats:
        update_readme(stats)
    else:
        # Fallback: Just print that we are done (or fail silently)
        pass
