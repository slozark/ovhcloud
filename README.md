# ovhcloud
Command-line client in Python to access OVH's APIs.

## Usage
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

    pip install ovhcloud

## Acknowledgments

This project is based on @kartoch 's [ovhcloud](https://github.com/kartoch/ovhcloud) and was made as a part of the PFE class at Lille University (France).
