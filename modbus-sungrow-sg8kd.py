read_register = {
  "5003": "daily_power_yield_0.01", # Wh # Close enough with 8KD
  "5004": "total_power_yield_100",  # MWh # 
  "5008": "internal_temp_10",       # C # Correct on 8KD
  "5011": "pv1_voltage_10",         # V 
  "5012": "pv1_current_10",         # A
  "5013": "pv2_voltage_10",         # V
  "5014": "pv2_current_10",         # A
  "5017": "total_pv_power",         # W # 
  "5019": "grid_voltage_10",        # V
  "5022": "inverter_current_10",    # A
  "5031": "total_active_power",     # W # Correct on 8KD
  "5036": "grid_frequency_10",      # Hz

 #  "5091": "power_meter",               # W - House Consumption # seems to be a constant 65,535W on 8KD
  "5097": "daily_purchased_energy_10", # kW

 # "5101": "daily_energy_consumption_0.01", # Wh
  "5103": "total_energy_consumption_10",   # kWh
}

holding_register = {
  "5000": "year",
  "5001": "month",
  "5002": "day",
  "5003": "hour",
  "5004": "minute",
  "5005": "second"
}

scan = """{
    "read": [
        {
            "start": "5000",
            "range": "100"
        },
        {
            "start": "5100",
            "range": "50"
        }
  ],
  "holding": [
    {
      "start": "4999",
      "range": "10"
    }
  ]
}"""

# Match Modbus registers to pvoutput api fields
# Reference: https://pvoutput.org/help.html#api-addstatus
pvoutput = {
  "Energy Generation": "daily_power_yield", 
  "Power Generation": "total_active_power",
  "Energy Consumption": "daily_energy_consumption",
  "Power Consumption": "power_meter",
  "Temperature": "internal_temp",
  "Voltage": "grid_voltage"
}




# # Can't recall where I pulled the 8kd config below from - but it doesn't seem to work well for me. The 5KD config above seems to largely work. 

# read_register = {
#   "5008":  "internal_temp_10",
#   "5011":  "pv1_voltage_10",
#   "5012":  "pv1_current_10",
#   "5013":  "pv2_voltage_10",
#   "5014":  "pv2_current_10",
#   "5017":  "total_pv_power",  # PVOutput, v2 - Power Generation
#   "5019":  "grid_voltage_10", # PVOutput, v6 - Grid voltage
#   "5022":  "inverter_current_10",
#   "5036":  "grid_frequency_10",
#   "5091":  "power_meter",      # in Watts, PVOutput, v4 - Power Consumption
#   "5092":  "power_meter_hi",   # in Watts, hi word
#   "5097":  "5097",          # 0.1 kW, iSolarCloud, "Daily Purchased Energy"
#   "13001": "running_state",
#   "13002": "daily_pv_energy_10",
#   "13003": "total_pv_energy_10",
#   "13005": "daily_export_energy_10",
#   "13006": "total_export_energy_10",
#   "13008": "load_power",
#   "13010": "export_power",
#   "13011": "grid_import_or_export",
#   "13012": "daily_charge_energy_10",
#   "13013": "total_charge_energy_10",
#   "13015": "co2_emission_reduction",
#   "13017": "daily_use_energy_10",
#   "13018": "total_use_energy_10",
#   "13020": "battery_voltage_10",
#   "13021": "battery current_10",
#   "13022": "battery_power",
#   "13023": "battery_level_10",
#   "13024": "battery_health_10",
#   "13025": "battery_temp_10",
#   "13026": "daily_discharge_energy_10",
#   "13027": "total_discharge_energy_10",
#   "13029": "use_power",
#   "13031": "inverter_current_10",
#   "13034": "pv_power"
# }

# holding_register = {
#   "5000": "year",
#   "5001": "month",
#   "5002": "day",
#   "5003": "hour",
#   "5004": "minute",
#   "5005": "second"
# }

# scan = """{
#   "read": [
#      {
#        "start": "5000",
#        "range": "100"
#      },
#      {
#        "start": "13000",
#        "range": "100"
#      }
#   ],
#   "holding": [
#      {
#        "start": "4999",
#        "range": "100"
#      }
#   ]
# }"""


# # Match Modbus registers to pvoutput api fields
# # Reference: https://pvoutput.org/help.html#api-addstatus
# pvoutput = {
#   "Energy Generation": "daily_power_yield",
#   "Power Generation": "total_active_power",
#   "Energy Consumption": "daily_energy_consumption",
#   "Power Consumption": "power_meter",
#   "Temperature": "internal_temp",
#   "Voltage": "grid_voltage"
# }
