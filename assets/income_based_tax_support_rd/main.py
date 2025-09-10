from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_RDTAX@DF_IPTAX")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_income_based_tax_support_rd")
        print(f"Uploaded {data.num_rows} rows to income_based_tax_support_rd")
        
    save_state("income_based_tax_support_rd", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
