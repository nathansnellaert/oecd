from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_QDD_GOV_REG@DF_GOV_REG")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_regulatory_governance")
        print(f"Uploaded {data.num_rows} rows to regulatory_governance")
        
    save_state("regulatory_governance", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
