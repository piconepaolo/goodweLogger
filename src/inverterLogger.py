import re
import string
from unittest import result
import config
import asyncio
import sys
import goodwe

result=[]

async def get_runtime_data():
    result.clear()
    ip_address = config.inverter['ip_address']
    
    sensors = [
        "ppv",               # PV power (W)
        "pbattery1",         # battery power (W) + = charging, - = discharging
        "battery_mode",      # 1=standby, 2=discharge, 3=charge
        "battery_soc",       # battery state of charge (%)
        "active_power",      # grid power (W): - = buy, + = sell
        "grid_in_out",       # 1=sell or export, 2=buy or import
        "house_consumption", # own consumption (W)
        "e_day",             # today's PV energy production (kWh)
        "e_total",           # total PV energy production (kWh)
        "meter_e_total_exp", # total sold (exported) energy (kWh)
        "meter_e_total_imp"  # total bought or imported energy (kWh)
    ]
    
    inverter = await goodwe.connect(ip_address)
    runtime_data = await inverter.read_runtime_data()
    for sensor in inverter.sensors():
        if sensor.id_ in runtime_data: #dopo questo posso filtrare i sensori che non voglio dalla lista sopra ##sensor.id_ in sensors##
            if sensor.id_ in sensors:
                print(f"{sensor.id_}: \t\t {sensor.name}={runtime_data[sensor.id_]} {sensor.unit}")
                result.append(f"{sensor.name}={runtime_data[sensor.id_]} {sensor.unit}")
                
def run():
    asyncio.run(get_runtime_data()) 
    return result # TODO parsarlo per bene 

def main():
    asyncio.run(get_runtime_data())    

if __name__ == "__main__":
    sys.exit(main())