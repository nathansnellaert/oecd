from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_QDD_CFC@DF_QDD_CFC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_controlled_foreign_company_rules")
        print(f"Uploaded {data.num_rows} rows to controlled_foreign_company_rules")
        
    save_state("controlled_foreign_company_rules", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
