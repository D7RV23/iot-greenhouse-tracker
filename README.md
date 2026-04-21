# iot-greenhouse-tracker
Group Project for CS/ECE 459 Internet of Things

### Setup SQL server
Verify that you have the following directory structure:
```
SQL_setup/
├── backups/
├── init/
│   └── schema.sql
├── postgres_data/
├── .env
├── db_connect_select.py
├── docker-compose.yml
└── Dockerfile
```
Build the docker environment
```
docker compose up
```
### Backup DHT11 Data
Run this script
```
docker exec greenhouse_db pg_dump -U postgres postgres > ./backups/backup_$(date +%F).sql
```





