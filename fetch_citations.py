import urllib.request
import re
import os

url = "https://scholar.google.com/citations?user=dAy6c40AAAAJ"
# Disguise the request as a normal web browser
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')

# Find ALL instances of <td class="gsc_rsb_std">number</td>
matches = re.findall(r'<td class="gsc_rsb_std">(\d+)</td>', html)

# The table has multiple values. 
# Index 0 is Total Citations, Index 2 is Total h-index.
if len(matches) >= 3:
    citations = matches[0]
    h_index = matches[2]
    
    # Ensure the _data directory exists
    os.makedirs('_data', exist_ok=True)
    
    # Write the result to a YAML file for Jekyll to use
    with open('_data/scholar.yml', 'w') as f:
        f.write(f"citations: {citations}\n")
        f.write(f"h_index: {h_index}\n")
        
    print(f"Successfully updated metrics -> Citations: {citations}, h-index: {h_index}")
else:
    print("Could not find the citation and h-index counts.")