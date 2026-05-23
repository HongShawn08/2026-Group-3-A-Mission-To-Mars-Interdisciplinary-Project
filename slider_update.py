with open('algae_web_app.py', 'r') as f:
    lines = f.readlines()

# Find and replace specific lines manually to avoid breaking the template
output = []
i = 0
while i < len(lines):
    line = lines[i]
    
    # Replace Simulation Days input  
    if 'id="days"' in line and 'type="number"' in line:
        # Replace the number input with a range slider
        indent = len(line) - len(line.lstrip())
        output.append(' ' * indent + '<input type="range" id="days" value="30" min="10" max="100" style="width: 100%; cursor: pointer;">\n')
        output.append(' ' * indent + '<div style="text-align: center; margin-top: 8px; font-size: 0.9em; font-weight: 500; color: #333;"><span id="daysValue">30</span> days</div>\n')
        i += 1
        continue
    
    # Replace Temperature inputs
    elif 'id="tempMin"' in line and 'type="number"' in line:
        indent = len(line) - len(line.lstrip())
        # Look ahead to find the matching closing div and tempMax
        j = i
        while j < len(lines) and 'id="tempMax"' not in lines[j]:
            j += 1
        # Found tempMax at lines[j]
        # Replace with dual sliders
        output.append(' ' * indent + '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">\n')
        output.append(' ' * indent + '    <div>\n')
        output.append(' ' * indent + '        <label style="font-size: 0.85em; color: #666; display: block; margin-bottom: 4px;">Min</label>\n')
        output.append(' ' * indent + '        <input type="range" id="tempMin" value="18" min="10" max="30" style="width: 100%; cursor: pointer;">\n')
        output.append(' ' * indent + '        <div style="text-align: center; font-size: 0.85em; color: #333; margin-top: 4px;" id="tempMinValue">18</div>\n')
        output.append(' ' * indent + '    </div>\n')
        output.append(' ' * indent + '    <div>\n')
        output.append(' ' * indent + '        <label style="font-size: 0.85em; color: #666; display: block; margin-bottom: 4px;">Max</label>\n')
        output.append(' ' * indent + '        <input type="range" id="tempMax" value="24" min="10" max="30" style="width: 100%; cursor: pointer;">\n')
        output.append(' ' * indent + '        <div style="text-align: center; font-size: 0.85em; color: #333; margin-top: 4px;" id="tempMaxValue">24</div>\n')
        output.append(' ' * indent + '    </div>\n')
        output.append(' ' * indent + '</div>\n')
        
        # Skip old temperature lines
        i = j + 1
        # Skip the range-display div if present
        if i < len(lines) and 'range-display' in lines[i]:
            i += 3  # Skip <div>, <span>, </div>
        continue
        
    # Replace Light inputs
    elif 'id="lightMin"' in line and 'type="number"' in line:
        indent = len(line) - len(line.lstrip())
        j = i
        while j < len(lines) and 'id="lightMax"' not in lines[j]:
            j += 1
        # Replace with dual sliders
        output.append(' ' * indent + '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">\n')
        output.append(' ' * indent + '    <div>\n')
        output.append(' ' * indent + '        <label style="font-size: 0.85em; color: #666; display: block; margin-bottom: 4px;">Min</label>\n')
        output.append(' ' * indent + '        <input type="range" id="lightMin" value="7" min="6" max="12" style="width: 100%; cursor: pointer;">\n')
        output.append(' ' * indent + '        <div style="text-align: center; font-size: 0.85em; color: #333; margin-top: 4px;" id="lightMinValue">7</div>\n')
        output.append(' ' * indent + '    </div>\n')
        output.append(' ' * indent + '    <div>\n')
        output.append(' ' * indent + '        <label style="font-size: 0.85em; color: #666; display: block; margin-bottom: 4px;">Max</label>\n')
        output.append(' ' * indent + '        <input type="range" id="lightMax" value="11" min="6" max="12" style="width: 100%; cursor: pointer;">\n')
        output.append(' ' * indent + '        <div style="text-align: center; font-size: 0.85em; color: #333; margin-top: 4px;" id="lightMaxValue">11</div>\n')
        output.append(' ' * indent + '    </div>\n')
        output.append(' ' * indent + '</div>\n')
        
        # Skip old light lines
        i = j + 1
        # Skip the range-display div if present
        if i < len(lines) and 'range-display' in lines[i]:
            i += 3  # Skip <div>, <span>, </div>
        continue
        
    # Replace CO2 inputs
    elif 'id="co2Min"' in line and 'type="number"' in line:
        indent = len(line) - len(line.lstrip())
        j = i
        while j < len(lines) and 'id="co2Max"' not in lines[j]:
            j += 1
        # Replace with dual sliders
        output.append(' ' * indent + '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">\n')
        output.append(' ' * indent + '    <div>\n')
        output.append(' ' * indent + '        <label style="font-size: 0.85em; color: #666; display: block; margin-bottom: 4px;">Min</label>\n')
        output.append(' ' * indent + '        <input type="range" id="co2Min" value="0.04" min="0.03" max="0.08" step="0.01" style="width: 100%; cursor: pointer;">\n')
        output.append(' ' * indent + '        <div style="text-align: center; font-size: 0.85em; color: #333; margin-top: 4px;" id="co2MinValue">0.04</div>\n')
        output.append(' ' * indent + '    </div>\n')
        output.append(' ' * indent + '    <div>\n')
        output.append(' ' * indent + '        <label style="font-size: 0.85em; color: #666; display: block; margin-bottom: 4px;">Max</label>\n')
        output.append(' ' * indent + '        <input type="range" id="co2Max" value="0.07" min="0.03" max="0.08" step="0.01" style="width: 100%; cursor: pointer;">\n')
        output.append(' ' * indent + '        <div style="text-align: center; font-size: 0.85em; color: #333; margin-top: 4px;" id="co2MaxValue">0.07</div>\n')
        output.append(' ' * indent + '    </div>\n')
        output.append(' ' * indent + '</div>\n')
        
        # Skip old CO2 lines
        i = j + 1
        # Skip the range-display div if present
        if i < len(lines) and 'range-display' in lines[i]:
            i += 3  # Skip <div>, <span>, </div>
        continue
    else:
        output.append(line)
        i += 1

with open('algae_web_app.py', 'w') as f:
    f.writelines(output)

print("✓ Input controls replaced with sliders!")
