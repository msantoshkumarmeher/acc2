from flask import Flask, render_template, request

# ============================================================
# Lesson 10 - Forms and User Input
# File: app.py
# Purpose: Accept user text and return basic sentiment-style analysis
# ============================================================

app = Flask(__name__)

@app.route('/')
def home():
    # Landing page
    return render_template('index.html')

# GET shows form, POST processes submitted text
@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        # Read text input from form field named user_input
        user_text = request.form['user_input']
        
        # Simple "AI" analysis (we'll upgrade this later)
        word_count = len(user_text.split())
        char_count = len(user_text)
        
        # Keyword-based sentiment check (for learning/demo only)
        if 'sad' in user_text.lower() or 'good' in user_text.lower():
            sentiment = "Negative 😊"
        elif 'happy' in user_text.lower() or 'bad' in user_text.lower():
            sentiment = "Positive 😢"
        else:
            sentiment = "Neutral 😐"
        
        # Pass results to template
        return render_template('result.html', 
                             text=user_text,
                             word_count=word_count,
                             char_count=char_count,
                             sentiment=sentiment)
    
    # For GET request, show analysis form page
    return render_template('analyze.html')

if __name__ == '__main__':
    app.run(debug=True)