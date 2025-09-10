from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_MOB@DF_MOBILISATION")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_private_finance_mobilisation")
        print(f"Uploaded {data.num_rows} rows to private_finance_mobilisation")
        
    save_state("private_finance_mobilisation", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
