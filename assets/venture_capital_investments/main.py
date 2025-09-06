from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_VC@DF_VC_INV")
    
    if data.num_rows > 0:
        upload_data(data, "venture_capital_investments")
        print(f"Uploaded {data.num_rows} rows to venture_capital_investments")
        
    save_state("venture_capital_investments", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
