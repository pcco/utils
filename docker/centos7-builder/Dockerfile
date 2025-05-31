FROM centos:centos7

# Remove any existing repo definitions
RUN rm -f /etc/yum.repos.d/*.repo

# Configure vault.centos.org as the repo source
RUN tee /etc/yum.repos.d/CentOS-Vault.repo > /dev/null <<'EOF'
[base]
name=CentOS-7 - Base
baseurl=https://vault.centos.org/7.9.2009/os/$basearch/
gpgcheck=1
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

[updates]
name=CentOS-7 - Updates
baseurl=https://vault.centos.org/7.9.2009/updates/$basearch/
gpgcheck=1
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

[extras]
name=CentOS-7 - Extras
baseurl=https://vault.centos.org/7.9.2009/extras/$basearch/
gpgcheck=1
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
EOF

# Download the GPG key
RUN curl -o /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 \
    https://vault.centos.org/7.9.2009/os/x86_64/RPM-GPG-KEY-CentOS-7

# Clean and make yum cache
RUN yum clean all && yum makecache

# Install Development Tools group
RUN yum groupinstall -y "Development Tools" && \
    yum install -y curl wget vim epel-release

CMD ["/bin/bash"]

