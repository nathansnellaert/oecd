from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HCQO@DF_PS")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_patient_safety")
        print(f"Uploaded {data.num_rows} rows to patient_safety")
        
    save_state("patient_safety", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
