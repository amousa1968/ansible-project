# Ansible Project for Application Restart

This Ansible project provides automated solutions for restarting WebSphere Application Server and other services across Linux and Windows environments in dev, staging, and production environments using Ansible Tower/AWX.

## Project Structure

```
├── playbooks/
│   ├── restart_websphere.yml          # Main WebSphere restart playbook
│   ├── restart_linux_service.yml      # Generic Linux service restart
│   └── restart_windows_service.yml    # Generic Windows service restart
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
│   └── windows_service/               # Generic Windows service management
│       ├── tasks/
│       │   └── main.yml
│       └── defaults/
│           └── main.yml
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

## Playbooks

### restart_websphere.yml
Restarts WebSphere Application Server across all environments. Uses the `was_restart` role which automatically detects the operating system and applies appropriate restart procedures.

### restart_linux_service.yml
Generic playbook for restarting services on Linux servers using the `linux_service` role.

### restart_windows_service.yml
Generic playbook for restarting services on Windows servers using the `windows_service` role.

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

## Usage with Ansible Tower

1. **Import Project**: Import this project into Ansible Tower/AWX
2. **Configure Inventories**: Create inventories in Tower corresponding to the environment directories
3. **Create Job Templates**:
   - Template for WebSphere restart using `restart_websphere.yml`
   - Template for Linux service restart using `restart_linux_service.yml`
   - Template for Windows service restart using `restart_windows_service.yml`
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
