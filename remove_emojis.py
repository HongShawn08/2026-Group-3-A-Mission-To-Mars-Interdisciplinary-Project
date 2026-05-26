with open('algae_web_app.py', 'r') as f:
    content = f.read()

# Remove emoji from recommendations
content = content.replace("'✓ EXCELLENT:", "'EXCELLENT:")
content = content.replace("'✓ GOOD:", "'GOOD:")
content = content.replace("'⚠ MODERATE:", "'MODERATE:")
content = content.replace("'✗ LOW:", "'LOW:")

with open('algae_web_app.py', 'w') as f:
    f.write(content)

print("✓ Emojis removed from recommendations!")
