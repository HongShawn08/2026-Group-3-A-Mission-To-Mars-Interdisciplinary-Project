# Read the file
with open('algae_web_app.py', 'r') as f:
    content = f.read()

# ===== UPDATE 1: Change font family =====
content = content.replace(
    "font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;",
    "font-family: system-ui, -apple-system, sans-serif;"
)

# ===== UPDATE 2: Change body background =====
content = content.replace(
    "background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);",
    "background: #ffffff;"
)

# ===== UPDATE 3: Change header background =====
content = content.replace(
    "background: linear-gradient(135deg, #2E7D32 0%, #1B5E20 100%);",
    "background: #2c3e50;"
)

# ===== UPDATE 4: Change container border radius =====
content = content.replace(
    "border-radius: 15px;",
    "border-radius: 0px;"
)

# ===== UPDATE 5: Change container shadow =====
content = content.replace(
    "box-shadow: 0 20px 60px rgba(0,0,0,0.3);",
    "box-shadow: 0 1px 3px rgba(0,0,0,0.1);"
)

# ===== UPDATE 6: Change header h1 font size and color references =====
content = content.replace(
    "color: #2E7D32;",
    "color: #2c3e50;"
)

# ===== UPDATE 7: Change controls background =====
content = content.replace(
    "background: #f5f5f5;",
    "background: #f8f8f8;"
)

# ===== UPDATE 8: Replace Simulation Days input with slider =====
old_days_input = '''                <div class="control-group">
                    <label for="days">Simulation Days:</label>
                    <input type="number" id="days" value="30" min="10" max="100">
                </div>'''

new_days_input = '''                <div class="control-group">
                    <label>Simulation Days:</label>
                    <div class="slider-container">
                        <input type="range" id="days" value="30" min="10" max="100" class="slider">
                        <div class="slider-labels">
                            <span>10</span>
                            <span id="daysValue">30</span>
                            <span>100</span>
                        </div>
                    </div>
                </div>'''

content = content.replace(old_days_input, new_days_input)

# ===== UPDATE 9: Replace Temperature inputs with dual sliders =====
old_temp_input = '''                <div class="control-group">
                    <label>Temperature (°C):</label>
                    <input type="number" id="tempMin" value="18" min="10" max="30" placeholder="Min">
                    <input type="number" id="tempMax" value="24" min="10" max="30" placeholder="Max" style="margin-top: 8px;">
                    <div class="range-display">
                        <span id="tempRange">18°C - 24°C</span>
                    </div>
                </div>'''

new_temp_input = '''                <div class="control-group">
                    <label>Temperature (°C):</label>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                        <div>
                            <div style="font-size: 0.75em; color: #666; margin-bottom: 4px;">Min</div>
                            <div class="slider-container">
                                <input type="range" id="tempMin" value="18" min="10" max="30" class="slider">
                                <div style="text-align: center; font-size: 0.85em; color: #2c3e50; font-weight: 600;" id="tempMinValue">18</div>
                            </div>
                        </div>
                        <div>
                            <div style="font-size: 0.75em; color: #666; margin-bottom: 4px;">Max</div>
                            <div class="slider-container">
                                <input type="range" id="tempMax" value="24" min="10" max="30" class="slider">
                                <div style="text-align: center; font-size: 0.85em; color: #2c3e50; font-weight: 600;" id="tempMaxValue">24</div>
                            </div>
                        </div>
                    </div>
                </div>'''

content = content.replace(old_temp_input, new_temp_input)

# ===== UPDATE 10: Replace Light inputs with dual sliders =====
old_light_input = '''                <div class="control-group">
                    <label>Light Exposure (hrs):</label>
                    <input type="number" id="lightMin" value="7" min="6" max="12" placeholder="Min">
                    <input type="number" id="lightMax" value="11" min="6" max="12" placeholder="Max" style="margin-top: 8px;">
                    <div class="range-display">
                        <span id="lightRange">7 - 11 hrs</span>
                    </div>
                </div>'''

new_light_input = '''                <div class="control-group">
                    <label>Light Exposure (hrs):</label>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                        <div>
                            <div style="font-size: 0.75em; color: #666; margin-bottom: 4px;">Min</div>
                            <div class="slider-container">
                                <input type="range" id="lightMin" value="7" min="6" max="12" class="slider">
                                <div style="text-align: center; font-size: 0.85em; color: #2c3e50; font-weight: 600;" id="lightMinValue">7</div>
                            </div>
                        </div>
                        <div>
                            <div style="font-size: 0.75em; color: #666; margin-bottom: 4px;">Max</div>
                            <div class="slider-container">
                                <input type="range" id="lightMax" value="11" min="6" max="12" class="slider">
                                <div style="text-align: center; font-size: 0.85em; color: #2c3e50; font-weight: 600;" id="lightMaxValue">11</div>
                            </div>
                        </div>
                    </div>
                </div>'''

