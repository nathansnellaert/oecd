from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EGDNA_SOCDEM@DF_SOCIODEMOGRAPHIC_QUINTILES")
    
    if data.num_rows > 0:
        upload_data(data, "income_quintiles_by_socio_demographic")
        print(f"Uploaded {data.num_rows} rows to income_quintiles_by_socio_demographic")
        
    save_state("income_quintiles_by_socio_demographic", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
