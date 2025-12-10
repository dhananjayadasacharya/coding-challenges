# Acres per crop (80 acres divided equally into 5)
acres = 16

# --- Tomato calculations ---
tomato_30 = acres * 0.30 * 10          # 30% land → 10 t/acre
tomato_70 = acres * 0.70 * 12          # 70% land → 12 t/acre
tomato_yield = tomato_30 + tomato_70   # total tonnes
tomato_sales = tomato_yield * 7000     # Rs. 7 per kg = 7000 per tonne

# --- Potato calculations ---
potato_yield = acres * 10              # 10 t/acre
potato_sales = potato_yield * 20000    # Rs. 20 per kg = 20000 per tonne

# --- Cabbage calculations ---
cabbage_yield = acres * 14             # 14 t/acre
cabbage_sales = cabbage_yield * 24000  # Rs. 24 per kg = 24000 per tonne

# --- Sunflower calculations ---
sunflower_yield = acres * 0.7          # 0.7 t/acre
sunflower_sales = sunflower_yield * 200000  # Rs. 200 per kg = 200000 per tonne

# --- Sugarcane calculations ---
sugarcane_yield = acres * 45           # 45 t/acre
sugarcane_sales = sugarcane_yield * 4000    # Rs. 4000 per tonne

# --- Overall sales (80 acres) ---
overall_sales = (tomato_sales + potato_sales +
                 cabbage_sales + sunflower_sales + sugarcane_sales)

# --- Chemical-free sales after 11 months ---
# Sugarcane is NOT chemical-free yet
chemical_free_sales = (tomato_sales + potato_sales +
                       cabbage_sales + sunflower_sales)

print("Overall Sales from 80 acres       :", overall_sales)
print("Sales from Chemical-Free Farming in 11 months :", chemical_free_sales)
