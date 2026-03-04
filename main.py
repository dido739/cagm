from flask import Flask, redirect, render_template, request, send_from_directory
import os
import requests
file_path = 'templates/index.html'
app = Flask(__name__)
@app.route('/')
def root():
    return render_template('index.html')

@app.route('/post')
def create_post():
    return render_template('post.html')

@app.route('/post-data', methods=['POST'])
def post_data():
   data = request.form.get('link')
   data1 = request.form.get('alt_text')
   if not data1:
         data1 = data
   print(data)
   with open(file_path, 'a') as file:
            file.write('<li>' +"<a href='" + data + "' target='_blank'>" + data1 + '</a></li>\n')
   return redirect("/post")

@app.route('/sw.js')
def service_worker():
    return send_from_directory(app.static_folder, 'sw.js',
                               mimetype='application/javascript')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))