"""
Mars Colony Algae Growth Simulation - Command Line Version
Computer Science Component - IDP 2026

This CLI version simulates algae growth on Mars without requiring a GUI.
"""

import random
import math
from datetime import datetime

class AlgaeSimulationCLI:
    def __init__(self):
        self.simulation_data = []
        
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
            
            # Add small noise (±3% for realistic variation)
            noise = growth_rate * random.uniform(-0.03, 0.03)
            growth_rate = max(0.1, growth_rate + noise)
            
            # Oxygen output (proportional to growth)
            oxygen_output = growth_rate * random.uniform(4.5, 5.5)
            
            data.append({
                'day': day,
                'temperature': temperature,
                'light_hours': light_hours,
                'co2_level': co2_level,
                'growth_rate': growth_rate,
                'oxygen_output': oxygen_output
            })
        
        return data
    
    def run_simulation(self, soil_type="Iron-rich", enzyme_type="Enzyme A", 
                      num_days=30, temp_min=18, temp_max=24, 
                      light_min=7, light_max=11, co2_min=0.04, co2_max=0.07):
        """Run simulation and display results"""
        
        print("\n" + "="*80)
        print("MARS COLONY ALGAE GROWTH SIMULATION")
        print("="*80)
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        print("SIMULATION PARAMETERS:")
        print("-" * 80)
        print(f"  Soil Type:          {soil_type}")
        print(f"  Enzyme Type:        {enzyme_type}")
        print(f"  Simulation Days:    {num_days}")
        print(f"  Temperature Range:  {temp_min}°C - {temp_max}°C")
        print(f"  Light Exposure:     {light_min} - {light_max} hours/day")
        print(f"  CO₂ Level Range:    {co2_min} - {co2_max}")
        print()
        
        # Generate simulation data
        self.simulation_data = self.generate_data(
            num_days, soil_type, enzyme_type,
            temp_min, temp_max, light_min, light_max, co2_min, co2_max
        )
        
        # Display detailed results
        print("DAILY RESULTS:")
        print("-" * 80)
        print(f"{'Day':<6} {'Temp(°C)':<12} {'Light(hrs)':<12} {'CO₂':<8} {'Growth(g/d)':<14} {'O₂(mL/h)':<12}")
        print("-" * 80)
        
        for data_point in self.simulation_data:
            print(f"{data_point['day']:<6} "
                  f"{data_point['temperature']:<12.1f} "
                  f"{data_point['light_hours']:<12.1f} "
                  f"{data_point['co2_level']:<8.3f} "
                  f"{data_point['growth_rate']:<14.2f} "
                  f"{data_point['oxygen_output']:<12.2f}")
        
        # Calculate and display statistics
        growth_rates = [d['growth_rate'] for d in self.simulation_data]
        oxygen_outputs = [d['oxygen_output'] for d in self.simulation_data]
        
        avg_growth = sum(growth_rates) / len(growth_rates)
        max_growth = max(growth_rates)
        min_growth = min(growth_rates)
        
        avg_oxygen = sum(oxygen_outputs) / len(oxygen_outputs)
        max_oxygen = max(oxygen_outputs)
        min_oxygen = min(oxygen_outputs)
        
        total_biomass = sum(growth_rates)
        total_oxygen = sum(oxygen_outputs)
        
        print()
        print("STATISTICAL SUMMARY:")
        print("-" * 80)
        print(f"Growth Rate (g/day):")
        print(f"  Average:  {avg_growth:.2f}")
        print(f"  Maximum:  {max_growth:.2f}")
        print(f"  Minimum:  {min_growth:.2f}")
        print(f"  Total:    {total_biomass:.2f} g")
        print()
        print(f"Oxygen Output (mL/hour):")
        print(f"  Average:  {avg_oxygen:.2f}")
        print(f"  Maximum:  {max_oxygen:.2f}")
        print(f"  Minimum:  {min_oxygen:.2f}")
        print(f"  Total:    {total_oxygen:.2f} mL")
        print()
        
        # Recommendations
        print("COLONY RECOMMENDATIONS:")
        print("-" * 80)
        if avg_growth > 4.5:
            print("  ✓ EXCELLENT: Algae growth rate is optimal for colony")
        elif avg_growth > 3.5:
            print("  ✓ GOOD: Algae growth rate is suitable for colony needs")
        elif avg_growth > 2.5:
            print("  ⚠ MODERATE: Algae growth rate is acceptable but could be improved")
        else:
            print("  ✗ LOW: Algae growth rate is insufficient for colony")
        
        if avg_oxygen > 100:
            print("  ✓ EXCELLENT: Oxygen production meets colony requirements")
        elif avg_oxygen > 80:
            print("  ✓ GOOD: Oxygen production is adequate")
        elif avg_oxygen > 60:
            print("  ⚠ MODERATE: Consider additional algae cultivation areas")
        else:
            print("  ✗ LOW: Significant oxygen deficit - requires intervention")
        
        print()
        print("="*80)
        print()
        
        return self.simulation_data


def main():
    """Run multiple simulations to compare different configurations"""
    
    simulator = AlgaeSimulationCLI()
    
    # Simulation 1: Baseline (Iron-rich soil, Enzyme A, standard conditions)
    print("\n" + "#"*80)
    print("# SIMULATION 1: BASELINE CONDITIONS")
    print("#"*80)
    simulator.run_simulation(
        soil_type="Iron-rich",
        enzyme_type="Enzyme A",
        num_days=30,
        temp_min=18,
        temp_max=24,
        light_min=7,
        light_max=11,
        co2_min=0.04,
        co2_max=0.07
    )
    
    # Simulation 2: Enhanced enzyme (Iron-rich soil, Enzyme C, standard conditions)
    print("\n" + "#"*80)
    print("# SIMULATION 2: ENHANCED ENZYME (Enzyme C)")
    print("#"*80)
    simulator.run_simulation(
        soil_type="Iron-rich",
        enzyme_type="Enzyme C",
        num_days=30,
        temp_min=18,
        temp_max=24,
        light_min=7,
        light_max=11,
        co2_min=0.04,
        co2_max=0.07
    )
    
    # Simulation 3: Optimal conditions (Iron-rich soil, Enzyme C, optimal environment)
    print("\n" + "#"*80)
    print("# SIMULATION 3: OPTIMAL CONDITIONS")
    print("#"*80)
    simulator.run_simulation(
        soil_type="Iron-rich",
        enzyme_type="Enzyme C",
        num_days=30,
        temp_min=20,
        temp_max=22,
        light_min=8,
        light_max=11,
        co2_min=0.05,
        co2_max=0.07
    )
    
    # Simulation 4: Challenging conditions (Clay-based soil, Control, suboptimal environment)
    print("\n" + "#"*80)
    print("# SIMULATION 4: CHALLENGING CONDITIONS")
    print("#"*80)
    simulator.run_simulation(
        soil_type="Clay-based",
        enzyme_type="Control (None)",
        num_days=30,
        temp_min=15,
        temp_max=20,
        light_min=6,
        light_max=8,
        co2_min=0.03,
        co2_max=0.05
    )
    
    print("\n" + "#"*80)
    print("# SIMULATION COMPLETE")
    print("#"*80)


if __name__ == "__main__":
    main()
