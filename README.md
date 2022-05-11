# Gala Games Automated Testing

Perform automated tests against Gala Games pages (games and store) using a combination of:

1. Docker
2. Python
   1. Selenium
   2. pytest
3. Selenium Dynamic Grid with video recording enabled.

## Tests

* From the Games page, I should not be able to launch Town Star without being logged in
* From the Store page, search for an item of your choice
* From the Store page, I should be able to filter Town Star items by Epic Rarity
* From the Store page, I should be able to filter Spider Tank items by Rare Rarity

## Development and Test Environment

* Microsoft Windows 11 Pro 10.0.22000 Build 22000
  * WSL2 Installed and enabled.
  * Running Ubuntu 20.04.4 LTS
    * Python 3.8.10 (Default for Ubuntu 20.04.04 LTS)
* Docker version 20.10.14, build a224086
* Configuration notes:
  *  Docker Desktop -> Settings -> General -> enable "Expose deamon on tcp://localhost:2375 without TLS". (Mac and Windows)
  *  Docker Desktop -> Resources -> WSL INTEGRATION -> Enable integration with additional distros: Ubuntu Enabled

## Instructions
1. Clone the repository locally and change directory to galagamesauto.
   1. `git clone https://github.com/caleb-moniot/galagamesauto.git`
2. Start a standalone Selenium Grid in detached mode using docker-compose-v3-dynamic-grid.yml.
   1. `docker-compose -f docker-compose-v3-dynamic-grid.yml up -d`
3. Build the galagamesauto container.
   1. `docker build -f Dockerfile -t galagamesauto:latest .`
4. Run the tests.
   1. `docker run --network="host" galagamesauto:latest`

## Review

After starting the container, pytest will report pass/fail to the console as tests run. They can be monitored during execution by opening a browser and navigating to http://localhost:4444/ui#/sessions. Once a session is started, select it and enter the password `secret` when prompted. The sessions are short so if they are missed, a recording of each one is stored as a MP4 on the host machine under the assets/{session_guid}/video.mp4.

## Cleanup
After the tests are complete, Selenium Grid can be shut down.
1. `docker-compose -f docker-compose-v3-dynamic-grid.yml down`