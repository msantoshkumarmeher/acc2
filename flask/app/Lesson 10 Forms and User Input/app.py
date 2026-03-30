from flask import Flask, render_template, request  # Added 'request'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])  # Allow both GET and POST
def analyze():
    if request.method == 'POST':
        # This runs when form is submitted
        user_text = request.form['user_input']  # Get data from form
        
        # Simple "AI" analysis (we'll upgrade this later)
        word_count = len(user_text.split())
        char_count = len(user_text)
        
        # Check for keywords (simple sentiment)
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
    
    # If GET request, just show the form
    return render_template('analyze.html')

if __name__ == '__main__':
    app.run(debug=True)