from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN10@DF_TABLE2_B6_VPVOP")
    
    if data.num_rows > 0:
        upload_data(data, "annual_disposable_income_ppp")
        print(f"Uploaded {data.num_rows} rows to annual_disposable_income_ppp")
        
    save_state("annual_disposable_income_ppp", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
