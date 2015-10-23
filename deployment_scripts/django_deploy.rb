
#!/usr/bin/ruby

STDOUT.sync = true

### This script automates the 2nd part of django deployment, extracting the package and restarting apache.
PKG_TAR_GZ = ARGV[0]
APP_NAME   = ARGV[1]
FILEDIR    = "/www/hisquare"
HOMEDIR    = "/home/deploy/hsma_app"
PYTHON_ENV = "#{HOMEDIR}/env/bin/python3.4"

### These commands are designed for ubuntu, so they are abstracted here to be able to be changed
apachectl_path = "#{FILEDIR}/mod_wsgi-express-8001"
stop_apache = "#{apachectl_path}/apachectl stop"
stop_nginx = "service nginx stop"
start_apache = "#{apachectl_path}/apachectl start"
start_nginx = "service nginx start"

# Check inputs
if !File.directory?(HOMEDIR)
        Kernel.abort("Home directory not present:: #{HOMEDIR}")
end
if !File.directory?(FILEDIR)
	Kernel.abort("Modwsgi directory not present: #{FILEDIR}")
end
if !File.exists?(PKG_TAR_GZ)
        Kernel.abort("Deployment package not present: #{HOMEDIR}/#{PKG_TAR_GZ}")
end
if !File.exists?(PYTHON_ENV)
	Kernel.abort("Python executable not present in home dir: #{PYTHON_ENV}")
end
if !File.directory?(apachectl_path)
        Kernel.abort("No apachectl at #{apachectl_path}. Check that the port is correct")
end
if File.directory?(APP_NAME)
	del_old = "rm -r #{APP_NAME}"
else
	Kernel.abort("Invalid app name provided")
end


# Do deploy
Dir.chdir HOMEDIR
[
	stop_apache,
	del_old,
        "tar xvzf #{PKG_TAR_GZ}",
        start_apache,
	"mv #{PKG_TAR_GZ} archive/"
].each do |command|
        puts command
        system(command)

	if command == stop_apache
		# Give mod_wsgi some time to stop
		sleep(5)
	end
end



