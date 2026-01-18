import numpy as np
import matplotlib.pyplot as plt

# Example data: elevation ranges and corresponding area percentages
elevation_ranges = ['<100', '100-200', '200-300', '300-400', '400-500', '>500']
area_percentages = [0, 0, 0, 83, 99, 100]  # Cumulative area (%)

plt.figure(figsize=(8, 6))
plt.plot(elevation_ranges, area_percentages, marker='o', color='blue', linewidth=2)
plt.xlabel('Elevation Range (m)')
plt.ylabel('Cumulative Area (%)')
plt.title('Hypsographic Curve (Elevation vs Cumulative Area)')
plt.grid(True)
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()