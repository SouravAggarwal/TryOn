# Migration Commands
1. python manage.py makemigrations
2. python manage.py migrate


# Runserver commands
1. python manage.py runserver 0.0.0.0:8000

# Admin
1. python manage.py createsuperuser  
2. user: souravaggarwal
3. pass: 121212

# Setup EC2 server
1. Inbound and Outbound Security rules
   1. SSH, HTTP, HTTPS with Anywhere IP4 and 6
   2. Custom TCP 8000 with Anywhere IP4 and 6
   
# Connect EC2 with local terminal
1. chmod 400 "tryon-backend-core-ec2-ssh-keypair.pem"
2. ssh -i "creds/tryon-backend-core-ec2-ssh-keypair.pem" ec2-user@ec2-44-202-33-3.compute-1.amazonaws.com
   
# Add EC2 ssh on Github
1. ssh-keygen -t rsa -b 4096 -C "srvaggarwal96@gmail.com"
2. cat ~/.ssh/id_rsa.pub
3. ssh -T git@github.com     (To verify)
   
# EC2 Setup and Python installation
1. sudo yum update && sudo yum upgrade -y
2. sudo yum install nginx -y
3. sudo yum install python3.11 -y
4. sudo yum groupinstall "Development Tools" -y  && sudo yum install gcc gcc-c++ make -y
5. curl -O https://bootstrap.pypa.io/get-pip.py && python3.11 get-pip.py
#5. sudo apt install python3-pip python3-venv
1. python3 -m venv venv
2. source venv/bin/activate

# Git clone
1. git clone git@github.com:SouravAggarwal/TryOn.git
2. cd TryOn/Backend/
3. git checkout main && git pull origin main
4. pip install -r tryon_backend/requirements.txt
5. python manage.py runserver 0.0.0.0:8000



            sudo systemctl restart gunicorn
            sudo systemctl restart nginx
