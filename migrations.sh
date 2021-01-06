#!/bin/bashRun; 
echo "migrating database....................."
export PATH=$PATH:$HOME/bin:$HOME/.rvm/gems/ruby-2.5.3/bin:$HOME/.rvm/rubies/ruby-2.5.3/lib/ruby/gems/2.5.0/bin:$HOME/.rvm/rubies/ruby-2.5.3/bin
rake db:migrate