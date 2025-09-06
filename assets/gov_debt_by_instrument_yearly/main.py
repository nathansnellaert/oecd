from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_GOV_FIN_INSTR@DF_GOV_FIN_INSTR_YU")
    
    if data.num_rows > 0:
        upload_data(data, "gov_debt_by_instrument_yearly")
        print(f"Uploaded {data.num_rows} rows to gov_debt_by_instrument_yearly")
        
    save_state("gov_debt_by_instrument_yearly", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
