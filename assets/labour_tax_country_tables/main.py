from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TAX_WAGES_COU@DF_TW_COU")
    
    if data.num_rows > 0:
        upload_data(data, "labour_tax_country_tables")
        print(f"Uploaded {data.num_rows} rows to labour_tax_country_tables")
        
    save_state("labour_tax_country_tables", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
