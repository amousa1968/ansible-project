# Ansible Project for Application Restart

This Ansible project provides automated solutions for restarting WebSphere Application Server and other services across Linux and Windows environments in dev, staging, and production environments using Ansible Tower/AWX.

## Project Structure

```
├── playbooks/
│   ├── restart_websphere.yml          # Main WebSphere restart playbook
│   ├── restart_linux_service.yml      # Generic Linux service restart
│   ├── restart_windows_service.yml    # Generic Windows service restart
│   ├── ibm-http-server-install.yml    # Install IBM HTTP Server
│   ├── ibm-http-server-install-dev.yml    # Install IBM HTTP Server (Dev)
│   ├── ibm-http-server-install-staging.yml # Install IBM HTTP Server (Staging)
│   ├── ibm-http-server-install-prod.yml    # Install IBM HTTP Server (Prod)
│   ├── ibm-http-server-start.yml       # Start IBM HTTP Server
│   ├── ibm-http-server-stop.yml        # Stop IBM HTTP Server
│   └── ibm-http-server-restart.yml     # Restart IBM HTTP Server
├── roles/
│   ├── was_restart/                   # WebSphere Application Server restart role
│   │   ├── tasks/
│   │   │   └── main.yml
│   │   └── vars/
│   │       └── main.yml
│   ├── linux_service/                 # Generic Linux service management
│   │   ├── tasks/
│   │   │   └── main.yml
│   │   └── defaults/
│   │       └── main.yml
│   ├── windows_service/               # Generic Windows service management
│   │   ├── tasks/
│   │   │   └── main.yml
│   │   └── defaults/
│   │       └── main.yml
│   ├── ibm_http_install/              # IBM HTTP Server install role
│   ├── ibm_http_start/                # IBM HTTP Server start role
│   ├── ibm_http_stop/                 # IBM HTTP Server stop role
│   └── ibm_http_restart/              # IBM HTTP Server restart role
├── environments/
│   ├── dev/
│   │   └── hosts.ini
│   ├── staging/
│   │   └── hosts.ini
│   └── prod/
│       └── hosts.ini
└── ansible.cfg
```

## Environments

The project supports three environments:

- **dev**: Development environment with test servers
- **staging**: Staging/UAT environment
- **prod**: Production environment

Each environment inventory (`environments/{env}/hosts.ini`) contains:
- `websphere_servers`: Hosts running WebSphere Application Server
- `linux_servers`: Linux hosts for generic service management
- `windows_servers`: Windows hosts for generic service management
- `ibm_http_servers`: Hosts running IBM HTTP Server

## Playbooks

### WebSphere Application Server
- `restart_websphere.yml`: Restarts WebSphere Application Server across all environments

### Generic Service Management
- `restart_linux_service.yml`: Generic playbook for restarting services on Linux servers
- `restart_windows_service.yml`: Generic playbook for restarting services on Windows servers

### IBM HTTP Server Management
- `ibm-http-server-install.yml`: Install IBM HTTP Server
- `ibm-http-server-install-dev.yml`: Install IBM HTTP Server in development
- `ibm-http-server-install-staging.yml`: Install IBM HTTP Server in staging
- `ibm-http-server-install-prod.yml`: Install IBM HTTP Server in production
- `ibm-http-server-start.yml`: Start IBM HTTP Server
- `ibm-http-server-stop.yml`: Stop IBM HTTP Server
- `ibm-http-server-restart.yml`: Restart IBM HTTP Server

## Roles

### was_restart
- **Purpose**: Restart WebSphere Application Server
- **OS Support**: Linux and Windows
- **Variables**:
  - `was_service_name`: Service name (default: websphere)
  - `was_restart_timeout`: Timeout for restart operations (default: 30)

### linux_service
- **Purpose**: Generic Linux service management
- **Variables**:
  - `service_name`: Name of the service to restart (default: websphere)

### windows_service
- **Purpose**: Generic Windows service management
- **Variables**:
  - `service_name`: Name of the service to restart (default: websphere)

### IBM HTTP Server Roles
- `ibm_http_install`: Install IBM HTTP Server on Linux/Windows
- `ibm_http_start`: Start IBM HTTP Server service
- `ibm_http_stop`: Stop IBM HTTP Server service
- `ibm_http_restart`: Restart IBM HTTP Server service

**Common Variables for IBM HTTP Server roles**:
- `ibm_http_service_name`: Service name (default: ibm-http-adminctl)
- `ibm_http_port`: HTTP port (default: 80)
- `ibm_http_timeout`: Timeout for operations (default: 30)

## Usage with Ansible Tower

1. **Import Project**: Import this project into Ansible Tower/AWX
2. **Configure Inventories**: Create inventories in Tower corresponding to the environment directories
3. **Create Job Templates**:
   - Template for WebSphere restart using `restart_websphere.yml`
   - Template for Linux service restart using `restart_linux_service.yml`
   - Template for Windows service restart using `restart_windows_service.yml`
   - Templates for IBM HTTP Server operations using respective playbooks
4. **Set Variables**: Override default variables as needed for specific environments
5. **Schedule/Execute**: Run manually or schedule automated restarts

## Prerequisites

- Ansible 2.9+
- SSH access to target servers
- sudo privileges on Linux servers
- WinRM access on Windows servers
- SSH keys configured for passwordless authentication

## Configuration

The `ansible.cfg` file contains:
- Inventory path pointing to `environments/`
- Roles path pointing to `roles/`
- Privilege escalation settings
- SSH key configuration

## Security Notes

- SSH keys are used for authentication
- Privilege escalation is enabled for service management
- Host key checking is disabled for automation convenience

## Customization

To customize for different services:
1. Update `service_name` variable in role defaults
2. Modify task files in roles for specific service requirements
3. Add new roles for additional service types
4. Update inventory files with appropriate host groups
