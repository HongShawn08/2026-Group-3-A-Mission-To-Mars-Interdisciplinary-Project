with open('algae_web_app.py', 'r') as f:
    content = f.read()

# Change font
content = content.replace(
    "font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;",
    "font-family: system-ui, -apple-system, sans-serif;"
)

# Remove purple gradient from body
content = content.replace(
    "background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);",
    "background: white;"
)

# Change header from gradient to solid color
content = content.replace(
    "background: linear-gradient(135deg, #2E7D32 0%, #1B5E20 100%);",
    "background: #2c3e50;"
)

# Remove emoji from header
content = content.replace(
    "🚀 Mars Colony Algae Growth Simulation",
    "Mars Colony Algae Growth Simulation"
)

# Simplify container styling
content = content.replace(
    "border-radius: 15px;",
    "border-radius: 3px;"
)

content = content.replace(
    "box-shadow: 0 20px 60px rgba(0,0,0,0.3);",
    "box-shadow: 0 1px 3px rgba(0,0,0,0.1);"
)

# Remove buttons emoji
content = content.replace(
    "▶ Run Simulation",
    "Run Simulation"
)

content = content.replace(
    "↻ Reset",
    "Reset"
)

with open('algae_web_app.py', 'w') as f:
    f.write(content)

print("✓ Basic styling updated!")
