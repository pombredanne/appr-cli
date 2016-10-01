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
# cnr-server
## Install
1. Install etcd from a [recent release](https://github.com/coreos/etcd) and simply run `etcd` with no arguments.
2. pip install cnr-server && pip install gunicorn
3. Run the cnr-server on port 5000 `gunicorn cnr.api.wsgi:app -b :5000`

## Storage
The server stores the contents, multiple datastore can be used and models customized.
Base models are:
 - Package:
    - blob
    - digest
    - release
    - name
    - created_at
 - Channel
    - name
    - releases
    - current

The package is the content that can be addressed via its unique name in the format: "namespace/content-name" or its digest.
Channel allow to organize and tag packages, e.g: channel 'stable'.

### Etcd
The structure in etcd is the following:

``` shell
/cnr/packages/{namespace}/{package_name}/releases/{release} -> package-data {blob/digest/created_at...}
/cnr/packages/{namespace}/{package_name}/channels/{channel_name} -> link/path to a release (/cnr/packages/{namespace}/{package_name}/releases/{release})
/cnr/packages/{namespace}/{package_name}/digests/{digest} -> link/path to a release (/cnr/packages/{namespace}/{package_name}/releases/{release})
```

Example:

#### Search
And index is created on package add / delete and stored in:
/cnr/search/index

#### Track delated releases

/cnr/packages/{namespace}/{package_name}/deleted/{release} -> delete-info {digest/deleted_at}
>>>>>>> 5d5d822... Add README
