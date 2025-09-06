from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TIM_2021@DF_TIM_2021")
    
    if data.num_rows > 0:
        upload_data(data, "trade_in_employment_2021")
        print(f"Uploaded {data.num_rows} rows to trade_in_employment_2021")
        
    save_state("trade_in_employment_2021", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
