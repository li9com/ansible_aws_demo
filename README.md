# ansible_aws_demo

A set of playbooks to demo Ansible for AWS. The demo app uses *AWS Lambda* and *DynamoDB*.

This demo utilizes Ansible to deploy from zero to all-run state an application in AWS.


## Structure

There are two important directories on top:
 * `infra` - includes ansible playbooks and configuration for deployment of infra
 * `demoapp` - includes source code and playbooks to deploy the frontend and the backend of the demo application.


## Provisioning of Infrastructure

This process is split up into three task books. Each of them configures a small part of the infrastructure. These books are located in the `infra` directory.

- `tasks_install-network.yml` - configures VPC, network, subnet, security group
- `tasks_install-ec2.yml` - deploys EC2 instances
- `tasks_install-elb.yml` - configures a load balancer

The provisioning is done in the above order. Uninstallation is done in the reverse order.


### Commands to run (staying at the top, root directory)

- **Network**

  ```shell
  # Installation
  ansible-playbook install_infra.yml -e tasks_file=tasks_install-network.yml --ask-vault-pass
  # Uninstallation
  ansible-playbook install_infra.yml -e tasks_file=tasks_uninstall-network.yml --ask-vault-pass
  ```

- **EC2 instances**

  ```shell
  # Installation
  ansible-playbook install_infra.yml -e tasks_file=tasks_install-ec2.yml --ask-vault-pass
  # Uninstallation
  ansible-playbook install_infra.yml -e tasks_file=tasks_uninstall-ec2.yml --ask-vault-pass
  ```

- **Load Balancer**

  ```shell
  # Installation
  ansible-playbook install_infra.yml -e tasks_file=tasks_install-elb.yml --ask-vault-pass
  # Uninstallation
  ansible-playbook install_infra.yml -e tasks_file=tasks_uninstall-elb.yml --ask-vault-pass
  ```

Here I use option `--ask-vault-pass` because the file `group_vars/all/aws-secrets.yml` includes the AWS secret and access keys. You may put these in the environment variables and don't use the options at all. For this also make sure you have commented in the **environment** section in `install_infra.yml` playbook.


## Provisioning of Backend

To deploy the Backend run this playbook

```shell
ansible-playbook install_backend.yml -t install --ask-vault-pass
```

We use here the tag *-t install* to specify to only install the Backend. When we need to uninstall the Backend we run the same playbook, but now we provide tag *-t uninstall*. These two tags should not be used at the same time.

```shell
ansible-playbook install_backend.yml -t uninstall --ask-vault-pass
```



## Provisioning of Frontend

To deploy the Frontend run this playbook

```shell
ansible-playbook install_frontend.yml -t install --ask-vault-pass
```

We use here the tag *-t install* to specify to only install the Frontend. When we need to uninstall the Frontend we run the same playbook, but now we provide tag *-t uninstall*. These two tags should not be used at the same time.

```shell
ansible-playbook install_frontend.yml -t uninstall --ask-vault-pass
```

## Authors

- Dmitrii Mostovshchikov @ Li9, Inc., Dmitrii.Mostovshchikov@li9.com.

