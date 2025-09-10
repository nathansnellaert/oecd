from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REV_AFRICA@DF_REVCIV")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_cote_divoire_tax_revenues")
        print(f"Uploaded {data.num_rows} rows to cote_divoire_tax_revenues")
        
    save_state("cote_divoire_tax_revenues", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
