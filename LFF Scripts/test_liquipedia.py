import urllib.request
import json
import gzip
import re
import sys

# Configure UTF-8 stdout
if sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

url = "https://liquipedia.net/fortnite/api.php?action=parse&page=Portal:Transfers&format=json"
req = urllib.request.Request(
    url,
    headers={
        "User-Agent": "LFF-App/1.0 (martin@lff-fortnite.fr)",
        "Accept-Encoding": "gzip"
    }
)

try:
    with urllib.request.urlopen(req) as resp:
        raw = resp.read()
        decompressed = gzip.decompress(raw).decode("utf-8")
        data = json.loads(decompressed)
        html = data["parse"]["text"]["*"]
        
        # Save HTML for analysis
        with open("liquipedia_transfers_sample.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("HTML saved, length:", len(html))
        
        # Look for transfer rows
        # Liquipedia transfers usually have class="divCell" or "transfer-row" or "divRow"
        div_rows = re.findall(r'<div class="divRow[^"]*">(.*?)</div>\s*(?=<div class="divRow|$)', html, re.DOTALL)
        print("divRows found:", len(div_rows))
        
        # Also check table rows
        tr_rows = re.findall(r'<tr[^>]*>(.*?)</tr>', html, re.DOTALL)
        print("tr rows found:", len(tr_rows))

        # Let's inspect raw cells of Row 0
        if div_rows:
            raw_cells = re.findall(r'<div class="divCell[^"]*">(.*?)</div>', div_rows[0], re.DOTALL)
            for idx, rc in enumerate(raw_cells):
                print(f"--- Cell {idx} ---")
                print(rc)
            
except Exception as e:
    print("Error:", e)
