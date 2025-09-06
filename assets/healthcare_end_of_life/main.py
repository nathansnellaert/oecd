from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HCQO@DF_EOLC")
    
    if data.num_rows > 0:
        upload_data(data, "healthcare_end_of_life")
        print(f"Uploaded {data.num_rows} rows to healthcare_end_of_life")
        
    save_state("healthcare_end_of_life", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
