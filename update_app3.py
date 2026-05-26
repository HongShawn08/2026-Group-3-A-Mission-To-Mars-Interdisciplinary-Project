# Read the file
with open('algae_web_app.py', 'r') as f:
    content = f.read()

# Replace Simulation Days input with slider
old_days = '''                <div class="control-group">
                    <label for="days">Simulation Days:</label>
                    <input type="number" id="days" value="30" min="10" max="100">
                </div>'''

new_days = '''                <div class="control-group">
                    <label>Simulation Days:</label>
                    <div class="slider-container">
                        <input type="range" id="days" value="30" min="10" max="100">
                        <div class="slider-label">
                            <span>10</span>
                            <span class="slider-value" id="daysValue">30</span>
                            <span>100</span>
                        </div>
                    </div>
                </div>'''

content = content.replace(old_days, new_days)

# Replace Temperature input with dual sliders
old_temp = '''                <div class="control-group">
                    <label>Temperature (°C):</label>
                    <input type="number" id="tempMin" value="18" min="10" max="30" placeholder="Min">
                    <input type="number" id="tempMax" value="24" min="10" max="30" placeholder="Max" style="margin-top: 8px;">
                    <div class="range-display">
                        <span id="tempRange">18°C - 24°C</span>
                    </div>
                </div>'''

new_temp = '''                <div class="control-group">
                    <label>Temperature (°C):</label>
                    <div class="slider-dual">
                        <div class="slider-dual-item">
                            <label style="font-size: 0.75em; color: #666;">Min</label>
                            <div class="slider-container">
                                <input type="range" id="tempMin" value="18" min="10" max="30">
                                <div style="text-align: center; font-size: 0.85em; color: #2c3e50; font-weight: 600;" id="tempMinValue">18</div>
                            </div>
                        </div>
                        <div class="slider-dual-item">
                            <label style="font-size: 0.75em; color: #666;">Max</label>
                            <div class="slider-container">
                                <input type="range" id="tempMax" value="24" min="10" max="30">
                                <div style="text-align: center; font-size: 0.85em; color: #2c3e50; font-weight: 600;" id="tempMaxValue">24</div>
                            </div>
                        </div>
                    </div>
                </div>'''

content = content.replace(old_temp, new_temp)

# Replace Light input with dual sliders
old_light = '''                <div class="control-group">
                    <label>Light Exposure (hrs):</label>
                    <input type="number" id="lightMin" value="7" min="6" max="12" placeholder="Min">
                    <input type="number" id="lightMax" value="11" min="6" max="12" placeholder="Max" style="margin-top: 8px;">
                    <div class="range-display">
                        <span id="lightRange">7 - 11 hrs</span>
                    </div>
                </div>'''

new_light = '''                <div class="control-group">
                    <label>Light Exposure (hrs):</label>
                    <div class="slider-dual">
                        <div class="slider-dual-item">
                            <label style="font-size: 0.75em; color: #666;">Min</label>
                            <div class="slider-container">
                                <input type="range" id="lightMin" value="7" min="6" max="12">
                                <div style="text-align: center; font-size: 0.85em; color: #2c3e50; font-weight: 600;" id="lightMinValue">7</div>
                            </div>
                        </div>
                        <div class="slider-dual-item">
                            <label style="font-size: 0.75em; color: #666;">Max</label>
                            <div class="slider-container">
                                <input type="range" id="lightMax" value="11" min="6" max="12">
                                <div style="text-align: center; font-size: 0.85em; color: #2c3e50; font-weight: 600;" id="lightMaxValue">11</div>
                            </div>
                        </div>
                    </div>
                </div>'''

content = content.replace(old_light, new_light)

# Replace CO2 input with dual sliders
old_co2 = '''                <div class="control-group">
                    <label>CO₂ Level:</label>
                    <input type="number" id="co2Min" value="0.04" min="0.03" max="0.08" step="0.01" placeholder="Min">
                    <input type="number" id="co2Max" value="0.07" min="0.03" max="0.08" step="0.01" placeholder="Max" style="margin-top: 8px;">
                    <div class="range-display">
                        <span id="co2Range">0.04 - 0.07</span>
                    </div>
                </div>'''

new_co2 = '''                <div class="control-group">
                    <label>CO2 Level:</label>
                    <div class="slider-dual">
                        <div class="slider-dual-item">
                            <label style="font-size: 0.75em; color: #666;">Min</label>
                            <div class="slider-container">
                                <input type="range" id="co2Min" value="0.04" min="0.03" max="0.08" step="0.01">
                                <div style="text-align: center; font-size: 0.85em; color: #2c3e50; font-weight: 600;" id="co2MinValue">0.04</div>
                            </div>
                        </div>
                        <div class="slider-dual-item">
                            <label style="font-size: 0.75em; color: #666;">Max</label>
                            <div class="slider-container">
                                <input type="range" id="co2Max" value="0.07" min="0.03" max="0.08" step="0.01">
                                <div style="text-align: center; font-size: 0.85em; color: #2c3e50; font-weight: 600;" id="co2MaxValue">0.07</div>
                            </div>
                        </div>
                    </div>
                </div>'''

content = content.replace(old_co2, new_co2)

# Remove emojis from buttons
content = content.replace('Run Simulation', 'Run Simulation')
content = content.replace('↻ Reset', 'Reset')
content = content.replace('Reset', 'Reset')

# Fix the button text
content = content.replace('<button class="btn btn-run" id="runBtn">Run Simulation</button>', '<button class="btn btn-run" id="runBtn">Run Simulation</button>')
content = content.replace('<button class="btn btn-reset" id="resetBtn">↻ Reset</button>', '<button class="btn btn-reset" id="resetBtn">Reset</button>')

# Save the file
with open('algae_web_app.py', 'w') as f:
    f.write(content)

print("HTML form controls updated to sliders!")