content = content.replace(old_light_input, new_light_input)

# ===== UPDATE 11: Replace CO2 inputs with dual sliders =====
old_co2_input = '''                <div class="control-group">
                    <label>CO₂ Level:</label>
                    <input type="number" id="co2Min" value="0.04" min="0.03" max="0.08" step="0.01" placeholder="Min">
                    <input type="number" id="co2Max" value="0.07" min="0.03" max="0.08" step="0.01" placeholder="Max" style="margin-top: 8px;">
                    <div class="range-display">
                        <span id="co2Range">0.04 - 0.07</span>
                    </div>
                </div>'''

new_co2_input = '''                <div class="control-group">
                    <label>CO₂ Level:</label>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                        <div>
                            <div style="font-size: 0.75em; color: #666; margin-bottom: 4px;">Min</div>
                            <div class="slider-container">
                                <input type="range" id="co2Min" value="0.04" min="0.03" max="0.08" step="0.01" class="slider">
                                <div style="text-align: center; font-size: 0.85em; color: #2c3e50; font-weight: 600;" id="co2MinValue">0.04</div>
                            </div>
                        </div>
                        <div>
                            <div style="font-size: 0.75em; color: #666; margin-bottom: 4px;">Max</div>
                            <div class="slider-container">
                                <input type="range" id="co2Max" value="0.07" min="0.03" max="0.08" step="0.01" class="slider">
                                <div style="text-align: center; font-size: 0.85em; color: #2c3e50; font-weight: 600;" id="co2MaxValue">0.07</div>
                            </div>
                        </div>
                    </div>
                </div>'''

content = content.replace(old_co2_input, new_co2_input)

# ===== UPDATE 12: Update buttons to remove emoji =====
content = content.replace(
    '<button class="btn btn-run" id="runBtn">▶ Run Simulation</button>',
    '<button class="btn btn-run" id="runBtn">Run Simulation</button>'
)

content = content.replace(
    '<button class="btn btn-reset" id="resetBtn">↻ Reset</button>',
    '<button class="btn btn-reset" id="resetBtn">Reset</button>'
)

# ===== UPDATE 13: Update header to remove emoji =====
content = content.replace(
    '<h1>🚀 Mars Colony Algae Growth Simulation</h1>',
    '<h1>Mars Colony Algae Growth Simulation</h1>'
)

# ===== UPDATE 14: Replace updateRanges event listeners with slider input handlers =====
old_listeners = '''        // Update range displays
        document.getElementById('tempMin').addEventListener('change', updateRanges);
        document.getElementById('tempMax').addEventListener('change', updateRanges);
        document.getElementById('lightMin').addEventListener('change', updateRanges);
        document.getElementById('lightMax').addEventListener('change', updateRanges);
        document.getElementById('co2Min').addEventListener('change', updateRanges);
        document.getElementById('co2Max').addEventListener('change', updateRanges);
        
        function updateRanges() {
            document.getElementById('tempRange').textContent = 
                `${document.getElementById('tempMin').value}°C - ${document.getElementById('tempMax').value}°C`;
            document.getElementById('lightRange').textContent = 
                `${document.getElementById('lightMin').value} - ${document.getElementById('lightMax').value} hrs`;
            document.getElementById('co2Range').textContent = 
                `${document.getElementById('co2Min').value} - ${document.getElementById('co2Max').value}`;
        }'''

new_listeners = '''        // Update slider displays
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
        });'''

content = content.replace(old_listeners, new_listeners)

# ===== UPDATE 15: Update resetForm to update slider displays =====
old_reset = '''        function resetForm() {
            document.getElementById('soil').value = 'Sulfate-based';
            document.getElementById('enzyme').value = 'Chromate Reductase';
            document.getElementById('days').value = 30;
            document.getElementById('tempMin').value = 18;
            document.getElementById('tempMax').value = 24;
            document.getElementById('lightMin').value = 7;
            document.getElementById('lightMax').value = 11;
            document.getElementById('co2Min').value = 0.04;
            document.getElementById('co2Max').value = 0.07;
            updateRanges();
            document.getElementById('summarySection').style.display = 'none';
            document.getElementById('status').textContent = 'Ready';
        }'''

new_reset = '''        function resetForm() {
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
        }'''

content = content.replace(old_reset, new_reset)

# Save the file
with open('algae_web_app.py', 'w') as f:
    f.write(content)

print("✓ All updates completed successfully!")
