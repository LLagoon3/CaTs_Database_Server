docker exec mysql-server mysqldump -u cats -pcats1234 cats_db > /tmp/cats_db-$(date +%Y-%m-%d-%H.%M.%S).sql
