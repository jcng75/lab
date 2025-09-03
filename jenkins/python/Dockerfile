FROM jenkins/agent:latest-alpine-jdk21
USER root
RUN apk add --no-cache python3 py3-pip \
    && mkdir -p /home/jenkins \
    && chown jenkins:jenkins /home/jenkins
USER jenkins
