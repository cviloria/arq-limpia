import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]
call("pip uninstall -y " + ' '.join(packages), shell=True)