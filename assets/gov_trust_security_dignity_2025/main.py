from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_GOV_INT@DF_GOV_TDG_2025")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_gov_trust_security_dignity_2025")
        print(f"Uploaded {data.num_rows} rows to gov_trust_security_dignity_2025")
        
    save_state("gov_trust_security_dignity_2025", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
