# Service-Exchange and Billing Platform

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

A SaaS product for P2P service exchange and billing using Stripe payments.

## 🔧 Tech Stack Used:

- ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
- ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
- ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
- ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
- ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
- ![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
- ![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4)
- ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

## Setup

This project is built using [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django).

Run:

```
docker compose up
```


Your application will start on `localhost:8000`.

## Deployment

### Requirements:

- AWS account
- AWS instance with minimum 2 GiB memory
- A custom domain name

### Steps:

1. Launch the instance
2. Configure the hosted zones from Route 53
3. Configure the inbound rules (port 8000)

### Installing Dependencies:

1. Login to the server as the root user
2. Follow the instructions step by step from [here](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)
3. Run:
```
sudo apt install docker-ce docker-compose git
```
4. Add your deploy keys from GitHub to the server
5. Follow the instructions from [GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
6. Clone the GitHub repository to the server using SSH
7. Create a new directory named `.production`
8. Run:
```
vim /root/Billing-System/.envs/.production/.django
```
   From your local codebase, copy all the content of the file `/.envs/.production/.django` and paste it in the newly created file using vim.
   
9.  Run:
```
vim /root/Billing-System/.envs/.production/.postgres
```
   From your local codebase, copy all the content of the file `/.envs/.production/.postgres` and paste it in the newly created file using vim.
    

10. Run:
```
cd /root/Billing-System && docker-compose -f production.yml down && git pull && docker-compose -f production.yml build && docker-compose -f production.yml run --rm django python manage.py migrate && docker-compose -f production.yml up -d
```


You can now visit your application on the configured domain name.

If the response on the terminal looks like the provided screenshot, then the resources provisioned to the instance are not enough, and you will need to upgrade the memory size to at least 2 GiB (works fine).

