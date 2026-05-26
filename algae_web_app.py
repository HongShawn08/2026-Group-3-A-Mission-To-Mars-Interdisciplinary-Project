"""
Mars Colony Algae Growth Simulation - Web Interface
Computer Science Component - IDP 2026

Flask web app for interactive algae growth simulation with real-time visualization.
"""

from flask import Flask, request, jsonify, Response
import random
import math
import json
from datetime import datetime

app = Flask(__name__)

# HTML Template for the web interface
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mars Algae Growth Simulation</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: system-ui, -apple-system, sans-serif;
            background: white;
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 3px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        
        .header {
            background: #2c3e50;
            color: white;
            padding: 40px;
            text-align: center;
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .header p {
            font-size: 1.1em;
            opacity: 0.9;
        }
        
        .content {
            display: flex;
            height: 100%;
        }
        
        .controls {
            flex: 0 0 350px;
            padding: 30px;
            background: #f5f5f5;
            border-right: 1px solid #ddd;
            overflow-y: auto;
            max-height: 800px;
        }
        
        .controls h2 {
            color: #2E7D32;
            margin-bottom: 20px;
            font-size: 1.3em;
        }
        
        .control-group {
            margin-bottom: 20px;
        }
        
        .control-group label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 500;
            font-size: 0.9em;
        }
        
        .control-group input[type="number"],
        .control-group select {
            width: 100%;
            padding: 10px;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-size: 0.9em;
            transition: border-color 0.3s;
        }
        
        .control-group input[type="number"]:focus,
        .control-group select:focus {
            outline: none;
            border-color: #2E7D32;
        }
        
        .range-display {
            display: flex;
            justify-content: space-between;
            margin-top: 8px;
            font-size: 0.85em;
            color: #666;
        }
        
        .button-group {
            display: flex;
            gap: 10px;
            margin-top: 30px;
        }
        
        .btn {
            flex: 1;
            padding: 12px 20px;
            border: none;
            border-radius: 5px;
            font-size: 1em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .btn-run {
            background: #2E7D32;
            color: white;
        }
        
        .btn-run:hover {
            background: #1B5E20;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(46, 125, 50, 0.3);
        }
        
        .btn-reset {
            background: #FFC107;
            color: #333;
        }
        
        .btn-reset:hover {
            background: #FFB300;
        }
        
        .btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
        }
        
        .status {
            margin-top: 20px;
            padding: 15px;
            background: white;
            border-radius: 5px;
            text-align: center;
            font-weight: 500;
            color: #666;
            min-height: 20px;
        }
        
        .status.running {
            color: #FF9800;
        }
        
        .status.complete {
            color: #2E7D32;
        }
        
        .charts {
            flex: 1;
            padding: 30px;
            display: flex;
            flex-direction: column;
            gap: 30px;
            overflow-y: auto;
            max-height: 800px;
        }
        
        .chart-container {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            position: relative;
            height: 350px;
        }
        
        .chart-title {
            font-size: 1.1em;
            font-weight: 600;
            color: #2E7D32;
            margin-bottom: 15px;
        }
        
        .summary {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-top: 20px;
        }
        
        .summary-item {
            background: #f9f9f9;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #2E7D32;
        }
        
        .summary-label {
            font-size: 0.85em;
            color: #666;
            margin-bottom: 5px;
        }
        
        .summary-value {
            font-size: 1.5em;
            font-weight: bold;
            color: #2E7D32;
        }
        
        .recommendation {
            background: white;
            padding: 15px;
            border-radius: 5px;
            margin-top: 15px;
            border-left: 4px solid #FF9800;
        }
        
        .recommendation.good {
            border-left-color: #2E7D32;
        }
        
        .recommendation.poor {
            border-left-color: #F44336;
        }
        
        .loading {
            display: none;
            text-align: center;
            padding: 20px;
            color: #FF9800;
        }
        
        .spinner {
            display: inline-block;
            width: 20px;
            height: 20px;
            border: 3px solid #f3f3f3;
            border-top: 3px solid #FF9800;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        @media (max-width: 768px) {
            .content {
                flex-direction: column;
            }
            
            .controls {
                flex: 0 0 auto;
                border-right: none;
                border-bottom: 1px solid #ddd;
                max-height: none;
            }
            
            .charts {
                max-height: none;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Mars Colony Algae Growth Simulation</h1>
            <p>Computer Science IDP 2026 - Interactive Environmental Modeling</p>
        </div>
        
        <div class="content">
            <div class="controls">
                <h2>Simulation Parameters</h2>
                
                <div class="control-group">
                    <label for="soil">Soil Type:</label>
                    <select id="soil">
                        <option value="Iron-rich">Iron-rich (1.25x)</option>
                        <option value="Sulfate-based" selected>Sulfate-based (1.0x)</option>
                        <option value="Clay-based">Clay-based (0.75x)</option>
                    </select>
                </div>
                
                <div class="control-group">
                    <label for="enzyme">Enzyme Type:</label>
                    <select id="enzyme">
                        <option value="Chromate Reductase" selected>Chromate Reductase (1.50x)</option>
                        <option value="Class II Chromate Reductase">Class II Chromate Reductase (1.30x)</option>
                        <option value="Urease">Urease (0.85x)</option>
                    </select>
                </div>
                
                <div class="control-group">
                    <label for="days">Simulation Days:</label>
                    <input type="range" id="days" value="30" min="10" max="100" style="width: 100%; cursor: pointer;">
                    <div style="text-align: center; margin-top: 8px; font-size: 0.9em; font-weight: 500; color: #333;"><span id="daysValue">30</span> days</div>
                </div>
                
                <h2 style="margin-top: 30px;">Environmental Ranges</h2>
                
                <div class="control-group">
                    <label>Temperature (°C):</label>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                        <div>
                            <label style="font-size: 0.85em; color: #666; display: block; margin-bottom: 4px;">Min</label>
                            <input type="range" id="tempMin" value="18" min="10" max="30" style="width: 100%; cursor: pointer;">
                            <div style="text-align: center; font-size: 0.85em; color: #333; margin-top: 4px;" id="tempMinValue">18</div>
                        </div>
                        <div>
                            <label style="font-size: 0.85em; color: #666; display: block; margin-bottom: 4px;">Max</label>
                            <input type="range" id="tempMax" value="24" min="10" max="30" style="width: 100%; cursor: pointer;">
                            <div style="text-align: center; font-size: 0.85em; color: #333; margin-top: 4px;" id="tempMaxValue">24</div>
                        </div>
                    </div>
                </div>
                
                <div class="control-group">
                    <label>Light Exposure (hrs):</label>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                        <div>
                            <label style="font-size: 0.85em; color: #666; display: block; margin-bottom: 4px;">Min</label>
                            <input type="range" id="lightMin" value="7" min="6" max="12" style="width: 100%; cursor: pointer;">
                            <div style="text-align: center; font-size: 0.85em; color: #333; margin-top: 4px;" id="lightMinValue">7</div>
                        </div>
                        <div>
                            <label style="font-size: 0.85em; color: #666; display: block; margin-bottom: 4px;">Max</label>
                            <input type="range" id="lightMax" value="11" min="6" max="12" style="width: 100%; cursor: pointer;">
                            <div style="text-align: center; font-size: 0.85em; color: #333; margin-top: 4px;" id="lightMaxValue">11</div>
                        </div>
                    </div>
                </div>
                
                <div class="control-group">
                    <label>CO₂ Level:</label>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                        <div>
                            <label style="font-size: 0.85em; color: #666; display: block; margin-bottom: 4px;">Min</label>
                            <input type="range" id="co2Min" value="0.04" min="0.03" max="0.08" step="0.01" style="width: 100%; cursor: pointer;">
                            <div style="text-align: center; font-size: 0.85em; color: #333; margin-top: 4px;" id="co2MinValue">0.04</div>
                        </div>
                        <div>
                            <label style="font-size: 0.85em; color: #666; display: block; margin-bottom: 4px;">Max</label>
                            <input type="range" id="co2Max" value="0.07" min="0.03" max="0.08" step="0.01" style="width: 100%; cursor: pointer;">
                            <div style="text-align: center; font-size: 0.85em; color: #333; margin-top: 4px;" id="co2MaxValue">0.07</div>
                        </div>
                    </div>
                </div>
                
                <div class="button-group">
                    <button class="btn btn-run" id="runBtn">Run Simulation</button>
                    <button class="btn btn-reset" id="resetBtn">Reset</button>
                </div>
                
                <div class="loading" id="loading">
                    <div class="spinner"></div>
                    <p>Running simulation...</p>
                </div>
                
                <div class="status" id="status">Ready</div>
            </div>
            
            <div class="charts">
                <div class="chart-container">
                    <div class="chart-title">Growth Rate Timeline</div>
                    <canvas id="growthChart"></canvas>
                </div>
                
                <div class="chart-container">
                    <div class="chart-title">Oxygen Production</div>
                    <canvas id="oxygenChart"></canvas>
                </div>
                
                <div id="summarySection" style="display: none;">
                    <div class="summary">
                        <div class="summary-item">
                            <div class="summary-label">Avg Growth Rate</div>
                            <div class="summary-value" id="avgGrowth">-</div>
                        </div>
                        <div class="summary-item">
                            <div class="summary-label">Total Biomass</div>
                            <div class="summary-value" id="totalBiomass">-</div>
                        </div>
                        <div class="summary-item">
                            <div class="summary-label">Avg O₂ Output</div>
                            <div class="summary-value" id="avgOxygen">-</div>
                        </div>
                        <div class="summary-item">
                            <div class="summary-label">Total O₂ Produced</div>
                            <div class="summary-value" id="totalOxygen">-</div>
                        </div>
                    </div>
                    
                    <div class="recommendation" id="recommendation"></div>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        let growthChart, oxygenChart;
        
        // Update slider value displays
        document.getElementById('days').addEventListener('input', e => {
            document.getElementById('daysValue').textContent = e.target.value;
        });
        document.getElementById('tempMin').addEventListener('input', e => {
            document.getElementById('tempMinValue').textContent = e.target.value;
        });
        document.getElementById('tempMax').addEventListener('input', e => {
            document.getElementById('tempMaxValue').textContent = e.target.value;
        });
        document.getElementById('lightMin').addEventListener('input', e => {
            document.getElementById('lightMinValue').textContent = e.target.value;
        });
        document.getElementById('lightMax').addEventListener('input', e => {
            document.getElementById('lightMaxValue').textContent = e.target.value;
        });
        document.getElementById('co2Min').addEventListener('input', e => {
            document.getElementById('co2MinValue').textContent = parseFloat(e.target.value).toFixed(2);
        });
        document.getElementById('co2Max').addEventListener('input', e => {
            document.getElementById('co2MaxValue').textContent = parseFloat(e.target.value).toFixed(2);
        });
        
        // Event listeners
        document.getElementById('runBtn').addEventListener('click', runSimulation);
        document.getElementById('resetBtn').addEventListener('click', resetForm);
        
        function resetForm() {
            document.getElementById('soil').value = 'Sulfate-based';
            document.getElementById('enzyme').value = 'Chromate Reductase';
            document.getElementById('days').value = 30;
            document.getElementById('tempMin').value = 18;
            document.getElementById('tempMax').value = 24;
            document.getElementById('lightMin').value = 7;
            document.getElementById('lightMax').value = 11;
            document.getElementById('co2Min').value = 0.04;
            document.getElementById('co2Max').value = 0.07;
            
            document.getElementById('daysValue').textContent = '30';
            document.getElementById('tempMinValue').textContent = '18';
            document.getElementById('tempMaxValue').textContent = '24';
            document.getElementById('lightMinValue').textContent = '7';
            document.getElementById('lightMaxValue').textContent = '11';
            document.getElementById('co2MinValue').textContent = '0.04';
            document.getElementById('co2MaxValue').textContent = '0.07';
            
            document.getElementById('summarySection').style.display = 'none';
            document.getElementById('status').textContent = 'Ready';
        }
        
        function runSimulation() {
            const params = {
                soil_type: document.getElementById('soil').value,
                enzyme_type: document.getElementById('enzyme').value,
                num_days: parseInt(document.getElementById('days').value),
                temp_min: parseFloat(document.getElementById('tempMin').value),
                temp_max: parseFloat(document.getElementById('tempMax').value),
                light_min: parseFloat(document.getElementById('lightMin').value),
                light_max: parseFloat(document.getElementById('lightMax').value),
                co2_min: parseFloat(document.getElementById('co2Min').value),
                co2_max: parseFloat(document.getElementById('co2Max').value)
            };
            
            // Validate
            if (params.temp_min >= params.temp_max) {
                alert('Temperature Min must be less than Max');
                return;
            }
            if (params.light_min >= params.light_max) {
                alert('Light Min must be less than Max');
                return;
            }
            if (params.co2_min >= params.co2_max) {
                alert('CO₂ Min must be less than Max');
                return;
            }
            
            document.getElementById('loading').style.display = 'block';
            document.getElementById('status').textContent = 'Running...';
            document.getElementById('status').className = 'status running';
            document.getElementById('runBtn').disabled = true;
            
            fetch('/simulate', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(params)
            })
            .then(r => r.json())
            .then(data => displayResults(data))
            .catch(e => {
                console.error(e);
                document.getElementById('status').textContent = 'Error running simulation';
                document.getElementById('status').className = 'status';
            })
            .finally(() => {
                document.getElementById('loading').style.display = 'none';
                document.getElementById('runBtn').disabled = false;
            });
        }
        
        function displayResults(data) {
            const days = data.data.map(d => d.day);
            const growth = data.data.map(d => d.growth_rate);
            const oxygen = data.data.map(d => d.oxygen_output);
            
            // Growth Chart
            if (growthChart) growthChart.destroy();
            growthChart = new Chart(document.getElementById('growthChart'), {
                type: 'line',
                data: {
                    labels: days,
                    datasets: [{
                        label: 'Growth Rate (g/day)',
                        data: growth,
                        borderColor: '#2E7D32',
                        backgroundColor: 'rgba(46, 125, 50, 0.1)',
                        tension: 0.4,
                        fill: true,
                        pointRadius: 4,
                        pointBackgroundColor: '#2E7D32',
                        pointBorderColor: '#fff',
                        pointBorderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: true,
                            labels: {
                                usePointStyle: true,
                                padding: 15
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {display: true, text: 'Growth Rate (g/day)'}
                        }
                    }
                }
            });
            
            // Oxygen Chart
            if (oxygenChart) oxygenChart.destroy();
            oxygenChart = new Chart(document.getElementById('oxygenChart'), {
                type: 'line',
                data: {
                    labels: days,
                    datasets: [{
                        label: 'O₂ Production (mL/hour)',
                        data: oxygen,
                        borderColor: '#1976D2',
                        backgroundColor: 'rgba(25, 118, 210, 0.1)',
                        tension: 0.4,
                        fill: true,
                        pointRadius: 4,
                        pointBackgroundColor: '#1976D2',
                        pointBorderColor: '#fff',
                        pointBorderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: true,
                            labels: {
                                usePointStyle: true,
                                padding: 15
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {display: true, text: 'O₂ Production (mL/hour)'}
                        }
                    }
                }
            });
            
            // Summary
            const avgGrowth = (growth.reduce((a,b)=>a+b,0)/growth.length).toFixed(2);
            const totalBiomass = growth.reduce((a,b)=>a+b,0).toFixed(2);
            const avgOxygen = (oxygen.reduce((a,b)=>a+b,0)/oxygen.length).toFixed(2);
            const totalOxygen = oxygen.reduce((a,b)=>a+b,0).toFixed(2);
            
            document.getElementById('avgGrowth').textContent = `${avgGrowth} g/day`;
            document.getElementById('totalBiomass').textContent = `${totalBiomass} g`;
            document.getElementById('avgOxygen').textContent = `${avgOxygen} mL/h`;
            document.getElementById('totalOxygen').textContent = `${totalOxygen} mL`;
            
            let recommendation = '<strong>Colony Assessment:</strong><br>';
            let className = 'good';
            
            if (avgGrowth > 4.5) {
                recommendation += 'EXCELLENT: Algae growth rate is optimal for colony<br>';
            } else if (avgGrowth > 3.5) {
                recommendation += 'GOOD: Algae growth rate is suitable for colony needs<br>';
            } else if (avgGrowth > 2.5) {
                recommendation += 'MODERATE: Algae growth rate is acceptable but could be improved<br>';
            } else {
                recommendation += 'LOW: Algae growth rate is insufficient for colony<br>';
                className = 'poor';
            }
            
            if (avgOxygen > 100) {
                recommendation += 'EXCELLENT: Oxygen production meets colony requirements<br>';
            } else if (avgOxygen > 80) {
                recommendation += 'GOOD: Oxygen production is adequate<br>';
            } else if (avgOxygen > 60) {
                recommendation += 'MODERATE: Consider additional algae cultivation areas<br>';
            } else {
                recommendation += 'LOW: Significant oxygen deficit - requires intervention';
                className = 'poor';
            }
            
            document.getElementById('recommendation').innerHTML = recommendation;
            document.getElementById('recommendation').className = 'recommendation ' + className;
            
            document.getElementById('summarySection').style.display = 'block';
            document.getElementById('status').textContent = 'Simulation complete!';
            document.getElementById('status').className = 'status complete';
        }
    </script>
</body>
</html>
'''

def generate_algae_data(num_days, soil_type, enzyme_type, temp_min, temp_max, 
                       light_min, light_max, co2_min, co2_max):
    """Generate synthetic algae growth data"""
    
    soil_coefficients = {
        "Iron-rich": 1.25,
        "Sulfate-based": 1.0,
        "Clay-based": 0.75
    }
    
    enzyme_coefficients = {
        "Chromate Reductase": 1.50,
        "Class II Chromate Reductase": 1.30,
        "Urease": 0.85
    }
    
    soil_factor = soil_coefficients[soil_type]
    enzyme_factor = enzyme_coefficients[enzyme_type]
    
    data = []
    for day in range(1, num_days + 1):
        light_hours = random.uniform(light_min, light_max)
        temperature = random.uniform(temp_min, temp_max)
        co2_level = random.uniform(co2_min, co2_max)
        
        # Calculate growth factors
        light_factor = (light_hours - 6) / 6
        
        optimal_temp = 21
        temp_deviation = abs(temperature - optimal_temp)
        temp_factor = max(0.3, 1 - (temp_deviation ** 2) / 80)
        
        co2_factor = math.log(1 + co2_level * 60) / math.log(1 + 0.08 * 60)
        
        time_factor = 1 + (0.025 * day) - (0.00025 * day ** 2)
        time_factor = max(0.6, min(1.4, time_factor))
        
        base_growth = 4.2
        growth_rate = (base_growth * light_factor * temp_factor * co2_factor * 
                      soil_factor * enzyme_factor * time_factor)
        
        noise = growth_rate * random.uniform(-0.03, 0.03)
        growth_rate = max(0.1, growth_rate + noise)
        
        oxygen_output = growth_rate * random.uniform(4.5, 5.5)
        
        data.append({
            'day': day,
            'temperature': round(temperature, 1),
            'light_hours': round(light_hours, 1),
            'co2_level': round(co2_level, 3),
            'growth_rate': round(growth_rate, 2),
            'oxygen_output': round(oxygen_output, 2)
        })
    
    return data

@app.route('/')
def index():
    from flask import Response
    return Response(HTML_TEMPLATE, mimetype='text/html')

@app.route('/simulate', methods=['POST'])
def simulate():
    params = request.json
    
    data = generate_algae_data(
        params['num_days'],
        params['soil_type'],
        params['enzyme_type'],
        params['temp_min'],
        params['temp_max'],
        params['light_min'],
        params['light_max'],
        params['co2_min'],
        params['co2_max']
    )
    
    return jsonify({'data': data})

if __name__ == '__main__':
    print("\n" + "="*60)
    print("Mars Algae Growth Simulation - Web Interface")
    print("="*60)
    print("\n🚀 Starting web server...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("\nPress Ctrl+C to stop the server\n")
    app.run(debug=False, port=5000)
