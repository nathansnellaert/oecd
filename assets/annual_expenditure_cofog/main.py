from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC10@DF_TABLE11")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_annual_expenditure_cofog")
        print(f"Uploaded {data.num_rows} rows to annual_expenditure_cofog")
        
    save_state("annual_expenditure_cofog", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
