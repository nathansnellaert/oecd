from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_QDD_GOV_SP_REV@DF_GOV_SP_REV")
    
    if data.num_rows > 0:
        upload_data(data, "spending_review")
        print(f"Uploaded {data.num_rows} rows to spending_review")
        
    save_state("spending_review", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
