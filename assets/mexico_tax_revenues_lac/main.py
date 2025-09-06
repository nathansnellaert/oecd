from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REV_LAC@DF_REVMEX")
    
    if data.num_rows > 0:
        upload_data(data, "mexico_tax_revenues_lac")
        print(f"Uploaded {data.num_rows} rows to mexico_tax_revenues_lac")
        
    save_state("mexico_tax_revenues_lac", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
