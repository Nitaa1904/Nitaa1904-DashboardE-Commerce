# Gunakan base image Python
FROM python:3.10

# Set working directory di container
WORKDIR /app

# Salin file lokal ke container
COPY . .

# Install semua dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Expose port Streamlit (default 8501)
EXPOSE 8501

# Jalankan aplikasi
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
