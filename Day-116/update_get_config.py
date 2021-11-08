#!/usr/bin/env python3

import json
import sys
from string import Template

OS_TYPE = ["sles12", "rhel8"]
CONFIG_JSON = "platform_config.json"
CONFIG_TEMPLATE = "os_config.template"


def parse_config(os_type):
    with open(CONFIG_JSON, "r") as config:
        data = json.load(config)
    print(data)
    os_baseline = data['os_info']['data'][os_type]['os_baseline']
    installer_baseline = data['os_info']['data'][os_type]['installer_baseline']
    return(os_baseline, installer_baseline)


def generate_config(os_type):
    os_baseline, installer_baseline = parse_config(os_type)
    with open("get_os_config.tmpl", "r") as tmpl:
        # Use templating
        template = Template(tmpl.read())
    final_config = template.substitute(os_Baseline=os_baseline, installer_Baseline=installer_baseline)
    with open("get_os_config.{}".format(os_type), "w") as output:
        output.write(final_config)



if __name__ == "__main__":
    generate_config(sys.argv[1])

