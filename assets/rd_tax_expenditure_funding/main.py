from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_RDTAX@DF_RDTAX")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_rd_tax_expenditure_funding")
        print(f"Uploaded {data.num_rows} rows to rd_tax_expenditure_funding")
        
    save_state("rd_tax_expenditure_funding", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
