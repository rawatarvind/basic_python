# Directory containing .deb packages for Ubuntu/Debian

from packages_installer import main # Import the main function

# # List of packages to install using yum/dnf on CentOS 7

centos_packages = ['vim', 'git','google-chrome', 'skypeforlinux.x86_64', 'zoom.x86_64', 'wps-office.x86_64','glade*' ,'slack.x86_64', 'fusioninventory-agent.x86_64', 'openvpn.x86_64', 'usbguard.x86_64',  'anydesk.x86_64', 'ntfs-3g.x86_64']

# Directory containing .deb packages for Ubuntu/Debian
deb_package_directory = '/home/sarvind/Ubuntu_packages'

# Call the main function to install packages based on the OS
main(centos_packages, deb_package_directory)