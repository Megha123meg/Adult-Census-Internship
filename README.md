# Adult-Census-Internship

### Software and tools requirements

1. [GithubAccount](https://github.com)
2. [VSCodeIDE](https://code.visualstudio.com/)
3. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

Create a new environment

...

conda create -p venv python==3.7 -y

...

WebApp Link: http://ec2-18-144-170-92.us-west-1.compute.amazonaws.com:8080/

ppk file : https://github.com/Megha123meg/Adult-Census-Internship/blob/main/test.ppk

Steps to run WebApp:
step 1: Open putty
step 2: in hostname give "ec2-18-144-170-92.us-west-1.compute.amazonaws.com"
step 3: In the left corner go to SSH ->Auth->Credentials in the "Private Key file for authentication" browse and select the "ppk file" you downloaded above.
step 4: click open
step 5: A new terminal will open
step 6: login as: ubuntu
step 7: ubuntu@ip-172-31-14-35:~$ python3 app.py
step 8: Open a web browser
step 9: give the url: ec2-18-144-170-92.us-west-1.compute.amazonaws.com:8080
step 10: Give the values in the respective fields
step 11: Click on Predict button.
