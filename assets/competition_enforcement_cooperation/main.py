from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_CEC_QDD@DF_QDD_CEC")
    
    if data.num_rows > 0:
        upload_data(data, "competition_enforcement_cooperation")
        print(f"Uploaded {data.num_rows} rows to competition_enforcement_cooperation")
        
    save_state("competition_enforcement_cooperation", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
