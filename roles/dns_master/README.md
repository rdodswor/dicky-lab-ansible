# DNS Master Role

## Description
Configures BIND9 as primary DNS server for dicky.lab with Dynamic DNS support.

## Configuration
- Primary: titus (192.168.100.10)
- Secondary: claudia (192.168.100.11)
- TSIG Key: dicky-lab-key
- Zone Location: /var/lib/bind/zones/

## Usage
```bash
ansible-playbook playbooks/dns.yml --limit titus
```
