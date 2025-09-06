from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN1@DF_QNA_INC_SAV")
    
    if data.num_rows > 0:
        upload_data(data, "quarterly_income_saving")
        print(f"Uploaded {data.num_rows} rows to quarterly_income_saving")
        
    save_state("quarterly_income_saving", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
