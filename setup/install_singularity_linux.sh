#!/bin/bash


# ----- Configuration ---------------------------------------------------------------

# adjust this as necessary
GO_VERSION="1.16.4"
SINGULARITY_VERSION="3.8.1"
OS="linux"
ARCH="amd64"


# ----- functions definitions -------------------------------------------------------

dependeciesInstallation(){

  echo "Installation of system dependecies"

  sudo apt-get update && sudo apt-get install -y \
      build-essential \
      libssl-dev \
      uuid-dev \
      libgpgme11-dev \
      squashfs-tools \
      libseccomp-dev \
      wget \
      pkg-config \
      git \
      cryptsetup \
      qt5-qmake \
      qtbase5-dev \
      qtbase5-dev-tools \
      libqt5gui5 \
      libqt5widgets5 \
      python3-pip \
      python3 \
      python3-pyqt5 \
      xterm \
      qtwayland5 \
      xfonts-base 
}

installPythonDependencies() {
    echo "fallback for cases where the apt package isn't available"

    if command -v pip >/dev/null 2>&1; then
        pip install PyQt5
    else
        python3 -m pip install PyQt5
    fi
}

goInstallation(){

  echo "Installation of Go"
    # Downloads the required Go package
    wget https://dl.google.com/go/go${GO_VERSION}.${OS}-${ARCH}.tar.gz && \
    # Extracts the archive
    sudo tar -C /usr/local -xzvf go${GO_VERSION}.${OS}-${ARCH}.tar.gz && \
    # Deletes the ``tar`` file  
    rm go${GO_VERSION}.${OS}-${ARCH}.tar.gz  


  # add Go to PATH in .bashrc (only if not already there)
  if ! grep -q '/usr/local/go/bin' ~/.bashrc; then
    echo 'export PATH=/usr/local/go/bin:$PATH' >> ~/.bashrc
  fi

  export PATH=/usr/local/go/bin:$PATH 
}

singularityInstall(){

  echo "Installation of Singularity via apt"
  sudo apt-get install -y singularity-container
}

# ----- end functions definitions ---------------------------------------------------

# ----- script steps ----------------------------------------------------------------

echo "Installation of singularity started."

dependeciesInstallation

# installPythonDependencies

while [[ true ]] 
do
    read -p "Do you need to install Go (programmation laguange) ?[y/n]" go
    
    if [ "$go" == "yes" -o "$go" == "y" ];
        then
            break
    elif [ "$go" == "no"  -o "$go" == "n" ];
        then
            break
    else
        echo "I didn't get your answer, please re-try..."
    fi
done

if [ "$go" == "yes" -o "$go" == "y" ];
  then
    goInstallation
fi

singularityInstall

echo "Installation of singularity completed"

# ----- end script steps ------------------------------------------------------------
