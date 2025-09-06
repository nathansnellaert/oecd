from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AFDD_STAT_ANNEX@DF_TAB15")
    
    if data.num_rows > 0:
        upload_data(data, "afdd_growth_decomposition_expenditure")
        print(f"Uploaded {data.num_rows} rows to afdd_growth_decomposition_expenditure")
        
    save_state("afdd_growth_decomposition_expenditure", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
