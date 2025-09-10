from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_SAL_STA@DF_ALL")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_statutory_salaries_full_dataset")
        print(f"Uploaded {data.num_rows} rows to statutory_salaries_full_dataset")
        
    save_state("statutory_salaries_full_dataset", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
