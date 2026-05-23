# Read the file
with open('algae_web_app.py', 'r') as f:
    content = f.read()

# Update chart colors to match new theme
content = content.replace("borderColor: '#2E7D32'", "borderColor: '#2c3e50'")
content = content.replace("backgroundColor: 'rgba(46, 125, 50, 0.1)'", "backgroundColor: 'rgba(44, 62, 80, 0.05)'")
content = content.replace("pointBackgroundColor: '#2E7D32'", "pointBackgroundColor: '#2c3e50'")

# Remove emoji from header  
content = content.replace("            <h1>🚀 Mars Colony Algae Growth Simulation</h1>",
                         "            <h1>Mars Colony Algae Growth Simulation</h1>")

# Update the summary text generation to remove emojis (for the displayed recommendations)
content = content.replace("            let recommendation = '<strong>Colony Assessment:</strong><br>';",
                         "            let recommendation = '<strong>Colony Assessment</strong><br>';")

# Update display styles to be cleaner
content = content.replace("            borderWidth: 2", "            borderWidth: 2")

# Save the file
with open('algae_web_app.py', 'w') as f:
    f.write(content)

print("Chart colors and emojis updated!")
