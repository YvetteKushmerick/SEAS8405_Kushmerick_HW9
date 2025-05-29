import subprocess

def start_ldap_server():
    print("Starting OpenLDAP Docker container...")
    subprocess.run([
        "docker", "run", "-d",
        "--name", "openldap",
        "-p", "389:389",
        "-e", "LDAP_ORGANISATION=MyOrg",
        "-e", "LDAP_DOMAIN=example.org",
        "-e", "LDAP_ADMIN_PASSWORD=admin",
        "osixia/openldap:1.5.0"
    ])

if __name__ == "__main__":
    start_ldap_server()