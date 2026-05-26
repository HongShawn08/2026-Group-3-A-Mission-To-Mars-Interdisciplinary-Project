import tkinter as tk
from tkinter import ttk
import random

print("Script started...")
print("Imports successful")

class AlgaeSimulation:
    def __init__(self, root):
        print("Initializing AlgaeSimulation...")
        self.root = root
        self.root.title("Mars Algae Growth Simulation")
        self.root.geometry("800x600")
        
        # Data storage
        self.simulation_data = []
        self.day_count = 0
        
        # Create UI
        self.create_widgets()
        print("UI created successfully")
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Mars Colony Algae Growth Simulation", 
                              font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Input Frame
        input_frame = tk.LabelFrame(self.root, text="Simulation Parameters", padx=10, pady=10)
        input_frame.pack(padx=20, pady=10, fill="x")
        
        # Soil Type
        tk.Label(input_frame, text="Soil Type:").grid(row=0, column=0, sticky="w", pady=5)
        self.soil_var = tk.StringVar(value="Iron-rich")
        soil_dropdown = ttk.Combobox(input_frame, textvariable=self.soil_var, 
                                     values=["Iron-rich", "Sulfate-based", "Clay-based"], 
                                     state="readonly", width=20)
        soil_dropdown.grid(row=0, column=1, pady=5)
        
        # Enzyme Type
        tk.Label(input_frame, text="Enzyme Type:").grid(row=1, column=0, sticky="w", pady=5)
        self.enzyme_var = tk.StringVar(value="Chromate Reductase")
        enzyme_dropdown = ttk.Combobox(input_frame, textvariable=self.enzyme_var,
                          values=["Chromate Reductase", "Class II Chromate Reductase", "Urease"],
                                      state="readonly", width=20)
        enzyme_dropdown.grid(row=1, column=1, pady=5)
        
        # Temperature Slider
        tk.Label(input_frame, text="Temperature (°C):").grid(row=2, column=0, sticky="w", pady=5)
        self.temp_var = tk.IntVar(value=20)
        temp_slider = tk.Scale(input_frame, from_=10, to=30, orient="horizontal",
                              variable=self.temp_var, length=200)
        temp_slider.grid(row=2, column=1, pady=5)
        self.temp_label = tk.Label(input_frame, text="20°C")
        self.temp_label.grid(row=2, column=2, pady=5)
        temp_slider.config(command=self.update_temp_label)
        
        # CO2 Level Slider
        tk.Label(input_frame, text="CO₂ Level:").grid(row=3, column=0, sticky="w", pady=5)
        self.co2_var = tk.DoubleVar(value=0.05)
        co2_slider = tk.Scale(input_frame, from_=0.03, to=0.08, resolution=0.01,
                             orient="horizontal", variable=self.co2_var, length=200)
        co2_slider.grid(row=3, column=1, pady=5)
        self.co2_label = tk.Label(input_frame, text="0.05")
        self.co2_label.grid(row=3, column=2, pady=5)
        co2_slider.config(command=self.update_co2_label)
        
        # Light Exposure Slider
        tk.Label(input_frame, text="Light Exposure (hrs):").grid(row=4, column=0, sticky="w", pady=5)
        self.light_var = tk.IntVar(value=9)
        light_slider = tk.Scale(input_frame, from_=6, to=12, orient="horizontal",
                               variable=self.light_var, length=200)
        light_slider.grid(row=4, column=1, pady=5)
        self.light_label = tk.Label(input_frame, text="9 hrs")
        self.light_label.grid(row=4, column=2, pady=5)
        light_slider.config(command=self.update_light_label)
        
        # Simulation Days
        tk.Label(input_frame, text="Simulation Days:").grid(row=5, column=0, sticky="w", pady=5)
        self.days_var = tk.IntVar(value=30)
        days_entry = tk.Entry(input_frame, textvariable=self.days_var, width=22)
        days_entry.grid(row=5, column=1, pady=5)
        
        # Control Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        run_button = tk.Button(button_frame, text="Run Simulation", command=self.run_simulation,
                              bg="green", fg="white", padx=20, pady=5)
        run_button.grid(row=0, column=0, padx=5)
        
        reset_button = tk.Button(button_frame, text="Reset", command=self.reset_simulation,
                                bg="orange", fg="white", padx=20, pady=5)
        reset_button.grid(row=0, column=1, padx=5)
        
        export_button = tk.Button(button_frame, text="Export Data", command=self.export_data,
                                 bg="blue", fg="white", padx=20, pady=5)
        export_button.grid(row=0, column=2, padx=5)
        
        # Results Frame
        results_frame = tk.LabelFrame(self.root, text="Simulation Results", padx=10, pady=10)
        results_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Results Text Box with Scrollbar
        scrollbar = tk.Scrollbar(results_frame)
        scrollbar.pack(side="right", fill="y")
        
        self.results_text = tk.Text(results_frame, height=10, width=80, 
                                   yscrollcommand=scrollbar.set)
        self.results_text.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.results_text.yview)
        
        # Status Bar
        self.status_label = tk.Label(self.root, text="Ready to run simulation", 
                                    bd=1, relief="sunken", anchor="w")
        self.status_label.pack(side="bottom", fill="x")
    
    def update_temp_label(self, value):
        self.temp_label.config(text=f"{int(float(value))}°C")
    
    def update_co2_label(self, value):
        self.co2_label.config(text=f"{float(value):.2f}")
    
    def update_light_label(self, value):
        self.light_label.config(text=f"{int(float(value))} hrs")
    
    def run_simulation(self):
        # Clear previous results
        self.results_text.delete(1.0, tk.END)
        self.simulation_data = []
        
        # Get input values
        soil_type = self.soil_var.get()
        enzyme_type = self.enzyme_var.get()
        temperature = self.temp_var.get()
        co2_level = self.co2_var.get()
        light_hours = self.light_var.get()
        num_days = self.days_var.get()
        
        self.status_label.config(text="Running simulation...")
        self.root.update()
        
        # Display header
        self.results_text.insert(tk.END, f"=== Simulation Parameters ===\n")
        self.results_text.insert(tk.END, f"Soil: {soil_type}\n")
        self.results_text.insert(tk.END, f"Enzyme: {enzyme_type}\n")
        self.results_text.insert(tk.END, f"Temperature: {temperature}°C\n")
        self.results_text.insert(tk.END, f"CO₂: {co2_level}\n")
        self.results_text.insert(tk.END, f"Light: {light_hours} hrs/day\n")
        self.results_text.insert(tk.END, f"\n=== Daily Results ===\n")
        self.results_text.insert(tk.END, f"{'Day':<6}{'Growth (g/day)':<18}{'O₂ Output (mL/hr)':<20}\n")
        self.results_text.insert(tk.END, "-" * 50 + "\n")
        
        # Run simulation for each day
        for day in range(1, num_days + 1):
            # TODO: Replace this with actual growth calculation based on your model
            # This is placeholder logic
            base_growth = random.uniform(2.0, 5.0)
            base_oxygen = random.uniform(10.0, 25.0)
            
            # Store data
            self.simulation_data.append({
                'day': day,
                'soil': soil_type,
                'enzyme': enzyme_type,
                'temperature': temperature,
                'co2': co2_level,
                'light': light_hours,
                'growth_rate': base_growth,
                'oxygen_output': base_oxygen
            })
            
            # Display results
            self.results_text.insert(tk.END, 
                f"{day:<6}{base_growth:<18.2f}{base_oxygen:<20.2f}\n")
        
        # Summary statistics
        avg_growth = sum(d['growth_rate'] for d in self.simulation_data) / len(self.simulation_data)
        avg_oxygen = sum(d['oxygen_output'] for d in self.simulation_data) / len(self.simulation_data)
        
        self.results_text.insert(tk.END, "\n=== Summary ===\n")
        self.results_text.insert(tk.END, f"Average Growth Rate: {avg_growth:.2f} g/day\n")
        self.results_text.insert(tk.END, f"Average O₂ Output: {avg_oxygen:.2f} mL/hr\n")
        
        self.status_label.config(text=f"Simulation complete - {num_days} days processed")
    
    def reset_simulation(self):
        self.results_text.delete(1.0, tk.END)
        self.simulation_data = []
        self.soil_var.set("Iron-rich")
        self.enzyme_var.set("Chromate Reductase")
        self.temp_var.set(20)
        self.co2_var.set(0.05)
        self.light_var.set(9)
        self.days_var.set(30)
        self.status_label.config(text="Simulation reset")
    
    def export_data(self):
        if not self.simulation_data:
            self.status_label.config(text="No data to export - run simulation first")
            return
        
        # TODO: Implement CSV export
        # For now, just show message
        self.status_label.config(text="Export feature - to be implemented")
        print("Data ready to export:", len(self.simulation_data), "records")

def main():
    print("Creating main window...")
    root = tk.Tk()
    print("Window created, initializing app...")
    app = AlgaeSimulation(root)
    print("Starting mainloop...")
    root.mainloop()
    print("Window closed")

if __name__ == "__main__":
    print("Running main()...")
    main()