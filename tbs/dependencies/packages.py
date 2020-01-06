"""
This is a simple config file holding an array of packages for each subtype that exists
"""

# packages required for everything
GENERAL_PACKAGES=["git"]

# packages required to build the repository
REPO_PACKAGES=["python-sphinx", "rust", "pacman-contrib", "i3lock-color-git", "dkms", "xorg-xset", "unzip", "asciidoc", "docbook-xsl", "pythonqt" ]

# packages required to build the kernel
KERNEL_PACKAGES=["asp", "autoconf", "automake", "binutils", "bison", "fakeroot", "file", "findutils", "flex", "gawk", "gcc", "gettext", "grep", "groff", "gzip", "libtool", "m4", "make", "pacman", "patch", "pkgconf", "sed", "sudo", "texinfo", "which"]

# packages required to build the iso
IMAGE_PACKAGES=["archiso"]

# packages required to sync with a server/cloud instance
UPLOAD_PACKAGES=["rsync"]