from flask import Flask, render_template_string

app = Flask(__name__)

# Landing page HTML template
landing_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landing Page</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        header {
            background: linear-gradient(45deg, #4CAF50, #8BC34A);
            color: white;
            padding: 50px 20px;
            text-align: center;
        }
        header h1 {
            font-size: 3em;
            margin: 0;
        }
        header p {
            font-size: 1.2em;
            margin-top: 10px;
        }
        section {
            padding: 50px 20px;
            max-width: 1000px;
            margin: 0 auto;
        }
        .features {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: center;
            margin-top: 30px;
        }
        .feature {
            background: #f4f4f9;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            width: 300px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .feature h3 {
            color: #4CAF50;
        }
        footer {
            background: #333;
            color: white;
            text-align: center;
            padding: 20px;
            margin-top: 50px;
        }
        .cta {
            background: #4CAF50;
            color: white;
            text-align: center;
            padding: 50px 20px;
            border-radius: 8px;
            margin-top: 30px;
        }
        .cta a {
            color: white;
            text-decoration: none;
            background: #333;
            padding: 10px 20px;
            border-radius: 5px;
            transition: background 0.3s;
        }
        .cta a:hover {
            background: #555;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to Our Landing Page</h1>
        <p>Your journey to success begins here.</p>
    </header>
    <section>
        <h2>Our Features</h2>
        <div class="features">
            <div class="feature">
                <h3>Fast Performance</h3>
                <p>Experience blazing-fast speeds and performance optimized for all devices.</p>
            </div>
            <div class="feature">
                <h3>Customizable</h3>
                <p>Tailor the experience to meet your unique needs and preferences.</p>
            </div>
            <div class="feature">
                <h3>Secure</h3>
                <p>Your data and privacy are protected with top-notch security measures.</p>
            </div>
        </div>
        <div class="cta">
            <h2>Ready to get started?</h2>
            <p>Join thousands of users who have transformed their lives with our platform.</p>
            <a href="#">Sign Up Now</a>
        </div>
    </section>
    <footer>
        <p>&copy; 2024 Your Company. All rights reserved.</p>
    </footer>
</body>
</html>
"""

@app.route("/")
def landing():
    return render_template_string(landing_page)

if __name__ == "__main__":
    app.run(debug=True)
