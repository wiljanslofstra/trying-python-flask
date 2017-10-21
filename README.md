# Python test

Just wanted to try some Python. This test blog uses:
- Flask
- SQLAlchemy with a MySQL client

## Development

```
# Build image
docker-compose build

# Run container (change port 5000 to whatever you want to see the app on)
docker-compose up

# And it's live at:
localhost:5000

# Database
localhost:6603

# Migrations
docker exec -it <container_id>
flask db migrate
flask db upgrade
```
