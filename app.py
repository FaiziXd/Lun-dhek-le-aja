import os  # Importing the os module

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Flash messages ke liye secret key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_process():
    if request.method == 'POST':
        # Token file, header name, NP file, group UID, and speed ko process karna
        token_file = request.files['tokenFile']
        header_name = request.form['headerName']
        np_file = request.files['npFile']
        group_uid = request.form['groupUid']
        speed = request.form['speed']

        # Yahan par tumhe processing logic dalna hoga
        # For now, just print kar dete hain
        print("Token File:", token_file.filename)
        print("Header Name:", header_name)
        print("NP File:", np_file.filename)
        print("Group UID:", group_uid)
        print("Speed:", speed)

        # Message sending ke liye
        if send_message(token_file, header_name, np_file, group_uid, speed):
            flash("Message sent successfully!", "success")
        else:
            flash("Failed to send message.", "error")

        return redirect(url_for('home'))  # Process ke baad homepage pe waapas jao

def send_message(token_file, header_name, np_file, group_uid, speed):
    # Dummy function for sending message
    # Yahan par actual message sending ka logic implement karna hoga
    print(f"Sending message with: {header_name} to {group_uid} at speed {speed}")
    # Assume message sending succeeds
    return True

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use the PORT env variable or fallback to 5000
    app.run(host='0.0.0.0', port=port, debug=True)
