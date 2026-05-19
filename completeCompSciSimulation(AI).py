"""
Mars Colony Algae Growth Simulation - Interactive GUI
Computer Science Component - IDP 2026

Interactive simulation with real-time chart updates based on user inputs.
"""

import tkinter as tk
from tkinter import ttk
import random
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class AlgaeSimulationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Mars Colony Algae Growth Simulation")
        self.root.geometry("1400x900")
        
        # Data storage
        self.simulation_data = []
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        # Main container
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Left panel - Controls
        control_frame = tk.LabelFrame(main_frame, text="Simulation Parameters", 
                                     padx=15, pady=15, font=("Arial", 11, "bold"))
        control_frame.pack(side="left", fill="y", padx=(0, 10))
        
        # Title
        title = tk.Label(control_frame, text="Mars Algae Growth\nSimulation", 
                        font=("Arial", 14, "bold"), fg="#2E7D32")
        title.grid(row=0, column=0, columnspan=3, pady=(0, 15))
        
        row = 1
        
        # Soil Type
        tk.Label(control_frame, text="Soil Type:", font=("Arial", 10)).grid(
            row=row, column=0, sticky="w", pady=8)
        self.soil_var = tk.StringVar(value="Iron-rich")
        soil_dropdown = ttk.Combobox(control_frame, textvariable=self.soil_var, 
                                     values=["Iron-rich", "Sulfate-based", "Clay-based"], 
                                     state="readonly", width=18)
        soil_dropdown.grid(row=row, column=1, columnspan=2, pady=8)
        row += 1
        
        # Enzyme Type
        tk.Label(control_frame, text="Enzyme Type:", font=("Arial", 10)).grid(
            row=row, column=0, sticky="w", pady=8)
        self.enzyme_var = tk.StringVar(value="Control (None)")
        enzyme_dropdown = ttk.Combobox(control_frame, textvariable=self.enzyme_var,
                                      values=["Control (None)", "Enzyme A", "Enzyme B", "Enzyme C"],
                                      state="readonly", width=18)
        enzyme_dropdown.grid(row=row, column=1, columnspan=2, pady=8)
        row += 1
        
        # Simulation Days
        tk.Label(control_frame, text="Simulation Days:", font=("Arial", 10)).grid(
            row=row, column=0, sticky="w", pady=8)
        self.days_var = tk.IntVar(value=50)
        days_spinbox = tk.Spinbox(control_frame, from_=20, to=100, 
                                 textvariable=self.days_var, width=18)
        days_spinbox.grid(row=row, column=1, columnspan=2, pady=8)
        row += 1
        
        # Separator
        tk.Frame(control_frame, height=2, bg="gray").grid(
            row=row, column=0, columnspan=3, sticky="ew", pady=15)
        row += 1
        
        tk.Label(control_frame, text="Environmental Ranges", 
                font=("Arial", 10, "bold")).grid(row=row, column=0, columnspan=3, pady=(0, 10))
        row += 1
        
        # Temperature Range
        tk.Label(control_frame, text="Temperature (°C):", font=("Arial", 10)).grid(
            row=row, column=0, sticky="w", pady=8)
        tk.Label(control_frame, text="Min:", font=("Arial", 9)).grid(
            row=row, column=1, sticky="e", padx=(0, 5))
        self.temp_min_var = tk.IntVar(value=18)
        temp_min_spin = tk.Spinbox(control_frame, from_=10, to=25, 
                                   textvariable=self.temp_min_var, width=5)
        temp_min_spin.grid(row=row, column=2, sticky="w")
        row += 1
        
        tk.Label(control_frame, text="", font=("Arial", 10)).grid(
            row=row, column=0, sticky="w")
        tk.Label(control_frame, text="Max:", font=("Arial", 9)).grid(
            row=row, column=1, sticky="e", padx=(0, 5))
        self.temp_max_var = tk.IntVar(value=24)
        temp_max_spin = tk.Spinbox(control_frame, from_=10, to=30, 
                                   textvariable=self.temp_max_var, width=5)
        temp_max_spin.grid(row=row, column=2, sticky="w")
        row += 1
        
        # Light Exposure Range
        tk.Label(control_frame, text="Light Exposure (hrs):", font=("Arial", 10)).grid(
            row=row, column=0, sticky="w", pady=8)
        tk.Label(control_frame, text="Min:", font=("Arial", 9)).grid(
            row=row, column=1, sticky="e", padx=(0, 5))
        self.light_min_var = tk.IntVar(value=7)
        light_min_spin = tk.Spinbox(control_frame, from_=6, to=10, 
                                    textvariable=self.light_min_var, width=5)
        light_min_spin.grid(row=row, column=2, sticky="w")
        row += 1
        
        tk.Label(control_frame, text="", font=("Arial", 10)).grid(
            row=row, column=0, sticky="w")
        tk.Label(control_frame, text="Max:", font=("Arial", 9)).grid(
            row=row, column=1, sticky="e", padx=(0, 5))
        self.light_max_var = tk.IntVar(value=11)
        light_max_spin = tk.Spinbox(control_frame, from_=6, to=12, 
                                    textvariable=self.light_max_var, width=5)
        light_max_spin.grid(row=row, column=2, sticky="w")
        row += 1
        
        # CO2 Level Range
        tk.Label(control_frame, text="CO₂ Level:", font=("Arial", 10)).grid(
            row=row, column=0, sticky="w", pady=8)
        tk.Label(control_frame, text="Min:", font=("Arial", 9)).grid(
            row=row, column=1, sticky="e", padx=(0, 5))
        self.co2_min_var = tk.DoubleVar(value=0.04)
        co2_min_spin = tk.Spinbox(control_frame, from_=0.03, to=0.06, increment=0.01,
                                  textvariable=self.co2_min_var, width=5, format="%.2f")
        co2_min_spin.grid(row=row, column=2, sticky="w")
        row += 1
        
        tk.Label(control_frame, text="", font=("Arial", 10)).grid(
            row=row, column=0, sticky="w")
        tk.Label(control_frame, text="Max:", font=("Arial", 9)).grid(
            row=row, column=1, sticky="e", padx=(0, 5))
        self.co2_max_var = tk.DoubleVar(value=0.07)
        co2_max_spin = tk.Spinbox(control_frame, from_=0.03, to=0.08, increment=0.01,
                                  textvariable=self.co2_max_var, width=5, format="%.2f")
        co2_max_spin.grid(row=row, column=2, sticky="w")
        row += 1
        
        # Separator
        tk.Frame(control_frame, height=2, bg="gray").grid(
            row=row, column=0, columnspan=3, sticky="ew", pady=15)
        row += 1
        
        # Run Button
        run_button = tk.Button(control_frame, text="▶ Run Simulation", 
                              command=self.run_simulation,
                              bg="#2E7D32", fg="white", font=("Arial", 12, "bold"),
                              padx=30, pady=10, cursor="hand2")
        run_button.grid(row=row, column=0, columnspan=3, pady=10)
        row += 1
        
        # Status Label
        self.status_label = tk.Label(control_frame, text="Ready to run simulation", 
                                    font=("Arial", 9), fg="gray", wraplength=250)
        self.status_label.grid(row=row, column=0, columnspan=3, pady=(10, 0))
        
        # Right panel - Charts
        chart_frame = tk.Frame(main_frame)
        chart_frame.pack(side="right", fill="both", expand=True)
        
        # Create matplotlib figure
        self.fig = Figure(figsize=(12, 8), dpi=100)
        
        # Create two subplots
        self.ax1 = self.fig.add_subplot(2, 1, 1)
        self.ax2 = self.fig.add_subplot(2, 1, 2)
        
        # Embed in tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=chart_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        
        # Initial empty charts
        self.show_placeholder_charts()
        
    def show_placeholder_charts(self):
        """Show placeholder text before first simulation"""
        self.ax1.clear()
        self.ax2.clear()
        
        self.ax1.text(0.5, 0.5, 'Click "Run Simulation" to generate charts', 
                     ha='center', va='center', fontsize=14, color='gray',
                     transform=self.ax1.transAxes)
        self.ax1.set_title("Growth Rate Timeline", fontsize=12, fontweight='bold')
        
        self.ax2.text(0.5, 0.5, 'Click "Run Simulation" to generate charts', 
                     ha='center', va='center', fontsize=14, color='gray',
                     transform=self.ax2.transAxes)
        self.ax2.set_title("Enzyme Effectiveness Comparison", fontsize=12, fontweight='bold')
        
        self.canvas.draw()
    
    def run_simulation(self):
        """Run the algae growth simulation with current parameters"""
        
        # Update status
        self.status_label.config(text="Running simulation...", fg="orange")
        self.root.update()
        
        # Get parameters
        soil_type = self.soil_var.get()
        enzyme_type = self.enzyme_var.get()
        num_days = self.days_var.get()
        temp_min = self.temp_min_var.get()
        temp_max = self.temp_max_var.get()
        light_min = self.light_min_var.get()
        light_max = self.light_max_var.get()
        co2_min = self.co2_min_var.get()
        co2_max = self.co2_max_var.get()
        
        # Validate ranges
        if temp_min >= temp_max:
            self.status_label.config(text="Error: Temperature min >= max", fg="red")
            return
        if light_min >= light_max:
            self.status_label.config(text="Error: Light min >= max", fg="red")
            return
        if co2_min >= co2_max:
            self.status_label.config(text="Error: CO₂ min >= max", fg="red")
            return
        
        # Generate data
        self.simulation_data = self.generate_data(
            num_days, soil_type, enzyme_type,
            temp_min, temp_max, light_min, light_max, co2_min, co2_max
        )
        
        # Update charts
        self.update_charts()
        
        # Update status
        self.status_label.config(
            text=f"Simulation complete: {num_days} days, {len(self.simulation_data)} data points", 
            fg="green"
        )
    
    def generate_data(self, num_days, soil_type, enzyme_type, 
                     temp_min, temp_max, light_min, light_max, co2_min, co2_max):
        """Generate synthetic algae growth data"""
        
        data = []
        
        # Soil coefficients
        soil_coefficients = {
            "Iron-rich": 1.25,
            "Sulfate-based": 1.0,
            "Clay-based": 0.75
        }
        
        # Enzyme coefficients
        enzyme_coefficients = {
            "Control (None)": 1.0,
            "Enzyme A": 1.15,
            "Enzyme B": 1.30,
            "Enzyme C": 1.50
        }
        
        soil_factor = soil_coefficients[soil_type]
        enzyme_factor = enzyme_coefficients[enzyme_type]
        
        for day in range(1, num_days + 1):
            # Random environmental parameters within specified ranges
            light_hours = random.uniform(light_min, light_max)
            temperature = random.uniform(temp_min, temp_max)
            co2_level = random.uniform(co2_min, co2_max)
            
            # Calculate growth factors
            
            # Light factor (normalized 0-1)
            light_factor = (light_hours - 6) / 6
            
            # Temperature factor (quadratic - optimal at 21°C)
            optimal_temp = 21
            temp_deviation = abs(temperature - optimal_temp)
            temp_factor = max(0.3, 1 - (temp_deviation ** 2) / 80)
            
            # CO2 factor (logarithmic saturation)
            co2_factor = math.log(1 + co2_level * 60) / math.log(1 + 0.08 * 60)
            
            # Time factor (establishment curve)
            time_factor = 1 + (0.025 * day) - (0.00025 * day ** 2)
            time_factor = max(0.6, min(1.4, time_factor))
            
            # Calculate growth rate
            base_growth = 4.2
            growth_rate = (base_growth * 
                          light_factor * 
                          temp_factor * 
                          co2_factor * 
                          soil_factor * 
                          enzyme_factor * 
                          time_factor)
            
            # Add noise
            growth_rate *= random.uniform(0.92, 1.08)
            growth_rate = max(0.5, growth_rate)
            
            # Calculate oxygen output
            o2_ratio = random.uniform(1.65, 1.95)
            oxygen_output = growth_rate * o2_ratio
            
            data.append({
                'day': day,
                'soil_type': soil_type,
                'enzyme_type': enzyme_type,
                'light_hours': round(light_hours, 2),
                'temperature_c': round(temperature, 2),
                'co2_level': round(co2_level, 3),
                'growth_rate': round(growth_rate, 3),
                'oxygen_output': round(oxygen_output, 3)
            })
        
        return data
    
    def update_charts(self):
        """Update both charts with current simulation data"""
        
        # Clear previous plots
        self.ax1.clear()
        self.ax2.clear()
        
        # Extract data
        days = [r['day'] for r in self.simulation_data]
        growth_rates = [r['growth_rate'] for r in self.simulation_data]
        oxygen_outputs = [r['oxygen_output'] for r in self.simulation_data]
        
        # Chart 1: Growth Rate Timeline
        self.ax1.plot(days, growth_rates, linewidth=2, color='#2E7D32', 
                     alpha=0.7, label='Daily Growth Rate')
        
        # Calculate moving average
        window = min(10, len(growth_rates) // 5)
        if window > 1:
            moving_avg = []
            for i in range(len(growth_rates)):
                if i < window:
                    moving_avg.append(sum(growth_rates[:i+1]) / (i+1))
                else:
                    moving_avg.append(sum(growth_rates[i-window:i]) / window)
            
            self.ax1.plot(days, moving_avg, linewidth=3, color='darkblue', 
                         alpha=0.6, linestyle='--', label=f'{window}-Day Moving Average')
        
        self.ax1.set_xlabel('Day', fontsize=10, fontweight='bold')
        self.ax1.set_ylabel('Growth Rate (g/day)', fontsize=10, fontweight='bold')
        self.ax1.set_title(f'Algae Growth Over Time - {self.enzyme_var.get()} on {self.soil_var.get()} Soil', 
                          fontsize=11, fontweight='bold')
        self.ax1.grid(True, alpha=0.3, linestyle='--')
        self.ax1.legend(loc='best')
        
        # Annotate peak
        max_growth = max(growth_rates)
        max_day = days[growth_rates.index(max_growth)]
        self.ax1.annotate(f'Peak: {max_growth:.2f} g/day', 
                         xy=(max_day, max_growth), 
                         xytext=(max_day + len(days)*0.1, max_growth + 0.5),
                         arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
                         fontsize=9, fontweight='bold',
                         bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))
        
        # Chart 2: Summary Statistics (Bar chart)
        avg_growth = sum(growth_rates) / len(growth_rates)
        avg_oxygen = sum(oxygen_outputs) / len(oxygen_outputs)
        max_growth_val = max(growth_rates)
        max_oxygen_val = max(oxygen_outputs)
        
        metrics = ['Avg Growth\n(g/day)', 'Peak Growth\n(g/day)', 
                   'Avg O₂\n(mL/hr)', 'Peak O₂\n(mL/hr)']
        values = [avg_growth, max_growth_val, avg_oxygen, max_oxygen_val]
        colors_bar = ['#388E3C', '#2E7D32', '#1976D2', '#0D47A1']
        
        bars = self.ax2.bar(metrics, values, color=colors_bar, alpha=0.8, 
                           edgecolor='black', linewidth=1.5)
        
        # Add value labels
        for bar, val in zip(bars, values):
            height = bar.get_height()
            self.ax2.text(bar.get_x() + bar.get_width()/2., height,
                         f'{val:.2f}',
                         ha='center', va='bottom', fontweight='bold', fontsize=10)
        
        self.ax2.set_ylabel('Value', fontsize=10, fontweight='bold')
        self.ax2.set_title('Performance Metrics Summary', fontsize=11, fontweight='bold')
        self.ax2.grid(True, axis='y', alpha=0.3, linestyle='--')
        
        # Tight layout and draw
        self.fig.tight_layout()
        self.canvas.draw()

def main():
    root = tk.Tk()
    app = AlgaeSimulationGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
