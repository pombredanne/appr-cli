<<<<<<< HEAD
<<<<<<< HEAD
# CNR Command Line Tool

## Install the Helm Registry Plugin

First, Install the latest [Helm release](https://github.com/kubernetes/helm#install).

If you are an OSX user, quickstart with brew: `brew install kubernetes-helm`

Next download and install the registry plugin for Helm.

### OSX

```
wget https://github.com/cn-app-registry/cnr-cli/releases/download/v0.3.7-dev/registry-cnr-v0.3.7-dev-osx-x64-helm-plugin.tar.gz
mkdir -p ~/.helm/plugins/
tar xzvf registry-cnr-v0.3.7-dev-osx-x64-helm-plugin.tar.gz  -C ~/.helm/plugins/
```

### Linux

```
wget https://github.com/cn-app-registry/cnr-cli/releases/download/v0.3.7-dev/registry-cnr-v0.3.7-dev-linux-x64-helm-plugin.tar.gz
mkdir -p ~/.helm/plugins/
tar xzvf registry-cnr-v0.3.7-dev-linux-x64-helm-plugin.tar.gz  -C ~/.helm/plugins/
```

### Windows

```
wget https://github.com/cn-app-registry/cnr-cli/releases/download/v0.3.7-dev/registry-cnr-v0.3.7-dev-win-x64-helm-plugin.tar.gz
mkdir -p ~/.helm/plugins/
tar xzvf registry-cnr-v0.3.7-dev-linux-x64-helm-plugin.tar.gz  -C ~/.helm/plugins/
```

Note: You must have bash in your path and change the `registry/plugin.yaml` execution to call `bash -c $HELM_PLUGIN_DIR/cnr.sh`


## Deploy Jenkins Using Helm from the Quay Registry


```
helm registry version app.quay.io
```

Output should be:
```
Api-version: {u'cnr-api': u'0.X.Y'}
Client-version: 0.X.Y
```

### Install Jenkins

```
helm init
helm registry list app.quay.io
helm registry install app.quay.io/helm/jenkins
```

## Create and Push Your Own Chart

First, create an account on https://app.quay.io (staging server) and login to the CLI using the username and password

Set an environment for the username created at Quay to use through the rest of these instructions.

```
export USERNAME=philips
```

Login to Quay with the Helm registry plugin:

```
helm registry login -u $USERNAME app.quay.io
```

Create a new Helm chart, the default will create a sample nginx application:

```
helm create nginx
```

Push this new chart to Quay and then deploy it from Quay.

```
cd nginx
helm registry push --namespace $USERNAME app.quay.io
helm registry install app.quay.io/$USERNAME/nginx
```
=======
=======
[![Coverage Status](https://coveralls.io/repos/github/cn-app-registry/cnr-server/badge.svg)](https://coveralls.io/github/cn-app-registry/cnr-server)

>>>>>>> 058761b... Add more api tests
# cnr-server
## Install
1. git clone https://github.com/cn-app-registry/cnr-server.git && cd cnr-server
2. pip install -e . && pip install gunicorn
3. Run the cnr-server on port 5000 `gunicorn cnr.api.wsgi:app -b :5000`
   or "./run-server"

## storage

### Filesystem (default)
By default package are stored in `/tmp/cnr`
```
STORAGE=filesystem ./run-server.sh
```

### Etcd
```
STORAGE=etcd ./run-server.sh
```

<<<<<<< HEAD
Example:

#### Search
And index is created on package add / delete and stored in:
/cnr/search/index

#### Track delated releases

/cnr/packages/{namespace}/{package_name}/deleted/{release} -> delete-info {digest/deleted_at}
>>>>>>> 5d5d822... Add README
=======
### Redis
```
STORAGE=redis ./run-server.sh
```
>>>>>>> 45405f3... Address package by digest
