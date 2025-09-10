from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DF_T2SEV4EYSJTJMT3HVC8I")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_t2sev4eysjtjmt3hvc8i")
        print(f"Uploaded {data.num_rows} rows to t2sev4eysjtjmt3hvc8i")
        
    save_state("t2sev4eysjtjmt3hvc8i", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
