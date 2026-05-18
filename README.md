# 2026 Group 3: Mission To Mars Interdisciplinary Project
## Mars Colony Algae Growth Simulation

### Overview
This repository contains Group 3's computer science component for the 11th grade Mission to Mars Interdisciplinary Project at CAMS. Our simulation models algae growth on Mars under varying environmental conditions to evaluate its viability as both an oxygen production system and sustainable food source for our colony.

**Research Question:** How do different environmental factors (soil composition, enzyme types, temperature, light exposure) affect algae growth rates and oxygen output on Mars?

### Team Members
- **Shawn** - Lead Developer & Data Analysis
- [Team Member 2] - [Role]
- [Team Member 3] - [Role]

*Additional contributors from Biotech and Engineering pathways TBD*

### Project Scope
This simulation addresses the **Biotechnology + Computer Science** intersection of our colony mission by:
- Generating synthetic datasets modeling algae cultivation under Martian conditions
- Analyzing growth patterns to optimize oxygen production and food sustainability
- Supporting colony life support system design with data-driven recommendations

### Technologies Used
- **Language:** Python 3.x
- **Libraries:** `random` (data generation), `matplotlib`/`seaborn` (visualization)
- **Data Structures:** Lists, dictionaries, nested data structures
- **Analysis Methods:** Rule-based modeling with controlled randomness, regression analysis

### Key Features
- **Synthetic Dataset Generation:** 50-200+ data points modeling realistic algae growth scenarios
- **Multi-variable Analysis:** Tracks soil type, enzyme concentration, temperature, CO₂ levels, light exposure, and growth rate
- **Dual Visualizations:** Line graphs (growth over time) and bar charts (comparison across conditions)
- **Decision Support:** Provides colony recommendations based on optimal growth parameters

### Computer Science Concepts Demonstrated
* Python lists and dictionaries for data storage
* `append()`, `insert()`, `remove()`, `pop()` operations
* List traversal with loops
* Conditional filtering and threshold detection
* Data analysis and pattern recognition
* Visualization with matplotlib/seaborn  

### How to Run
```bash
# Clone the repository
git clone https://github.com/HongShawn08/2026-Group-3-A-Mission-To-Mars-Interdisciplinary-Project.git

# Navigate to the project directory
cd 2026-Group-3-A-Mission-To-Mars-Interdisciplinary-Project

# Install dependencies (if needed)
pip install matplotlib seaborn

# Run the simulation
python algae_simulation.py
```

### Project Structure
├── algae_simulation.py       # Main simulation code
├── data_generation.py        # Synthetic dataset creation
├── analysis.py               # Data processing and statistical analysis
├── visualizations.py         # Chart generation scripts
├── datasets/                 # Generated CSV files
│   └── algae_growth_data.csv
├── charts/                   # Output visualizations
│   ├── growth_over_time.png
│   └── enzyme_comparison.png
├── prompts/                  # AI/LLM prompts used for model development
│   └── dataset_generation_log.md
└── README.md

### Dataset Variables
- **Soil Composition:** Simulated Martian regolith mixes (iron-rich, sulfate-based, etc.)
- **Enzyme Type:** Growth stimulants tested (Enzyme A, B, C)
- **Temperature:** 10-30°C (controlled habitat range)
- **CO₂ Levels:** 0.03-0.08 (Martian atmospheric simulation)
- **Light Exposure:** 6-12 hours (solar panel-powered grow lights)
- **Growth Rate:** grams/day (dependent variable)
- **Oxygen Output:** mL/hour (secondary output)

### Analysis & Findings
*[This section will be updated after data generation and analysis]*

**Preliminary Hypothesis:**  
Higher enzyme concentrations and iron-rich regolith will maximize algae growth, but temperature must remain within 18-24°C for optimal oxygen production efficiency.

### IDP Integration
This simulation fulfills:
- **CS Rubric:** Data structure use, iteration/processing, synthetic dataset generation, dual visualizations
- **Biotech Connection:** Agriculture/food production systems, environmental air/water management
- **Engineering Tie-in:** Life support system optimization, resource forecasting
- **Math Component:** Regression modeling on sensor data for growth rate predictions

### License
No license (academic project - CAMS Class of 2027)

### Acknowledgments
- Shawn Hong, Derrick Kwan, John Louie Maniego
