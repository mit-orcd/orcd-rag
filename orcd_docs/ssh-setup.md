---
tags:
 - SSH Key Setup
---

# SSH Key Setup

An SSH key is a secure access credential used in the SSH protocol and establishes a secure and encrypted connection to our HPC systems. This page is for those who wish to implement SSH key authentication on top of general MIT Kerberos authentication.

SSH keys consist of a pair: a public key and a private key. 

- **Public Key**: This key can be shared freely and is used to encrypt data that only the corresponding private key can decrypt.
- **Private Key**: This key must be kept secure and private. It is used to decrypt data encrypted with the corresponding public key and to prove the identity of the user during the SSH authentication process.

When you attempt to connect to an HPC system using SSH key authentication, the system uses your public key to initiate a challenge that can only be answered correctly using your private key. If the correct response is received, the system verifies your identity and grants access. 

Using the key and lock analogy, the private key is like your key, and the public key is like a lock you might place on a gym locker, which would be like your account on an ORCD system. You can leave the lock locked on the locker at the gym, because no one can open the lock without the key, but you wouldn't want to share your key with anyone else, because then they could get into your locker.

!!! danger "Do Not Share Your Private Key" 
    Your private key should never be shared with anyone. If someone else obtains your private key, they could potentially gain unauthorized access to any system your key is associated with.

## Checking for Existing SSH Keys

Before you generate an SSH key, you should check for existing SSH keys.  

1. Open your local terminal.  
2. Run the following command to view all existing SSH keys:  
```bash
ls -al ~/.ssh
```
3. If you see a list of files, you have existing SSH keys.
If you receive an error that ~/.ssh doesn't exist, you do not have an existing SSH key pair in the default location. You can create a new SSH key pair in the next step.

## Generating SSH Keys

If you do not have an existing SSH key, follow these steps. 

1. Open your local Terminal.  
2. Run the following command to generate an RSA key:  
```bash
ssh-keygen -t rsa
```
3. **Save the key pair:** You will be prompted to enter a file path to save the key. Press `Enter` to accept the default location:
```
Enter a file in which to save the key (/home/your_username/.ssh/id_rsa):
```

4. **Passphrase:** 
You will be asked to enter a passphrase for additional security. You can either enter a passphrase or leave it empty and press `Enter`:
```
Enter passphrase (empty for no passphrase):
```
!!! Note 
    On ORCD systems, we recommend setting a passphrase as it provides extra security for your account by helping to prevent someone else from using your SSH keys. When you create a passphrase, your private key can only authenticate into your account when the correct passphrase is provided during login. **Since you set your passphrase on your system, ORCD staff cannot help you remember or reset the passphrase for your SSH keys. You must create new SSH keys if you cannot remember your passphrase.**



## Uploading SSH Key on Our Systems

To upload your SSH key on our systems, you must update the `authorized_keys` file in the respective system via terminal. Alternatively, for the Engaging System, you have the option to use OnDemand, and for SuperCloud, you can fill out an SSH key addition form.

=== "Terminal"
    To add your SSH key via Terminal, please follow the steps outlined below:

    1. Login to an HPC system login-node using MIT Kerberos Login.
    2. On your local machine, copy the contents of your public key (`~/.ssh/id_rsa.pub`):
    ```shell
    cat ~/.ssh/id_rsa.pub
    ```
    > Make sure to copy the entire line starting with ssh-rsa and ending with your email address or comment. 
    3. On the head-node, append the copied contents to the authorized_keys file located at `/home/[username]/.ssh/authorized_keys`. You can use any text editor of your choice, such as nano and vim. For example, if you're using `nano`, the command would be:
    ```shell
    nano /home/[username]/.ssh/authorized_keys
    ```
    !!! Note
        **Do not remove anything already present in the authorized_keys file. Be careful to append your key to the end of the file rather than replacing its contents.**

=== "Engaging OnDemand"
    To add your SSH key to Engaging via OnDemand, please follow the steps outlined below:

    1. Login to Engaging OnDemand through the [portal](https://engaging-ood.mit.edu/).
    2. Once logged in, navigate to `Files` and `Home Directory`.
    3. On the top right corner, check `Show Dotfiles`.
    ![Dotfiles Option](../images/ssh-setup/dotfiles.png)
    4. Click on the `.ssh` folder.
    ![.ssh File Location](../images/ssh-setup/ssh_location.png)
    5. Locate and edit the `authorized_keys` file to add your new key.
    ![authorized_keys Image](../images/ssh-setup/authorized_keys.png)

    !!! Note
        **Do not remove anything already present in the authorized_keys file. Be careful to append your key to the end of the file rather than replacing its contents.**

=== "SuperCloud"
    To add your SSH key to SuperCloud, please follow the steps outlined below:

    1.  Navigate to the [SuperCloud SSH Key Addition Form](https://supercloud.mit.edu/requesting-account#adding-keys) and follow the instructions to add your SSH key. 
    2. If you encounter any problems during the SSH key submission process, refer to the [SSH Troubleshooting Checklist](https://mit-supercloud.github.io/supercloud-docs/ssh-troubleshooting-checklist/) for guidance. 

## Testing your SSH Key Setup

To ensure that your SSH key is correctly configured, follow these steps:

1. Attempt to login on your terminal: `ssh your_username@cluster_address`. For more details, you can reference the [Getting Started Tutorial](../getting-started.md) page.
2. If prompted for a password, the SSH key setup did not work. Recheck the steps and correct any issues.

## Troubleshooting SSH Key Issues
If you encounter SSH key issues, you can reference the [SSH Troubleshooting Checklist](https://mit-supercloud.github.io/supercloud-docs/ssh-troubleshooting-checklist/). While this guide is for SuperCloud, it should be helpful for other systems as well. If you are still having problems, please email us at <orcd-help@mit.edu> and visit the [Getting Help](../getting-help.md) page. In your help email, please include the output of the following command:
```sh
ssh -vvv USERNAME@cluster_address
``` 

