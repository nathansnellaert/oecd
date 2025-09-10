from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_WHT@DF_WHT_TREATY")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_withholding_tax_rates_treaty")
        print(f"Uploaded {data.num_rows} rows to withholding_tax_rates_treaty")
        
    save_state("withholding_tax_rates_treaty", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
