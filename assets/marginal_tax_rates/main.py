from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TAXBEN_METR@DF_METR")
    
    if data.num_rows > 0:
        upload_data(data, "marginal_tax_rates")
        print(f"Uploaded {data.num_rows} rows to marginal_tax_rates")
        
    save_state("marginal_tax_rates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
