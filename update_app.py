import re

# Read the file
with open('algae_web_app.py', 'r') as f:
    content = f.read()

# Replace gradient background with plain white
content = content.replace(
    "background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);",
    "background: #ffffff;"
)

# Replace Segoe UI font
content = content.replace(
    "font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;",
    "font-family: system-ui, -apple-system, sans-serif;"
)

# Replace container rounded corners with plain border
content = content.replace(
    "border-radius: 15px;\n            box-shadow: 0 20px 60px rgba(0,0,0,0.3);",
    "border: 1px solid #ddd;"
)

# Replace header gradient
content = content.replace(
    "background: linear-gradient(135deg, #2E7D32 0%, #1B5E20 100%);",
    "background: #2c3e50;"
)

# Replace header padding and add border
content = content.replace(
    "            padding: 40px;\n            text-align: center;",
    "            padding: 30px 40px;\n            border-bottom: 1px solid #ddd;\n            text-align: center;"
)

# Replace header h1 size
content = content.replace(
    "        .header h1 {\n            font-size: 2.5em;",
    "        .header h1 {\n            font-size: 1.8em;"
)

# Replace header h1 margin
content = content.replace(
    "            margin-bottom: 10px;",
    "            margin-bottom: 8px;\n            font-weight: 600;"
)

# Replace paragraph styling
content = content.replace(
    '            font-size: 1.1em;\n            opacity: 0.9;',
    '            font-size: 0.95em;\n            color: #bbb;'
)

# Replace controls background
content = content.replace(
    "            background: #f5f5f5;",
    "            background: #f8f8f8;"
)

# Replace controls width
content = content.replace(
    "            flex: 0 0 350px;",
    "            flex: 0 0 320px;"
)

# Add body color
content = content.replace(
    "            padding: 20px;\n        }",
    '            padding: 20px;\n            color: #333;\n        }'
)

# Replace controls h2 color and font
content = content.replace(
    '        .controls h2 {\n            color: #2E7D32;\n            margin-bottom: 20px;\n            font-size: 1.3em;',
    '        .controls h2 {\n            color: #2c3e50;\n            margin-bottom: 18px;\n            font-size: 0.95em;\n            font-weight: 600;\n            text-transform: uppercase;\n            letter-spacing: 0.5px;'
)

# Update input[type="number"] and select styling
old_input = '''        .control-group input[type="number"],
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
        }'''

new_input = '''        .control-group select {
            width: 100%;
            padding: 8px 10px;
            border: 1px solid #ccc;
            border-radius: 3px;
            font-size: 0.9em;
            background: white;
            color: #333;
        }
        
        .control-group select:focus {
            outline: none;
            border-color: #2c3e50;
            box-shadow: 0 0 3px rgba(44, 62, 80, 0.2);
        }
        
        .slider-container {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        
        input[type="range"] {
            width: 100%;
            height: 5px;
            border-radius: 3px;
            background: #ddd;
            outline: none;
            -webkit-appearance: none;
        }
        
        input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: #2c3e50;
            cursor: pointer;
        }
        
        input[type="range"]::-moz-range-thumb {
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: #2c3e50;
            cursor: pointer;
            border: none;
        }
        
        .slider-label {
            display: flex;
            justify-content: space-between;
            font-size: 0.8em;
            color: #666;
        }
        
        .slider-value {
            font-weight: 600;
            color: #2c3e50;
        }
        
        .slider-dual {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
        }
        
        .slider-dual-item {
            display: flex;
            flex-direction: column;
            gap: 5px;
        }
        
        .slider-dual-item label {
            margin-bottom: 0;
            font-size: 0.8em;
        }'''

content = content.replace(old_input, new_input)

# Save the file
with open('algae_web_app.py', 'w') as f:
    f.write(content)

print("File updated successfully!")
