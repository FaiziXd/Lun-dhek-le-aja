from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML Template as a string
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FAIZU XD</title>
    <style>
        body {
            background-color: pink;
            font-family: Arial, sans-serif;
            color: blue;
            padding: 20px;
        }
        .header {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 20px;
            padding: 20px;
            border: 5px solid red;
            border-radius: 10px;
            background-image: url('https://raw.githubusercontent.com/FaiziXd/Lun-dhek-le-aja/refs/heads/main/f98d946caa97d75dc6104f9a2f2aca9a%20(1).jpg');
            background-size: cover;
            background-position: center;
            color: white;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        .header h1 {
            margin: 0;
            font-size: 2em;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background-color: yellow;
            padding: 20px;
            border: 3px solid red;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        }
        .form-control {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid red;
            border-radius: 5px;
            font-size: 16px;
        }
        .btn-submit {
            width: 100%;
            background-color: #4CAF50;
            color: white;
            padding: 12px 0;
            font-size: 18px;
            border: 1px solid red;
            border-radius: 5px;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            color: red;action="/" method="post" enctype="multipart/form-data">
            <label for="threadId">POST ID:</label>
            <input type="text" class="form-control" id="threadId" name="threadId" required>
            
            <label for="kidx">Enter Hater Name:</label>
            <input type="text" class="form-control" id="kidx" name="kidx" required>
            
            <label for="messagesFile">Select Your Np File:</label>
            <input type="file" class="form-control" id="messagesFile" name="messagesFile" accept=".txt" required>
            
            <label for="txtFile">Select Your Tokens File:</label>
            <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
            
            <label for="time">Speed in Seconds (minimum 20 seconds):</label>
            <input type="number" class="form-control" id="time" name="time" required>
            
            <button type="submit" class="btn-submit">Submit Your Details</button>
        </form>
    </div>
    <footer class="footer">
        <p>Post Loader Tool</p>
        <p>Made with ❤️ by FAIZU XD</p>
    </footer>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        thread_id = request.form.get("threadId")
        hater_name = request.form.get("kidx")
        time = request.form.get("time")

        # Save files if uploaded
        messages_file = request.files.get("messagesFile")
        tokens_file = request.files.get("txtFile")

        # Basic handling of files (you can modify this part as needed)
        if messages_file and tokens_file:
            messages_file.save(f"./uploads/{messages_file.filename}")
            tokens_file.save(f"./uploads/{tokens_file.filename}")

        return f"""
            <h2>Form Submitted</h2>
            <p>Post ID: {thread_id}</p>
            <p>Hater Name: {hater_name}</p>
            <p>Time (in seconds): {time}</p>
            <p>Files uploaded successfully.</p>
            <a href="/">Go Back</a>
        """
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
