# ovhcloud
Command-line client in Python to access OVH's APIs.

## Requirements

This project is written in Python 3 and uses the following modules :
- [python-ovh](https://github.com/ovh/python-ovh)

You'll also need an OVH credentials file (more info [here](https://github.com/ovh/python-ovh#environment-vars-and-predefined-configuration-files)).  You'll find a dummy file with the sources, which you can fill by submitting [this form](https://eu.api.ovh.com/createToken/).  In a close release, this step won't be necessary.
By default, ovhcloud will check for `~/.ovhcloud/ovh.conf`.

## Usage

```
usage: ovhcloud {get,put,post,delete} url parts [param=value [...]] [-i] [-d conf_dir] [-c conf_file]

Command-line client in Python to access OVH's APIs.

positional arguments:
  {get,put,post,delete}

optional arguments:
  -h, --help            show this help message and exit
  -d conf_dir, --conf-dir conf_dir
                        specify ovhcloud's storage directory
  -c conf_file, --conf-ovh conf_file
                        specify an OVH configuration file path
  -i, --info            display more information on the url parts
```

ovhcloud parses the users arguments based on a specific syntax.  Some optional parameters will require a flag while some won't.  Please have a look below on how to use it :

    ovhcloud get vps

This basic command sends a GET request to the vps API.  In the case of a multi-part url (e.g. /license/cloudLinux/orderableVersions), the syntax is as follows :

    ovhcloud get license cloudLinux orderableVersions


### Optional flags

Flag | Long version | Description
--- | --- | ---
-h | --help | Display parser usage
-i | --info | Will display contextual information based on the url you provided to help you make a correct request
-c | --conf-ovh | Specify the path to your OVH credentials file.  Default : `~/.ovhcloud/`
-d | --conf-dir | Specify where ovhcloud should store its cache etc.  Default : `~/.ovhcloud/ovh.conf`

## POST/PUT parameters
OVH's APIs will sometimes require you (especially in PUT and POST mode) to provide parameters for your request.  To do so, add the parameter name followed by an equal sign and its value to the command line, e.g.:

    ovhcloud post cloud createProject catalogVersion=1 description=foo

## Install

    pip install ovhcloud (not available yet)
    
    OR
    
    python3 setup.py build && sudo python3 setup.py install

## License

This project is under the GPL3 license.

## Acknowledgments

Currently in alpha, user-friendly improvements coming soon.

This project is based on @kartoch 's [ovhcloud](https://github.com/kartoch/ovhcloud) and was made as a part of the PFE class at Lille University (France).
