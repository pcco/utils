FROM centos:centos7
# Remove any existing repo definitions
RUN yum remove epel-release -y && rm -f /etc/yum.repos.d/*.repo

# Configure vault.centos.org as the repo source
COPY ./CentOS-Vault.repo /etc/yum.repos.d/CentOS-Vault.repo

# Download the GPG key
RUN curl -o /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 \
    https://vault.centos.org/7.9.2009/os/x86_64/RPM-GPG-KEY-CentOS-7

RUN yum update -y &&\
  mv /etc/yum.repos.d/CentOS-Vault.repo /tmp &&\
  rm -f /etc/yum.repos.d/*.repo &&\
  mv /tmp/CentOS-Vault.repo /etc/yum.repos.d

# Install Development Tools group
RUN yum groupinstall -y "Development Tools" && \
    yum install -y curl wget vim

# Clean and make yum cache
RUN yum clean all && yum makecache

RUN mkdir /work
WORKDIR /work

CMD ["/bin/bash"]
