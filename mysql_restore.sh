backup_file="cats_db-2024-04-02-21.24.01.sql"
user="cats"
password="cats1234"

sudo docker cp /tmp/$backup_file mysql-server:/tmp/
echo "user : $user"
sudo docker exec mysql-server mysqldump -u $user -p$password cats_db < /tmp/$backup_file
sudo docker exec mysql-server mysql -u $user -p$password cats_db -e "source /tmp/$backup_file"
