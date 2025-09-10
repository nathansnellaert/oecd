from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_RDS_BERD@DF_BERD_INDU")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_business_rd_expenditure_by_industry")
        print(f"Uploaded {data.num_rows} rows to business_rd_expenditure_by_industry")
        
    save_state("business_rd_expenditure_by_industry", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
