# aws-scraper


## ansible run

1. `git clone git@gitlab.com:alexzerd-personal/aws-scraper.git`
2. `cd aws-scraper/ansible-playbook`
3. ansible will be using your default ~/.id_rsa key when trying to connect to remote server. Make sure that your ~/.id_rsa.pub is copied using `ssh-copy-id devops@172.105.247.205`
4. `ansible-playbook -i inventory provision.yml`
5. Go to `devops-task-b4cf9.forcandidate.com`. Beware that you'll need to `Accept the risk and continue`

## standalone run

1. `docker pull alexzerd/aws-scraper`
2. `docker run -d -p 5000:5000 alexzerd/aws-scraper`
3. Go to `http://localhost:5000`

### NB

1. `root` password stayed the same

***
