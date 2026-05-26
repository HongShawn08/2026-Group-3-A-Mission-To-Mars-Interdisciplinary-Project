# Read the file
with open('algae_web_app.py', 'r') as f:
    content = f.read()

# Replace the old updateRanges function calls with new slider event listeners
old_js = '''        // Update range displays
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

new_js = '''        // Update slider displays
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

content = content.replace(old_js, new_js)

# Update the reset function
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

# Update recommendation text to remove symbols
content = content.replace("recommendation += '✓ EXCELLENT:", "recommendation += 'EXCELLENT:")
content = content.replace("recommendation += '✓ GOOD:", "recommendation += 'GOOD:")
content = content.replace("recommendation += '⚠ MODERATE:", "recommendation += 'MODERATE:")
content = content.replace("recommendation += '✗ LOW:", "recommendation += 'LOW:")

# Save the file
with open('algae_web_app.py', 'w') as f:
    f.write(content)

print("JavaScript updated for slider functionality!")
