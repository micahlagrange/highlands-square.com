#!/bin/bash

set -e

#sudo ruby djangoDeploy.rb staticfiles /usr/local/highlands-square.com/static deploy hsma01p /www/hisquare/static

rsync -a --no-o --no-p /usr/local/highlands-square.com/static/* hsma01p:/www/hisquare/static
