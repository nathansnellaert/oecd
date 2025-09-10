from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PRICES_COICOP2018@DF_PRICES_C2018_N_TXCP01_NRG")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_cpi_excluding_food_energy_growth_coicop_2018")
        print(f"Uploaded {data.num_rows} rows to cpi_excluding_food_energy_growth_coicop_2018")
        
    save_state("cpi_excluding_food_energy_growth_coicop_2018", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
