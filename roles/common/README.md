# Common Role

## Description
Provides baseline configuration for all hosts in Dicky Lab, including:
- Timezone configuration
- NTP time synchronization using chrony
- Common package installation
- System baseline setup

## Requirements
- Ubuntu 20.04 or later
- Ansible 2.9 or later

## Role Variables

### Timezone
- `timezone`: System timezone (default: `Australia/Adelaide`)

### NTP Configuration
- `ntp_enabled`: Enable NTP synchronization (default: `true`)
- `ntp_service`: NTP service to use (default: `chrony`)
- `ntp_servers`: List of NTP servers (default: Australian pool servers)
- `ntp_fallback_servers`: Fallback NTP servers
- `ntp_allow_networks`: Networks allowed to query this host as NTP server

### Packages
- `common_packages`: List of packages to install
- `unwanted_packages`: List of packages to remove

### Automatic Updates
- `unattended_upgrades_enabled`: Enable automatic security updates (default: `true`)
- `unattended_upgrades_auto_reboot`: Automatically reboot if required (default: `false`)
- `unattended_upgrades_auto_reboot_time`: Time to reboot if needed (default: `"02:00"`)
- `unattended_upgrades_email`: Email address for notifications (default: `""`)
- `unattended_upgrades_origins`: List of apt origins to auto-update (default: security only)

## Dependencies
None

## Example Playbook
```yaml
---
- name: Apply common configuration
  hosts: all
  become: yes
  roles:
    - common
```

## Tags
- `common`: All common tasks
- `timezone`: Timezone configuration only
- `packages`: Package management only
- `ntp`: NTP configuration only
- `chrony`: Chrony-specific tasks

## Example Usage
```bash
# Apply entire common role to all hosts
ansible-playbook playbooks/common.yml

# Only configure NTP
ansible-playbook playbooks/common.yml --tags ntp

# Only install packages
ansible-playbook playbooks/common.yml --tags packages

# Check chrony sources (verbose mode)
ansible-playbook playbooks/common.yml --tags chrony,never -v
```

## Testing
```bash
# Check mode (dry run)
ansible-playbook playbooks/common.yml --check

# Verify chrony is running
ansible all -m service -a "name=chrony state=started" -b

# Check time sync status
ansible all -m command -a "chronyc tracking" -b

# View NTP sources
ansible all -m command -a "chronyc sources" -b
```

## Author
Richard Dodsworth - Dicky Lab

## License
MIT
