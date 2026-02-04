# DHCP Master Role

## Description
Configures ISC DHCP Server with failover and Dynamic DNS integration.

## Configuration
- Primary: titus (192.168.100.10)
- Secondary: claudia (192.168.100.11)
- Pool: 192.168.100.100-199
- DDNS: Enabled with dicky-lab-key

## Dependencies
- common role
- dns_master role (for DDNS key)

## Usage
```bash
ansible-playbook playbooks/dhcp.yml --limit titus
```

## Author
Richard Dodsworth - Dicky Lab
