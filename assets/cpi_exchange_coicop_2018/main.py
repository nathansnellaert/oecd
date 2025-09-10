from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PRICES_EXC_C18@DF_PRICES_EXCHANGE_COICOP18")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_cpi_exchange_coicop_2018")
        print(f"Uploaded {data.num_rows} rows to cpi_exchange_coicop_2018")
        
    save_state("cpi_exchange_coicop_2018", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
