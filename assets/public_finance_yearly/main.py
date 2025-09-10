from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_GOV@DF_GOV_PF_YU")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_public_finance_yearly")
        print(f"Uploaded {data.num_rows} rows to public_finance_yearly")
        
    save_state("public_finance_yearly", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
