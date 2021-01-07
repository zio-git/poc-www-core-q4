#!/bin/bashRun; 
echo "migrating database....................."
export PATH=$PATH:$HOME/bin:$HOME/.rvm/gems/ruby-2.5.3/bin:$HOME/.rvm/rubies/ruby-2.5.3/bin:$HOME/.gem/ruby/2.5.0/bin:$HOME/.rvm/bin:/usr/local/sbin:/usr/local/bin
bundle exec rake db:migrate