from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_KIIBIH@DF_B26")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_pension_contributors_formality_gender")
        print(f"Uploaded {data.num_rows} rows to pension_contributors_formality_gender")
        
    save_state("pension_contributors_formality_gender", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
