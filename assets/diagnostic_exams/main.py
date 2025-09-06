from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_PROC@DF_DIAG_EXAM")
    
    if data.num_rows > 0:
        upload_data(data, "diagnostic_exams")
        print(f"Uploaded {data.num_rows} rows to diagnostic_exams")
        
    save_state("diagnostic_exams", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
