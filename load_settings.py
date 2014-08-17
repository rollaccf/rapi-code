import yaml
import urllib.request
import subprocess

# load settings
def download_settings(name):
    # TODO: deal with errors
    url = "https://dev-master-dot-ccf-website.appspot.com/rapi/{}".format(name)
    filename, headers = urllib.request.urlretrieve(url, "settings.yaml")


if __name__ == "__main__":
    name = "test"
    download_settings(name)

    settings = yaml.load(open("settings.yaml", "r"))

    # TODO: set cron based on settings
    with open("rapi_crontab", 'w') as fh:
        fh.write("* */6 * * * cd /home/pi/scripts && python3 ~/scripts/load_settings.py\n")
        fh.write("*/30 * * * * cd /home/pi/scripts && python3 ~/scripts/take_picture.py\n")

    subprocess.call(["crontab", "rapi_crontab"])
