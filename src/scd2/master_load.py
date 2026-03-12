# MASTER_LOAD.py
import subprocess

load_order = [
    "country_load.py",
    "region_load.py",
    "state_load.py",
    "city_load.py",
    "category_load.py",
    "subcategory_load.py",
    "product_load.py",
    "segment_load.py",
    "customer_load.py",
    
    "ship_mode_load.py",
    "fact_sales_load.py",   # always last
]

for script in load_order:
    print(f"Running {script}...")
    subprocess.run(["python", script], check=True)
    print(f"{script} completed.")
