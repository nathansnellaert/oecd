from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DAC2@DF_DAC3A")
    
    if data.num_rows > 0:
        upload_data(data, "dac3a_oda_commitments")
        print(f"Uploaded {data.num_rows} rows to dac3a_oda_commitments")
        
    save_state("dac3a_oda_commitments", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
