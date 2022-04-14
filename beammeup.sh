#
# please start this script with sudo rights like: 
# sudo sh beammeup.sh

# show how to open dev site, start docker in another tab and start vue frontend in another tab
gnome-terminal --tab --title="Dengue Dashboard" --command="bash -c 'echo -e Starting services...; sleep 5; echo -e Click here to open your website: http://localhost:8000/; $SHELL'" --tab --title="Docker" --command="bash -c 'docker-compose -f local.yml up; $SHELL'" --tab --title="Vue Frontend" --command="bash -c 'cd vue_frontend; npm run serve; $SHELL'"

