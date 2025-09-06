from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_QDD_GOV_REG_DD@DF_GOV_REG_DD")
    
    if data.num_rows > 0:
        upload_data(data, "regulatory_governance_microdata")
        print(f"Uploaded {data.num_rows} rows to regulatory_governance_microdata")
        
    save_state("regulatory_governance_microdata", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
