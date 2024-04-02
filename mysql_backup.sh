docker exec mysql-server mysqldump -u cats -pcats1234 cats_db > /tmp/mysql/cats_db-$(date +%Y-%m-%d-%H.%M.%S).sql
