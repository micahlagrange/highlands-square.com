#!/usr/bin/ruby

STDOUT.sync = true

require 'date'
require 'FileUtils'

#### This script is intended to automate Django deployments in an extensible way

if !ARGV[0]
	Kernel.abort("This sript requires paramters: type, source dir, user, host, destination dir")
end

# Constants:

TYPE = ARGV[0]  # either staticfiles, templates or code
SRC = ARGV[1].chomp("/")   # local source directory
USER = ARGV[2]  # remote username
HOST = ARGV[3]  # remote ip
DESTDIR = ARGV[4].chomp("/") # remote desination directory

if ARGV[5]
	PEMKEY = "-i #{ARGV[5]}"  # include pem key in ssh 
else
	PEMKEY = ""               # default to using rsa
end

if !File.directory?(SRC)
	Kernel.abort("Source dir does not exist: #{SRC}")
end


### Functions:

# Use rsync so the same files are not constantly deployed over and over unless the version changes
puts "src: #{SRC}/* | host #{HOST} | destination dir: #{DESTDIR}" 
def deploy_static_files ()
	system("rsync", "-a", "--no-o", "--no-p", "#{USER}@#{SRC}/*", "#{HOST}:#{DESTDIR}")
	# system("ssh", "-t", "#{USER}@#{HOST}", "sudo chmod -R 755 #{DESTDIR}")
	# system("ssh", "-t", "#{USER}@#{HOST}", "sudo chown -R www-data:www-data #{DESTDIR}")
end


# Use scp to transfer code securely to destination
def deploy_code (tmp_dir, package)
	
	# Do deploy
	if File.exists?(package) 

		`scp #{PEMKEY} #{package} #{USER}@#{HOST}:#{DESTDIR}/`
	else
		Kernel.abort("Package doesn't exist at #{package}")
	end	
end


# Prepare code package
def make_package (tmp_dir)
        src_dirname = SRC.split("/").last

	datestr = Time.now.strftime("%Y%m%d_%H%M%S")
        zip_name = "#{src_dirname}_#{datestr}.tar.gz"
	
	puts "Copying files from #{SRC} to #{tmp_dir}..."
	system("rsync -r #{SRC} --exclude static --exclude media --exclude __pycache__ --exclude '*.sqlite3' --exclude '*.pyc' --exclude .c9 #{tmp_dir}")
	
	
	Dir.chdir tmp_dir
	[
		"pwd",
		"tar czf #{zip_name} #{src_dirname}"
	].each do |command|
	  puts command
	  system(command)
	end

	puts "Absolute path to new package: #{tmp_dir}/#{zip_name}"	
        if File.exists?(zip_name)
		package = zip_name
	else
		Kernel.abort("Zip did not work. File doesn't exist: #{zip_name}")
	end
return package
end


### Main code
if TYPE == 'staticfiles'
	deploy_static_files

elsif TYPE == 'code'
	tmp_dir = "djangoDeploy"
	puts "Making tmp directory"
	if !File.directory?(tmp_dir)
		FileUtils.makedirs(tmp_dir)
	end

	package = make_package tmp_dir
	puts "Deploying code to server"
	deploy_code tmp_dir, package	

	puts "Cleaning up..."
	Dir.chdir ".."
	  ["rm -r #{tmp_dir}"].each do |command| 
	  puts command
	  system(command)
	end
else
	puts "You must specify a type of deployment: code | staticfiles "	
end
