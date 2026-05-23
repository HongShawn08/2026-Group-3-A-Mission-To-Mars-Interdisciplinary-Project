# Read the file
with open('algae_web_app.py', 'r') as f:
    content = f.read()

# Update button styling
old_buttons = '''        .button-group {
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
        }'''

new_buttons = '''        .button-group {
            display: flex;
            gap: 10px;
            margin-top: 28px;
        }
        
        .btn {
            flex: 1;
            padding: 10px 16px;
            border: none;
            border-radius: 3px;
            font-size: 0.9em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .btn-run {
            background: #2c3e50;
            color: white;
        }
        
        .btn-run:hover {
            background: #1a252f;
        }
        
        .btn-reset {
            background: #95a5a6;
            color: white;
        }
        
        .btn-reset:hover {
            background: #7f8c8d;
        }'''

content = content.replace(old_buttons, new_buttons)

# Update status styling
old_status = '''        .status {
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
        }'''

new_status = '''        .status {
            margin-top: 18px;
            padding: 12px;
            background: white;
            border-radius: 3px;
            text-align: center;
            font-weight: 500;
            font-size: 0.85em;
            color: #666;
            min-height: 18px;
            border: 1px solid #eee;
        }
        
        .status.running {
            color: #e67e22;
            background: #fef5e7;
            border-color: #f8d7a1;
        }
        
        .status.complete {
            color: #27ae60;
            background: #eafaf1;
            border-color: #a9dfbf;
        }'''

content = content.replace(old_status, new_status)

# Update charts styling
old_charts = '''        .charts {
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
        }'''

new_charts = '''        .charts {
            flex: 1;
            padding: 25px;
            display: flex;
            flex-direction: column;
            gap: 25px;
            overflow-y: auto;
            max-height: 800px;
        }
        
        .chart-container {
            background: white;
            padding: 18px;
            border: 1px solid #ddd;
            position: relative;
            height: 300px;
        }
        
        .chart-title {
            font-size: 0.95em;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 12px;
        }'''

content = content.replace(old_charts, new_charts)

# Update summary styling
old_summary = '''        .summary {
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
        }'''

new_summary = '''        .summary {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-top: 15px;
        }
        
        .summary-item {
            background: white;
            padding: 12px;
            border: 1px solid #ddd;
            border-left: 3px solid #2c3e50;
        }
        
        .summary-label {
            font-size: 0.8em;
            color: #666;
            margin-bottom: 4px;
        }
        
        .summary-value {
            font-size: 1.3em;
            font-weight: 600;
            color: #2c3e50;
        }
        
        .recommendation {
            background: white;
            padding: 12px;
            border: 1px solid #ddd;
            margin-top: 12px;
            border-left: 3px solid #e67e22;
            font-size: 0.9em;
            line-height: 1.5;
        }
        
        .recommendation.good {
            border-left-color: #27ae60;
        }
        
        .recommendation.poor {
            border-left-color: #c0392b;
        }'''

content = content.replace(old_summary, new_summary)

# Update loading styling
old_loading = '''        .loading {
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
        }'''

new_loading = '''        .loading {
            display: none;
            text-align: center;
            padding: 15px;
            color: #e67e22;
            font-size: 0.9em;
        }
        
        .spinner {
            display: inline-block;
            width: 16px;
            height: 16px;
            border: 2px solid #f3f3f3;
            border-top: 2px solid #e67e22;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin-right: 8px;
        }'''

content = content.replace(old_loading, new_loading)

# Save the file
with open('algae_web_app.py', 'w') as f:
    f.write(content)

print("CSS styling updated successfully!")
