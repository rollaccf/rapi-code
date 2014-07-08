import yaml
import datetime
import subprocess

# take picture
def take_picture(settings):
   args = ""
   for arg in settings:
       if settings[arg]:
          args += " --{} {}".format(arg, settings[arg])

   filename = "{}.{}".format(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"), settings['encoding'])
   cmd = "raspistill {args} -o /home/pi/pictures/{filename}".format(args=args, filename=filename)
   print(cmd)
   subprocess.call(cmd.split())
   return filename

# upload picture
if __name__ == "__main__":

    settings = yaml.load(open('settings.yaml'))
    take_picture(settings['raspistill'])
