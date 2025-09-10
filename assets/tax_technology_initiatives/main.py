from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_QDD_ITTI@DF_QDD_ITTI")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_tax_technology_initiatives")
        print(f"Uploaded {data.num_rows} rows to tax_technology_initiatives")
        
    save_state("tax_technology_initiatives", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
