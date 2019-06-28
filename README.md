# ansible_aws_demo

A set of playbooks to demo Ansible for AWS. The demo app uses *AWS Lambda* and *DynamoDB*.

This demo utilizes Ansible to deploy from zero to all-running state an application in AWS.

Main development is doing in the @common-devel branch.


## Structure

There are two directories on top:
 * `demo_1` - includes ansible playbooks and configuration for deployment of infra
 * `demoapp` - includes source code and playbooks to deploy frontend and backend of app.


## Infra

Go to `/demo_1` directory. There is a bunch of task files named as `task_install-*` and `task_uninstall-*`. Every of them does only a small part of the whole job. These task files are not playbooks and cannot be run separately. (See `install.yml` for this).


There is a config file `vars_aws-vpc.yml` which describes the configuration of an infrastrcture for orchestrating.

There is a playbook `install.yml` which should be run to install and uninstall infra, and, also to install and uninstall the demo application.


### Using install.yml playbook

To run this playbook you need to provde `aws_secret_key` and `aws_access_key` environment variables. Or they being searched in the file `~/.aws/credentials`.

The playbook can be run by following ways:

  - install infra:
  `ansible-playbook install.yml -e do=install -e scope=infra`

  - install demo app:
    `ansible-playbook install.yml -e do=install -e scope=app`

  - uninstall infra:
  `ansible-playbook install.yml -e do=uninstall -e scope=infra`

  - uninstall demo app:
    `ansible-playbook install.yml -e do=uninstall -e scope=app`

  - additionally, you can get credentials to access the deployed infrastructure:
    `ansible-playbook install.yml -e do=install -e scope=infra -t summary`


  In case if during process `do=install` an error happens, the playbook automatically runs `do=uninstall` actions.

  **Note:**
  So far the demo app can be deployed without provisioning an infrastructure. Up now it has only **backend** component implemented which works entirely on *AWS Lambda* functions and *AWS DynamoDB*.


### Deployment

There is a two-step process to get all run.

  - deployment of instrastructure
  - intalling the demo application


## Backend

Implemented on *AWS Lambda* functions, persistent data is stored in *AWS DynamoDB*.


## Frontend

So far frontend is not ready yet.

