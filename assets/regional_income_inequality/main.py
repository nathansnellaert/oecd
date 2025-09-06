from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_SOC@DF_INCOME_INEQ")
    
    if data.num_rows > 0:
        upload_data(data, "regional_income_inequality")
        print(f"Uploaded {data.num_rows} rows to regional_income_inequality")
        
    save_state("regional_income_inequality", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
