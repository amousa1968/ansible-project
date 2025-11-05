#!/usr/bin/python3

from ansible.module_utils.basic import AnsibleModule
import os
import shutil

def create_project_structure(base_path, project_name):
    project_path = os.path.join(base_path, project_name)
    os.makedirs(project_path, exist_ok=True)

    # Create subdirectories
    subdirs = ['inventory', 'roles', 'playbooks', 'library', 'vars', 'templates']
    for subdir in subdirs:
        os.makedirs(os.path.join(project_path, subdir), exist_ok=True)

    # Create basic files
    files = {
        'ansible.cfg': """[defaults]
inventory = inventory/
roles_path = roles/
host_key_checking = False

[privilege_escalation]
become = true
become_method = sudo
become_user = root
""",
        'site.yml': """---
- name: Main playbook
  hosts: all
  gather_facts: true
  roles:
    - common
""",
        'inventory/hosts': """[all]
localhost ansible_connection=local
""",
        'roles/common/tasks/main.yml': """---
- name: Ensure common packages are installed
  package:
    name: "{{ item }}"
    state: present
  loop:
    - vim
    - curl
""",
    }

    for file_path, content in files.items():
        full_path = os.path.join(project_path, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as f:
            f.write(content)

    return project_path

def main():
    module = AnsibleModule(
        argument_spec=dict(
            base_path=dict(type='str', required=True),
            project_name=dict(type='str', required=True),
        ),
        supports_check_mode=True
    )

    base_path = module.params['base_path']
    project_name = module.params['project_name']

    if module.check_mode:
        module.exit_json(changed=True, msg=f"Would create project {project_name} in {base_path}")

    try:
        project_path = create_project_structure(base_path, project_name)
        module.exit_json(changed=True, project_path=project_path, msg=f"Project {project_name} created successfully")
    except Exception as e:
        module.fail_json(msg=f"Failed to create project: {str(e)}")

if __name__ == '__main__':
    main()
