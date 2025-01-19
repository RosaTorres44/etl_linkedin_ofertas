# etl_linkedin_ofertas
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt  --break-system-packages

echo "venv/
.env" > .gitignore

pip freeze


echo "DB_HOST="127.0.0.1"
DB_USER="root"
DB_PASSWORD=""
DB_NAME="data3g"
DB_PORT=3306 # Para MySQL o 5432 para PostgreSQL
"> .env 