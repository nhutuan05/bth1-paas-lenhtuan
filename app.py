from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Thực hành PaaS - Render</title>
    </head>
    <body style="text-align:center; font-family:Arial; padding:50px">
        <h1>THỰC HÀNH ĐIỆN TOÁN ĐÁM MÂY</h1>
        <h2>Mô hình PaaS - Render</h2>
        <p>Triển khai ứng dụng Python Flask trên Render.</p>
        <h3 style="color:green">Ứng dụng hoạt động thành công!</h3>
        <a href="/health">Kiểm tra dịch vụ</a>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "platform": "Render",
        "model": "PaaS"
    })
