from django.http import HttpResponse
from django.shortcuts import render
import os
import time
import subprocess

def htop(request):
    # Get system username
    username = os.getenv('USER')

    # Get current time in IST
    ist_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time() + 5 * 3600 + 30 * 60))

    # Get the output of the 'top' command
    top_output = subprocess.check_output(['top', '-bn1']).decode('utf-8')

    # Prepare the HTML response
    html_response = f"""
    <html>
        <body>
            <h1>System Info</h1>
            <p><strong>Name:</strong> Your Full Name</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {ist_time}</p>
            <pre>{top_output}</pre>
        </body>
    </html>
    """
    return HttpResponse(html_response)
