# Root CA Role

Ansible role for deploying and configuring a Root Certificate Authority using OpenSSL.

## Purpose

Creates a secure, production-grade Root CA following industry best practices:
- 4096-bit RSA keys with passphrase protection
- 20-year certificate validity
- Proper file permissions and directory structure
- Automated backup and verification
- Comprehensive documentation generation

## Requirements

- Ubuntu 24.04 LTS (or compatible Debian-based system)
- Ansible 2.9+
- Root/sudo access
- Ansible Vault for passphrase encryption

## Role Variables

See `defaults/main.yml` for all configurable variables.

### Key Variables

#### Certificate Details
- `ca_common_name`: Common Name for the Root CA certificate
- `ca_organization`: Organization name
- `ca_organizational_unit`: Organizational unit
- `ca_country`: Two-letter country code (default: AU)
- `ca_state`: State or province
- `ca_locality`: City or locality
- `ca_email`: Contact email address

#### Security Settings
- `ca_key_size`: RSA key size in bits (default: 4096)
- `ca_cert_validity_days`: Certificate validity period in days (default: 7300 = 20 years)
- `ca_key_cipher`: Encryption cipher for private key (default: aes256)
- `root_ca_passphrase`: Passphrase for private key (stored in Ansible Vault)

#### File Locations
- `ca_base_dir`: Base directory for CA files (default: /root/ca)
- `ca_backup_dir`: Backup location (default: /var/backups/ca)

#### Features
- `ca_backup_enabled`: Enable automatic backups (default: true)

## Dependencies
```yaml
dependencies:
  - role: common
```

The `common` role must be applied first to ensure base system configuration and package installation.

## Example Playbook
```yaml
---
- name: Setup Root Certificate Authority
  hosts: root_ca
  become: true
  
  roles:
    - role: ca_root
      tags:
        - ca_root
```

## Tags

All tasks are tagged for selective execution:

- `prerequisites`: System preparation (firewall, services)
- `directory_structure`: Create CA directory tree
- `openssl_config`: Deploy OpenSSL configuration
- `generate_ca`: Generate private key and certificate
- `verification`: Verify CA setup
- `backup`: Create encrypted backup

### Example Tag Usage
```bash
# Only verify existing CA
ansible-playbook ca_root.yml --tags verification

# Skip backup during testing
ansible-playbook ca_root.yml --skip-tags backup

# Only install prerequisites
ansible-playbook ca_root.yml --tags prerequisites
```

## Usage

### Initial Deployment
```bash
# Deploy Root CA
ansible-playbook playbooks/ca_root.yml --ask-vault-pass

# Verify deployment
ansible-playbook playbooks/ca_verify.yml --ask-vault-pass
```

### Verification
```bash
# On the CA server
sudo openssl x509 -noout -text -in /root/ca/certs/ca.cert.pem

# Check validity
sudo openssl x509 -noout -dates -in /root/ca/certs/ca.cert.pem

# Verify key-certificate pairing
cd /root/ca
sudo openssl x509 -noout -modulus -in certs/ca.cert.pem | openssl md5
sudo openssl rsa -noout -modulus -in private/ca.key.pem -passin pass:PASSPHRASE | openssl md5
```

### Signing Intermediate CA Certificates

See the generated `/root/ca/README.md` on the CA server for detailed procedures.

## Security Considerations

### Passphrase Management
The Root CA private key passphrase is stored in Ansible Vault. Never commit unencrypted passphrases to version control.

### Offline Storage
After initial setup and signing the intermediate CA certificate, the Root CA should be:
- Powered down
- Stored offline
- Only brought online for signing new intermediate certificates or emergencies

### Backup Strategy
- Automated backups are created during playbook runs
- Store backups in secure, encrypted, offline location
- Test recovery procedures regularly

### Access Control
- Only authorized administrators should have access
- Root CA server should be isolated from production networks
- All access should be logged and audited

## File Structure
```
/root/ca/
├── certs/              # Issued certificates
│   └── ca.cert.pem    # Root CA certificate (public)
├── crl/               # Certificate Revocation Lists
├── csr/               # Certificate Signing Requests (incoming)
├── newcerts/          # Certificate database copies
├── private/           # Private keys (restricted access)
│   └── ca.key.pem    # Root CA private key (encrypted)
├── index.txt          # Certificate database
├── serial             # Next certificate serial number
├── crlnumber          # CRL version number
├── openssl.cnf        # OpenSSL configuration
└── README.md          # Operational documentation
```

## Troubleshooting

### "Permission denied" errors
Ensure you're running with `become: true` and have sudo access.

### "Vault password required"
Always use `--ask-vault-pass` when running playbooks that access encrypted variables.

### Certificate generation fails
Check that the passphrase in Ansible Vault is correct and accessible.

### Idempotency warnings
The role is designed to be idempotent. Running multiple times should not regenerate existing certificates.

## License

MIT

## Author

Richard Dodsworth - Dicky Lab

## References

- [OpenSSL CA Documentation](https://www.openssl.org/docs/manmaster/man1/ca.html)
- [Ansible Best Practices](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
