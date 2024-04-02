backup_file="cats_db-2024-04-02-21.24.01.sql"
user="cats"
password="cats1234"

sudo docker cp /tmp/mysql/$backup_file mysql-server:/tmp/mysql/
echo "user : $user"
sudo docker exec mysql-server mysqldump -u $user -p$password cats_db < /tmp/mysql/$backup_file
sudo docker exec mysql-server mysql -u $user -p$password cats_db -e "source /tmp/mysql/$backup_file"
